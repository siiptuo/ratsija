import re

def _transliterate_word(word):
    output = ''
    i = 0
    while i < len(word):
        if word[i] == '\u0430':
            output += '\u0061'
            i += 1
        elif word[i] == '\u0410':
            output += '\u0041'
            i += 1
        elif word[i] == '\u0431':
            output += '\u0062'
            i += 1
        elif word[i] == '\u0411':
            output += '\u0042'
            i += 1
        elif word[i] == '\u0432':
            output += '\u0076'
            i += 1
        elif word[i] == '\u0412':
            output += '\u0056'
            i += 1
        elif word[i] == '\u0433':
            output += '\u0067'
            i += 1
        elif word[i] == '\u0413':
            output += '\u0047'
            i += 1
        elif word[i] == '\u0434':
            output += '\u0064'
            i += 1
        elif word[i] == '\u0414':
            output += '\u0044'
            i += 1
        elif i > 0 and word[i - 1] == '\u0431' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0411' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0431' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0432' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0412' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0432' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0433' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0413' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0433' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0434' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0414' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0434' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0436' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0416' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0436' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0437' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0417' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0437' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0439' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0419' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0439' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u043a' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u041a' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u043a' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u043b' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u041b' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u043b' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u043c' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u041c' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u043c' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u043d' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u041d' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u043d' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u043f' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u041f' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u043f' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0440' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0420' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0440' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0441' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0421' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0441' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0442' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0422' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0442' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0444' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0424' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0444' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0445' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0425' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0445' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0446' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0426' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0446' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0447' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0427' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0447' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0448' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0428' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0448' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif i > 0 and word[i - 1] == '\u0449' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0429' and word[i] == '\u0435':
            output += '\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0449' and word[i] == '\u0415':
            output += '\u0045'
            i += 1
        elif word[i] == '\u0435':
            output += '\u006a\u0065'
            i += 1
        elif word[i] == '\u0415':
            output += '\u004a\u0065'
            i += 1
        elif i > 0 and word[i - 1] == '\u0436' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0416' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0436' and word[i] == '\u0401':
            output += '\u004f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0447' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0427' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0447' and word[i] == '\u0401':
            output += '\u004f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0448' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0428' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0448' and word[i] == '\u0401':
            output += '\u004f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0449' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0429' and word[i] == '\u0451':
            output += '\u006f'
            i += 1
        elif i > 0 and word[i - 1] == '\u0449' and word[i] == '\u0401':
            output += '\u004f'
            i += 1
        elif word[i] == '\u0451':
            output += '\u006a\u006f'
            i += 1
        elif word[i] == '\u0401':
            output += '\u004a\u006f'
            i += 1
        elif word[i] == '\u0436':
            output += '\u017e'
            i += 1
        elif word[i] == '\u0416':
            output += '\u017d'
            i += 1
        elif word[i] == '\u0437':
            output += '\u007a'
            i += 1
        elif word[i] == '\u0417':
            output += '\u005a'
            i += 1
        elif i > 0 and word[i - 1] == '\u044c' and word[i] == '\u0438':
            output += '\u006a\u0069'
            i += 1
        elif i > 0 and word[i - 1] == '\u042c' and word[i] == '\u0438':
            output += '\u006a\u0069'
            i += 1
        elif i > 0 and word[i - 1] == '\u044c' and word[i] == '\u0418':
            output += '\u004a\u0069'
            i += 1
        elif word[i] == '\u0438':
            output += '\u0069'
            i += 1
        elif word[i] == '\u0418':
            output += '\u0049'
            i += 1
        elif i > 0 and word[i - 1] == '\u0438' and word[i] == '\u0439' and i == len(word) - 1:
            output += ''
            i += 1
        elif i > 0 and word[i - 1] == '\u0418' and word[i] == '\u0439' and i == len(word) - 1:
            output += ''
            i += 1
        elif i > 0 and word[i - 1] == '\u0438' and word[i] == '\u0419' and i == len(word) - 1:
            output += ''
            i += 1
        elif i == 0 and word[i] == '\u0439':
            output += '\u006a'
            i += 1
        elif i == 0 and word[i] == '\u0419':
            output += '\u004a'
            i += 1
        elif i > 0 and word[i - 1] == '\u0438' and word[i] == '\u0439':
            output += '\u006a'
            i += 1
        elif i > 0 and word[i - 1] == '\u0418' and word[i] == '\u0439':
            output += '\u006a'
            i += 1
        elif i > 0 and word[i - 1] == '\u0438' and word[i] == '\u0419':
            output += '\u004a'
            i += 1
        elif word[i] == '\u0439':
            output += '\u0069'
            i += 1
        elif word[i] == '\u0419':
            output += '\u0049'
            i += 1
        elif word[i] == '\u043a':
            output += '\u006b'
            i += 1
        elif word[i] == '\u041a':
            output += '\u004b'
            i += 1
        elif word[i] == '\u043b':
            output += '\u006c'
            i += 1
        elif word[i] == '\u041b':
            output += '\u004c'
            i += 1
        elif word[i] == '\u043c':
            output += '\u006d'
            i += 1
        elif word[i] == '\u041c':
            output += '\u004d'
            i += 1
        elif word[i] == '\u043d':
            output += '\u006e'
            i += 1
        elif word[i] == '\u041d':
            output += '\u004e'
            i += 1
        elif word[i] == '\u043e':
            output += '\u006f'
            i += 1
        elif word[i] == '\u041e':
            output += '\u004f'
            i += 1
        elif word[i] == '\u043f':
            output += '\u0070'
            i += 1
        elif word[i] == '\u041f':
            output += '\u0050'
            i += 1
        elif word[i] == '\u0440':
            output += '\u0072'
            i += 1
        elif word[i] == '\u0420':
            output += '\u0052'
            i += 1
        elif word[i] == '\u0441':
            output += '\u0073'
            i += 1
        elif word[i] == '\u0421':
            output += '\u0053'
            i += 1
        elif word[i] == '\u0442':
            output += '\u0074'
            i += 1
        elif word[i] == '\u0422':
            output += '\u0054'
            i += 1
        elif word[i] == '\u0443':
            output += '\u0075'
            i += 1
        elif word[i] == '\u0423':
            output += '\u0055'
            i += 1
        elif word[i] == '\u0444':
            output += '\u0066'
            i += 1
        elif word[i] == '\u0424':
            output += '\u0046'
            i += 1
        elif word[i] == '\u0445':
            output += '\u0068'
            i += 1
        elif word[i] == '\u0425':
            output += '\u0048'
            i += 1
        elif word[i] == '\u0446':
            output += '\u0074\u0073'
            i += 1
        elif word[i] == '\u0426':
            output += '\u0054\u0073'
            i += 1
        elif word[i] == '\u0447':
            output += '\u0074\u0161'
            i += 1
        elif word[i] == '\u0427':
            output += '\u0054\u0161'
            i += 1
        elif word[i] == '\u0448':
            output += '\u0161'
            i += 1
        elif word[i] == '\u0428':
            output += '\u0160'
            i += 1
        elif word[i] == '\u0449':
            output += '\u0161\u0074\u0161'
            i += 1
        elif word[i] == '\u0429':
            output += '\u0160\u0074\u0161'
            i += 1
        elif word[i] == '\u044a':
            output += ''
            i += 1
        elif word[i] == '\u042a':
            output += ''
            i += 1
        elif word[i] == '\u044b':
            output += '\u0079'
            i += 1
        elif word[i] == '\u042b':
            output += '\u0059'
            i += 1
        elif word[i] == '\u044c':
            output += ''
            i += 1
        elif word[i] == '\u042c':
            output += ''
            i += 1
        elif word[i] == '\u044d':
            output += '\u0065'
            i += 1
        elif word[i] == '\u042d':
            output += '\u0045'
            i += 1
        elif word[i] == '\u044e':
            output += '\u006a\u0075'
            i += 1
        elif word[i] == '\u042e':
            output += '\u004a\u0075'
            i += 1
        elif word[i] == '\u044f':
            output += '\u006a\u0061'
            i += 1
        elif word[i] == '\u042f':
            output += '\u004a\u0061'
            i += 1
        elif word[i] == '\u0301':
            output += ''
            i += 1
        elif word[i] == '\u0301':
            output += ''
            i += 1
        else:
            output += word[i]
            i += 1
    return output

def transliterate(text):
    return re.sub(r'[\w\u0300-\u036f]+', lambda m: _transliterate_word(m[0]), text)
