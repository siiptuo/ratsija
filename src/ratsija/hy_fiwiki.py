import re

def _transliterate_word(word):
    output = ''
    i = 0
    while i < len(word):
        if word[i] == 'ա':
            output += 'a'
            i += 1
        elif word[i] == 'Ա':
            output += 'A'
            i += 1
        elif word[i] == 'բ':
            output += 'b'
            i += 1
        elif word[i] == 'Բ':
            output += 'B'
            i += 1
        elif word[i] == 'գ':
            output += 'g'
            i += 1
        elif word[i] == 'Գ':
            output += 'G'
            i += 1
        elif word[i] == 'դ':
            output += 'd'
            i += 1
        elif word[i] == 'Դ':
            output += 'D'
            i += 1
        elif i == 0 and word[i] == 'ե':
            output += 'je'
            i += 1
        elif i == 0 and word[i] == 'Ե':
            output += 'Je'
            i += 1
        elif word[i] == 'ե':
            output += 'e'
            i += 1
        elif word[i] == 'Ե':
            output += 'E'
            i += 1
        elif word[i] == 'զ':
            output += 'z'
            i += 1
        elif word[i] == 'Զ':
            output += 'Z'
            i += 1
        elif word[i] == 'է':
            output += 'e'
            i += 1
        elif word[i] == 'Է':
            output += 'E'
            i += 1
        elif word[i] == 'ը':
            output += 'ë'
            i += 1
        elif word[i] == 'Ը':
            output += 'Ë'
            i += 1
        elif word[i] == 'թ':
            output += 't'
            i += 1
        elif word[i] == 'Թ':
            output += 'T'
            i += 1
        elif word[i] == 'ժ':
            output += 'ž'
            i += 1
        elif word[i] == 'Ժ':
            output += 'Ž'
            i += 1
        elif word[i] == 'ի':
            output += 'i'
            i += 1
        elif word[i] == 'Ի':
            output += 'I'
            i += 1
        elif word[i] == 'լ':
            output += 'l'
            i += 1
        elif word[i] == 'Լ':
            output += 'L'
            i += 1
        elif word[i] == 'խ':
            output += 'kh'
            i += 1
        elif word[i] == 'Խ':
            output += 'Kh'
            i += 1
        elif word[i] == 'ծ':
            output += 'ts'
            i += 1
        elif word[i] == 'Ծ':
            output += 'Ts'
            i += 1
        elif word[i] == 'կ':
            output += 'k'
            i += 1
        elif word[i] == 'Կ':
            output += 'K'
            i += 1
        elif word[i] == 'հ':
            output += 'h'
            i += 1
        elif word[i] == 'Հ':
            output += 'H'
            i += 1
        elif word[i] == 'ձ':
            output += 'dz'
            i += 1
        elif word[i] == 'Ձ':
            output += 'Dz'
            i += 1
        elif word[i] == 'ղ':
            output += 'gh'
            i += 1
        elif word[i] == 'Ղ':
            output += 'Gh'
            i += 1
        elif word[i] == 'ճ':
            output += 'tš'
            i += 1
        elif word[i] == 'Ճ':
            output += 'Tš'
            i += 1
        elif word[i] == 'մ':
            output += 'm'
            i += 1
        elif word[i] == 'Մ':
            output += 'M'
            i += 1
        elif word[i] == 'յ':
            output += 'j'
            i += 1
        elif word[i] == 'Յ':
            output += 'J'
            i += 1
        elif word[i] == 'ն':
            output += 'n'
            i += 1
        elif word[i] == 'Ն':
            output += 'N'
            i += 1
        elif word[i] == 'շ':
            output += 'š'
            i += 1
        elif word[i] == 'Շ':
            output += 'Š'
            i += 1
        elif i == 0 and word[i] == 'ո':
            output += 'vo'
            i += 1
        elif i == 0 and word[i] == 'Ո':
            output += 'Vo'
            i += 1
        elif i + 1 <= len(word) - 1 and word[i] == 'ո' and word[i + 1] == 'ւ':
            output += 'u'
            i += 2
        elif i + 1 <= len(word) - 1 and word[i] == 'Ո' and word[i + 1] == 'Ւ':
            output += 'U'
            i += 2
        elif word[i] == 'ո':
            output += 'o'
            i += 1
        elif word[i] == 'Ո':
            output += 'O'
            i += 1
        elif word[i] == 'չ':
            output += 'tš'
            i += 1
        elif word[i] == 'Չ':
            output += 'Tš'
            i += 1
        elif word[i] == 'պ':
            output += 'p'
            i += 1
        elif word[i] == 'Պ':
            output += 'P'
            i += 1
        elif word[i] == 'ջ':
            output += 'j'
            i += 1
        elif word[i] == 'Ջ':
            output += 'J'
            i += 1
        elif word[i] == 'ռ':
            output += 'r'
            i += 1
        elif word[i] == 'Ռ':
            output += 'R'
            i += 1
        elif word[i] == 'ս':
            output += 's'
            i += 1
        elif word[i] == 'Ս':
            output += 'S'
            i += 1
        elif word[i] == 'վ':
            output += 'v'
            i += 1
        elif word[i] == 'Վ':
            output += 'V'
            i += 1
        elif word[i] == 'տ':
            output += 't'
            i += 1
        elif word[i] == 'Տ':
            output += 'T'
            i += 1
        elif word[i] == 'ր':
            output += 'r'
            i += 1
        elif word[i] == 'Ր':
            output += 'R'
            i += 1
        elif word[i] == 'ց':
            output += 'ts'
            i += 1
        elif word[i] == 'Ց':
            output += 'Ts'
            i += 1
        elif word[i] == 'ւ':
            output += 'u'
            i += 1
        elif word[i] == 'Ւ':
            output += 'U'
            i += 1
        elif word[i] == 'փ':
            output += 'p'
            i += 1
        elif word[i] == 'Փ':
            output += 'P'
            i += 1
        elif word[i] == 'ք':
            output += 'k'
            i += 1
        elif word[i] == 'Ք':
            output += 'K'
            i += 1
        elif word[i] == 'օ':
            output += 'o'
            i += 1
        elif word[i] == 'Օ':
            output += 'O'
            i += 1
        elif word[i] == 'ֆ':
            output += 'f'
            i += 1
        elif word[i] == 'Ֆ':
            output += 'F'
            i += 1
        elif i == 0 and word[i] == 'և':
            output += 'jev'
            i += 1
        elif i == 0 and i + 1 <= len(word) - 1 and word[i] == 'Ե' and word[i + 1] == 'Ւ':
            output += 'Jev'
            i += 2
        elif word[i] == 'և':
            output += 'ev'
            i += 1
        elif i + 1 <= len(word) - 1 and word[i] == 'Ե' and word[i + 1] == 'Ւ':
            output += 'Ev'
            i += 2
        else:
            output += word[i]
            i += 1
    return output

def transliterate(text):
    return re.sub(r'\w+', lambda m: _transliterate_word(m[0]), text)
