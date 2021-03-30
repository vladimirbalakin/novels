import json


def read_from_json_file(name):
    with open(name, "r") as input_file:
        data = json.load(input_file)
    input_file.close()
    return data


def write_to_json_file(name, data):
    with open(name, "w") as output_file:
        json.dump(data, output_file)


def reformat_file(name_of_the_file: str) -> None:
    data = open(name_of_the_file, "r").read().replace('.', '. ')
    while '  ' in data:
        data = data.replace('  ', ' ')
    while '\n\n' in data:
        data = data.replace('\n\n', '\n')
    open(name_of_the_file, "w").write(data)


def extract_text_from_file(name_of_the_file: str) -> str:
    return open(name_of_the_file, "r").read()


def get_sentences_from_text(data: str) -> list:
    data = data.replace('. ', '.')
    data = data.replace('\n', ' ')

    while '  ' in data:
        data = data.replace('  ', ' ')

    punctuation_marks_in_sentence = ['/', ',', ':', ';', '(', ')', '"', "'", '-']
    punctuation_marks_in_the_end_of_sentence = ['.', '!', '?']
    sentences = ['']
    for i in data:
        if i != '\n':
            if i not in punctuation_marks_in_sentence:
                sentences[-1] += i
            if i in punctuation_marks_in_the_end_of_sentence:
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
                    if ord('A') <= ord(j[0]) <= ord('Z') and j not in words_with_capital_letters:
                        heroes.add(j)
                except:
                    pass
        except:
            pass
    return list(heroes)


words_with_capital_letters = read_from_json_file("words_with_capital_letters.json")
main_file = "The Rajah's Diamond.txt"
reformat_file(main_file)
text = extract_text_from_file(main_file)
sentences = get_sentences_from_text(text)
names = sorted(get_names_of_heroes(sentences))
print(names)
