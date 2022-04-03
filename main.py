# SPDX-FileCopyrightText: 2022 Tuomas Siipola
# SPDX-License-Identifier: CC0-1.0

import re
import sys
from pathlib import Path
import shutil

class Transliterator:
    def __init__(self, path: Path):
        self.name = path.stem.replace('-', '_')
        self.rules = []
        self.examples = []
        with path.open() as f:
            mode = None
            for line in f:
                if line.startswith('#'):
                    continue
                elif m := re.match(r"\[(.*)\]", line):
                    mode = m[1]
                elif mode == "rules":
                    before, value, after, replacement = line.removesuffix('\n').split('\t')
                    assert len(before) <= 1
                    assert len(after) <= 1
                    self.rules.append((before, value, after, replacement))
                elif mode == "examples":
                    inp, out = line.removesuffix('\n').split('\t')
                    self.examples.append((inp, out))
                else:
                    raise Exception(f"Unknown mode: {mode}")

def capitalize_rules(tr):
    rules = []
    for before, value, after, replacement in tr.rules:
        rules.append((before, value, after, replacement))
        if before not in ('', '^'):
            rules.append((before.upper(), value, after, replacement))
        rules.append((before, value.upper(), after, replacement.capitalize()))
    tr.rules = rules

def generate_main(tr):
    code = ''
    code += 'import re\n'
    code += '\n'
    code += "def _transliterate_word(word):\n"
    code += "    output = ''\n"
    code += "    i = 0\n"
    code += "    while i < len(word):\n"
    for i, (before, value, after, replacement) in enumerate(tr.rules):
        conditions = []
        if before == '^':
            conditions.append(f"i == 0")
        elif before:
            conditions.append("i > 0")
            conditions.append(f"word[i - 1] == '{before}'")
        if len(value) > 1:
            conditions.append(f"i + {len(value) - 1} <= len(word) - 1")
        for j, symbol in enumerate(value):
            if j == 0:
                conditions.append(f"word[i] == '{symbol}'")
            else:
                conditions.append(f"word[i + {j}] == '{symbol}'")
        if after == '$':
            conditions.append("i == len(word) - 1")
        elif after:
            conditions.append("i < len(word) - 1")
            conditions.append(f"word[i + 1] == '{after}'")
        if i == 0:
            code += "        if "
        else:
            code += "        elif "
        code += ' and '.join(conditions)
        code += ":\n"
        code += f"            output += '{replacement}'\n"
        code += f"            i += {str(len(value))}\n"
    code += "        else:\n"
    code += "            output += word[i]\n"
    code += "            i += 1\n"
    code += "    return output\n"
    code += "\n"
    code += f"def {tr.name}(text):\n"
    code += "    return re.sub(r'\w+', lambda m: _transliterate_word(m[0]), text)\n"
    return code

def generate_test(tr):
    code = "import unittest\n"
    code += f"from ratsija import {tr.name}\n"
    code += "\n"
    code += "class TestTransliterate(unittest.TestCase):\n"
    for i, (inp, exp) in enumerate(tr.examples):
        code += f"    def test_example{i + 1}(self):\n"
        code += f"        self.assertEqual({tr.name}('{inp}'), '{exp}')\n"
        code += "\n"
    code += "if __name__ == '__main__':\n"
    code += "    unittest.main()\n"
    return code

for child in Path('rules').iterdir():
    tr = Transliterator(child)
    capitalize_rules(tr)

    root = Path('build/python')

    shutil.copy(Path('LICENSES/CC0-1.0.txt'), root / 'LICENSE')
    (root / 'pyproject.toml').write_text('''[build-system]
requires = ["setuptools>=42"]
build-backend = "setuptools.build_meta"
''')

    (root / 'setup.cfg').write_text('''[metadata]
name = ratsija
version = 0.0.1
author = Tuomas Siipola
author_email = tuomas@zpl.fi
description = Transliteration library
url = https://github.com/siiptuo/ratsija
project_urls =
    Bug Tracker = https://github.com/siiptuo/ratsija/issues
classifiers =
    Development Status :: 2 - Pre-Alpha
    License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Operating System :: OS Independent
    Programming Language :: Python :: 3

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src''')

    src = root / 'src/ratsija'
    src.mkdir(parents=True, exist_ok=True)
    (src / '__init__.py').touch()
    (src / f'{tr.name}.py').write_text(generate_main(tr))

    tests = root / 'tests'
    tests.mkdir(parents=True, exist_ok=True)
    (tests / f'{tr.name}.py').write_text(generate_test(tr))
