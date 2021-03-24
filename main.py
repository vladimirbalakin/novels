def reformat_file(name_of_the_file: str) -> None:
    text = open(name_of_the_file, "r").read().replace('.', '. ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    open(name_of_the_file, "w").write(text)


def extract_text_from_file(name_of_the_file: str) -> str:
    return open(name_of_the_file, "r").read()


def get_sentences_from_text(text: str) -> list:
    text = text.replace('. ', '.')
    punctuation_marks_in_sentence = [' ', '/', ',', ':', ';', '(', ')', '"', "'", '-']
    sentences = ['']
    for i in text:
        if i != '\n':
            sentences[-1] += i
            if not (ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z') or ord('0') <= ord(i) <= ord(
                    '9') or
                    i in punctuation_marks_in_sentence):
                sentences.append('')
    sentences.pop(-1)
    return sentences


def get_names_of_heroes(sentences: list) -> list:
    heroes = set()
    for i in sentences:
        try:
            words = i.split(' ')
            words[-1] = words[-1][:-1]
            for j in words[1::]:
                try:
                    if ord('A') <= ord(j[0]) <= ord('Z'):
                        heroes.add(j)
                except:
                    pass
        except:
            pass
    return list(heroes)


reformat_file("frankenstain.txt")
text = extract_text_from_file("frankenstain.txt")
sentences = get_sentences_from_text(text)
print(get_names_of_heroes(sentences))
