import re

def _transliterate_word(word):
    output = ''
    i = 0
    while i < len(word):
        if word[i] == 'а':
            output += 'a'
            i += 1
        elif word[i] == 'А':
            output += 'A'
            i += 1
        elif word[i] == 'б':
            output += 'b'
            i += 1
        elif word[i] == 'Б':
            output += 'B'
            i += 1
        elif word[i] == 'в':
            output += 'v'
            i += 1
        elif word[i] == 'В':
            output += 'V'
            i += 1
        elif word[i] == 'г':
            output += 'g'
            i += 1
        elif word[i] == 'Г':
            output += 'G'
            i += 1
        elif word[i] == 'д':
            output += 'd'
            i += 1
        elif word[i] == 'Д':
            output += 'D'
            i += 1
        elif i > 0 and word[i - 1] == 'б' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Б' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'б' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'в' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'В' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'в' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'г' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Г' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'г' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'д' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Д' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'д' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'ж' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Ж' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'ж' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'з' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'З' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'з' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'й' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Й' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'й' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'к' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'К' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'к' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'л' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Л' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'л' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'м' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'М' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'м' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'н' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Н' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'н' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'п' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'П' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'п' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'р' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Р' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'р' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'с' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'С' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'с' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'т' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Т' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'т' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'ф' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Ф' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'ф' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'х' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Х' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'х' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'ц' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Ц' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'ц' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'ч' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Ч' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'ч' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'ш' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Ш' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'ш' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif i > 0 and word[i - 1] == 'щ' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'Щ' and word[i] == 'е':
            output += 'e'
            i += 1
        elif i > 0 and word[i - 1] == 'щ' and word[i] == 'Е':
            output += 'E'
            i += 1
        elif word[i] == 'е':
            output += 'je'
            i += 1
        elif word[i] == 'Е':
            output += 'Je'
            i += 1
        elif i > 0 and word[i - 1] == 'ж' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'Ж' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'ж' and word[i] == 'Ё':
            output += 'O'
            i += 1
        elif i > 0 and word[i - 1] == 'ч' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'Ч' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'ч' and word[i] == 'Ё':
            output += 'O'
            i += 1
        elif i > 0 and word[i - 1] == 'ш' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'Ш' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'ш' and word[i] == 'Ё':
            output += 'O'
            i += 1
        elif i > 0 and word[i - 1] == 'щ' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'Щ' and word[i] == 'ё':
            output += 'o'
            i += 1
        elif i > 0 and word[i - 1] == 'щ' and word[i] == 'Ё':
            output += 'O'
            i += 1
        elif word[i] == 'ё':
            output += 'jo'
            i += 1
        elif word[i] == 'Ё':
            output += 'Jo'
            i += 1
        elif word[i] == 'ж':
            output += 'ž'
            i += 1
        elif word[i] == 'Ж':
            output += 'Ž'
            i += 1
        elif word[i] == 'з':
            output += 'z'
            i += 1
        elif word[i] == 'З':
            output += 'Z'
            i += 1
        elif i > 0 and word[i - 1] == 'ь' and word[i] == 'и':
            output += 'ji'
            i += 1
        elif i > 0 and word[i - 1] == 'Ь' and word[i] == 'и':
            output += 'ji'
            i += 1
        elif i > 0 and word[i - 1] == 'ь' and word[i] == 'И':
            output += 'Ji'
            i += 1
        elif word[i] == 'и':
            output += 'i'
            i += 1
        elif word[i] == 'И':
            output += 'I'
            i += 1
        elif i > 0 and word[i - 1] == 'и' and word[i] == 'й' and i == len(word) - 1:
            output += ''
            i += 1
        elif i > 0 and word[i - 1] == 'И' and word[i] == 'й' and i == len(word) - 1:
            output += ''
            i += 1
        elif i > 0 and word[i - 1] == 'и' and word[i] == 'Й' and i == len(word) - 1:
            output += ''
            i += 1
        elif i == 0 and word[i] == 'й':
            output += 'j'
            i += 1
        elif i == 0 and word[i] == 'Й':
            output += 'J'
            i += 1
        elif i > 0 and word[i - 1] == 'и' and word[i] == 'й':
            output += 'j'
            i += 1
        elif i > 0 and word[i - 1] == 'И' and word[i] == 'й':
            output += 'j'
            i += 1
        elif i > 0 and word[i - 1] == 'и' and word[i] == 'Й':
            output += 'J'
            i += 1
        elif word[i] == 'й':
            output += 'i'
            i += 1
        elif word[i] == 'Й':
            output += 'I'
            i += 1
        elif word[i] == 'к':
            output += 'k'
            i += 1
        elif word[i] == 'К':
            output += 'K'
            i += 1
        elif word[i] == 'л':
            output += 'l'
            i += 1
        elif word[i] == 'Л':
            output += 'L'
            i += 1
        elif word[i] == 'м':
            output += 'm'
            i += 1
        elif word[i] == 'М':
            output += 'M'
            i += 1
        elif word[i] == 'н':
            output += 'n'
            i += 1
        elif word[i] == 'Н':
            output += 'N'
            i += 1
        elif word[i] == 'о':
            output += 'o'
            i += 1
        elif word[i] == 'О':
            output += 'O'
            i += 1
        elif word[i] == 'п':
            output += 'p'
            i += 1
        elif word[i] == 'П':
            output += 'P'
            i += 1
        elif word[i] == 'р':
            output += 'r'
            i += 1
        elif word[i] == 'Р':
            output += 'R'
            i += 1
        elif word[i] == 'с':
            output += 's'
            i += 1
        elif word[i] == 'С':
            output += 'S'
            i += 1
        elif word[i] == 'т':
            output += 't'
            i += 1
        elif word[i] == 'Т':
            output += 'T'
            i += 1
        elif word[i] == 'у':
            output += 'u'
            i += 1
        elif word[i] == 'У':
            output += 'U'
            i += 1
        elif word[i] == 'ф':
            output += 'f'
            i += 1
        elif word[i] == 'Ф':
            output += 'F'
            i += 1
        elif word[i] == 'х':
            output += 'h'
            i += 1
        elif word[i] == 'Х':
            output += 'H'
            i += 1
        elif word[i] == 'ц':
            output += 'ts'
            i += 1
        elif word[i] == 'Ц':
            output += 'Ts'
            i += 1
        elif word[i] == 'ч':
            output += 'tš'
            i += 1
        elif word[i] == 'Ч':
            output += 'Tš'
            i += 1
        elif word[i] == 'ш':
            output += 'š'
            i += 1
        elif word[i] == 'Ш':
            output += 'Š'
            i += 1
        elif word[i] == 'щ':
            output += 'štš'
            i += 1
        elif word[i] == 'Щ':
            output += 'Štš'
            i += 1
        elif word[i] == 'ъ':
            output += ''
            i += 1
        elif word[i] == 'Ъ':
            output += ''
            i += 1
        elif word[i] == 'ы':
            output += 'y'
            i += 1
        elif word[i] == 'Ы':
            output += 'Y'
            i += 1
        elif word[i] == 'ь':
            output += ''
            i += 1
        elif word[i] == 'Ь':
            output += ''
            i += 1
        elif word[i] == 'э':
            output += 'e'
            i += 1
        elif word[i] == 'Э':
            output += 'E'
            i += 1
        elif word[i] == 'ю':
            output += 'ju'
            i += 1
        elif word[i] == 'Ю':
            output += 'Ju'
            i += 1
        elif word[i] == 'я':
            output += 'ja'
            i += 1
        elif word[i] == 'Я':
            output += 'Ja'
            i += 1
        else:
            output += word[i]
            i += 1
    return output

def transliterate(text):
    return re.sub(r'\w+', lambda m: _transliterate_word(m[0]), text)
