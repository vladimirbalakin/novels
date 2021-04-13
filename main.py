import json
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import pydot


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
    for i in list(heroes):
        if i[:-1] in heroes:
            heroes.remove(i)
    return list(heroes)


def get_graph_from_sentences(sentences: list, heroes: list):
    g = nx.Graph()
    g.add_nodes_from(heroes)
    for i in sentences:
        list_of_nodes = []
        for word in i.split():
            if word in heroes or (word[-1] == 's' and word[:-1] in heroes):
                if word[-1] == 's' and word[:-1] in heroes:
                    list_of_nodes.append(word[:-1])
                else:
                    list_of_nodes.append(word)
        for j in range(len(list_of_nodes)):
            for k in range(j + 1, len(list_of_nodes)):
                g.add_edge(list_of_nodes[k], list_of_nodes[j])
    return g


words_with_capital_letters = read_from_json_file("words_with_capital_letters.json")
main_file = "The Rajah's Diamond.txt"
reformat_file(main_file)
text = extract_text_from_file(main_file)
sentences = get_sentences_from_text(text)
names = sorted(get_names_of_heroes(sentences))
g = get_graph_from_sentences(sentences, names)
pos = graphviz_layout(g, prog="dot")
labels = defaultdict(str)
for node in g.nodes():
    labels[node] = node

# nx.draw_networkx_nodes(g, pos, names)
nx.draw_networkx_labels(g, pos, labels)
# nx.draw_networkx_edges(g, pos, edgelist=g.edges)
nx.draw(g, pos)
plt.show()
print(names)
