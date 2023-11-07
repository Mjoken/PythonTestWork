def matchEN(text, alphabet=set('abcdefghijklmnopqrstuvwxyz')):
    return not alphabet.isdisjoint(text.lower())


def matchRU(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())


def text_stat(name):
    stat = {'word_amount': 0, 'paragraph_amount': 0, "bilingual_word_amount": 0}
    try:
        with open(name, "r", encoding='utf-8') as file:
            for line in file:
                line = line.replace("—", " ")
                fileAlphabet = set(line)
                if 'word_amount' in stat:
                    stat['word_amount'] += len(line.split())
                    for word in line.split():
                        for alpha in fileAlphabet:
                            if alpha.isalpha():
                                if not alpha in stat:
                                    stat[alpha] = [word.count(alpha), 0 if word.count(alpha) == 0 else 1]
                                stat[alpha][0] += word.count(alpha)
                                stat[alpha][1] += 0 if word.count(alpha) == 0 else 1
                        if matchRU(word) and matchEN(word):
                            if 'bilingual_word_amount' in stat:
                                stat['bilingual_word_amount'] += 1
                if 'paragraph_amount' in stat:
                    if line[0:4] == "    ":
                        stat['paragraph_amount'] += 1
            for i in stat:
                if i.isalpha():
                    stat[i] = (stat[i][0], stat[i][1])
        return stat
    except FileNotFoundError:
        stat['error'] = "File not found"
        return stat
    except UnicodeDecodeError:
        stat['error'] = "Wrong codec, program can decode only utf-8 and txt format"
        return stat


if __name__ == '__main__':
    print(text_stat("test.txt"))
