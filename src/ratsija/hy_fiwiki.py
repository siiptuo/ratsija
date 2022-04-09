import re

def _transliterate_word(word):
    output = ''
    i = 0
    while i < len(word):
        if word[i] == '\u0561':
            output += '\u0061'
            i += 1
        elif word[i] == '\u0531':
            output += '\u0041'
            i += 1
        elif word[i] == '\u0562':
            output += '\u0062'
            i += 1
        elif word[i] == '\u0532':
            output += '\u0042'
            i += 1
        elif word[i] == '\u0563':
            output += '\u0067'
            i += 1
        elif word[i] == '\u0533':
            output += '\u0047'
            i += 1
        elif word[i] == '\u0564':
            output += '\u0064'
            i += 1
        elif word[i] == '\u0534':
            output += '\u0044'
            i += 1
        elif i == 0 and word[i] == '\u0565':
            output += '\u006a\u0065'
            i += 1
        elif i == 0 and word[i] == '\u0535':
            output += '\u004a\u0065'
            i += 1
        elif word[i] == '\u0565':
            output += '\u0065'
            i += 1
        elif word[i] == '\u0535':
            output += '\u0045'
            i += 1
        elif word[i] == '\u0566':
            output += '\u007a'
            i += 1
        elif word[i] == '\u0536':
            output += '\u005a'
            i += 1
        elif word[i] == '\u0567':
            output += '\u0065'
            i += 1
        elif word[i] == '\u0537':
            output += '\u0045'
            i += 1
        elif word[i] == '\u0568':
            output += '\u00eb'
            i += 1
        elif word[i] == '\u0538':
            output += '\u00cb'
            i += 1
        elif word[i] == '\u0569':
            output += '\u0074'
            i += 1
        elif word[i] == '\u0539':
            output += '\u0054'
            i += 1
        elif word[i] == '\u056a':
            output += '\u017e'
            i += 1
        elif word[i] == '\u053a':
            output += '\u017d'
            i += 1
        elif word[i] == '\u056b':
            output += '\u0069'
            i += 1
        elif word[i] == '\u053b':
            output += '\u0049'
            i += 1
        elif word[i] == '\u056c':
            output += '\u006c'
            i += 1
        elif word[i] == '\u053c':
            output += '\u004c'
            i += 1
        elif word[i] == '\u056d':
            output += '\u006b\u0068'
            i += 1
        elif word[i] == '\u053d':
            output += '\u004b\u0068'
            i += 1
        elif word[i] == '\u056e':
            output += '\u0074\u0073'
            i += 1
        elif word[i] == '\u053e':
            output += '\u0054\u0073'
            i += 1
        elif word[i] == '\u056f':
            output += '\u006b'
            i += 1
        elif word[i] == '\u053f':
            output += '\u004b'
            i += 1
        elif word[i] == '\u0570':
            output += '\u0068'
            i += 1
        elif word[i] == '\u0540':
            output += '\u0048'
            i += 1
        elif word[i] == '\u0571':
            output += '\u0064\u007a'
            i += 1
        elif word[i] == '\u0541':
            output += '\u0044\u007a'
            i += 1
        elif word[i] == '\u0572':
            output += '\u0067\u0068'
            i += 1
        elif word[i] == '\u0542':
            output += '\u0047\u0068'
            i += 1
        elif word[i] == '\u0573':
            output += '\u0074\u0161'
            i += 1
        elif word[i] == '\u0543':
            output += '\u0054\u0161'
            i += 1
        elif word[i] == '\u0574':
            output += '\u006d'
            i += 1
        elif word[i] == '\u0544':
            output += '\u004d'
            i += 1
        elif word[i] == '\u0575':
            output += '\u006a'
            i += 1
        elif word[i] == '\u0545':
            output += '\u004a'
            i += 1
        elif word[i] == '\u0576':
            output += '\u006e'
            i += 1
        elif word[i] == '\u0546':
            output += '\u004e'
            i += 1
        elif word[i] == '\u0577':
            output += '\u0161'
            i += 1
        elif word[i] == '\u0547':
            output += '\u0160'
            i += 1
        elif i == 0 and word[i] == '\u0578':
            output += '\u0076\u006f'
            i += 1
        elif i == 0 and word[i] == '\u0548':
            output += '\u0056\u006f'
            i += 1
        elif i + 1 <= len(word) - 1 and word[i] == '\u0578' and word[i + 1] == '\u0582':
            output += '\u0075'
            i += 2
        elif i + 1 <= len(word) - 1 and word[i] == '\u0548' and word[i + 1] == '\u0552':
            output += '\u0055'
            i += 2
        elif word[i] == '\u0578':
            output += '\u006f'
            i += 1
        elif word[i] == '\u0548':
            output += '\u004f'
            i += 1
        elif word[i] == '\u0579':
            output += '\u0074\u0161'
            i += 1
        elif word[i] == '\u0549':
            output += '\u0054\u0161'
            i += 1
        elif word[i] == '\u057a':
            output += '\u0070'
            i += 1
        elif word[i] == '\u054a':
            output += '\u0050'
            i += 1
        elif word[i] == '\u057b':
            output += '\u006a'
            i += 1
        elif word[i] == '\u054b':
            output += '\u004a'
            i += 1
        elif word[i] == '\u057c':
            output += '\u0072'
            i += 1
        elif word[i] == '\u054c':
            output += '\u0052'
            i += 1
        elif word[i] == '\u057d':
            output += '\u0073'
            i += 1
        elif word[i] == '\u054d':
            output += '\u0053'
            i += 1
        elif word[i] == '\u057e':
            output += '\u0076'
            i += 1
        elif word[i] == '\u054e':
            output += '\u0056'
            i += 1
        elif word[i] == '\u057f':
            output += '\u0074'
            i += 1
        elif word[i] == '\u054f':
            output += '\u0054'
            i += 1
        elif word[i] == '\u0580':
            output += '\u0072'
            i += 1
        elif word[i] == '\u0550':
            output += '\u0052'
            i += 1
        elif word[i] == '\u0581':
            output += '\u0074\u0073'
            i += 1
        elif word[i] == '\u0551':
            output += '\u0054\u0073'
            i += 1
        elif word[i] == '\u0582':
            output += '\u0075'
            i += 1
        elif word[i] == '\u0552':
            output += '\u0055'
            i += 1
        elif word[i] == '\u0583':
            output += '\u0070'
            i += 1
        elif word[i] == '\u0553':
            output += '\u0050'
            i += 1
        elif word[i] == '\u0584':
            output += '\u006b'
            i += 1
        elif word[i] == '\u0554':
            output += '\u004b'
            i += 1
        elif word[i] == '\u0585':
            output += '\u006f'
            i += 1
        elif word[i] == '\u0555':
            output += '\u004f'
            i += 1
        elif word[i] == '\u0586':
            output += '\u0066'
            i += 1
        elif word[i] == '\u0556':
            output += '\u0046'
            i += 1
        elif i == 0 and word[i] == '\u0587':
            output += '\u006a\u0065\u0076'
            i += 1
        elif i == 0 and i + 1 <= len(word) - 1 and word[i] == '\u0535' and word[i + 1] == '\u0552':
            output += '\u004a\u0065\u0076'
            i += 2
        elif word[i] == '\u0587':
            output += '\u0065\u0076'
            i += 1
        elif i + 1 <= len(word) - 1 and word[i] == '\u0535' and word[i + 1] == '\u0552':
            output += '\u0045\u0076'
            i += 2
        else:
            output += word[i]
            i += 1
    return output

def transliterate(text):
    return re.sub(r'[\w\u0300-\u036f]+', lambda m: _transliterate_word(m[0]), text)
