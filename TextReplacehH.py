text = input('Введите текст: ')
if text.find('h') != -1:
    start = text.find('h')
    end = text.rfind('h')
    if start == end:
        print('В этом тексте одна буква h:', text)
    else:
        textbegin = text[:start + 1]
        textend = text[end:]
        textmiddle = text[start + 1:end]
        textmiddle = textmiddle.replace('h', 'H')
        newText = textbegin + textmiddle + textend
        print('Заменили h на H:', newText)
else:
    print('В этом тексте нет буквы h:', text)
