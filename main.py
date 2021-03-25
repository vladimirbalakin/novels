words_with_capital_letters = ['I', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                              'September', 'October', 'November', 'December', 'Monday', 'Tuesday', 'Wednesday',
                              'Thursday', 'Friday', 'Saturday', 'Sunday', 'Afghanistan', 'Albania', 'Algeria',
                              'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
                              'Austria', 'Austrian Empire', 'Azerbaijan', 'Baden', 'Bahamas', 'Bahrain', 'Bangladesh',
                              'Barbados', 'Bavaria', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bolivia',
                              'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Brunswick and Lüneburg',
                              'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon',
                              'Canada', 'Cayman Islands', 'Central African Republic', 'Central American Federation',
                              'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo Free State', 'The', 'Costa Rica',
                              'Cote d’Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Czechoslovakia',
                              'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica',
                              'Dominican Republic', 'Duchy of Parma', 'East Germany', 'German Democratic Republic',
                              'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini',
                              'Ethiopia', 'Federal Government of Germany', 'Fiji', 'Finland', 'France', 'Gabon',
                              'Gambia', 'Georgia', 'Germany', 'Ghana', 'Grand Duchy of Tuscany', 'Greece', 'Grenada',
                              'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Hanover',
                              'Hanseatic Republics', 'Hawaii', 'Hesse', 'Holy See', 'Honduras', 'Hungary', 'Iceland',
                              'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
                              'Jordan', 'Kazakhstan', 'Kenya', 'Kingdom of Serbia', 'Yugoslavia', 'Kiribati', 'Korea',
                              'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Lew Chew',
                              'Loochoo', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar',
                              'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
                              'Mauritius', 'Mecklenburg-Schwerin', 'Mecklenburg-Strelitz', 'Mexico', 'Micronesia',
                              'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia',
                              'Nassau', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                              'North German Confederation', 'North German Union', 'North Macedonia', 'Norway',
                              'Oldenburg', 'Oman', 'Orange Free State', 'Pakistan', 'Palau', 'Panama', 'Papal States',
                              'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Piedmont-Sardinia', 'Poland',
                              'Portugal', 'Qatar', 'Republic of Genoa', 'Republic of Korea', 'South Korea',
                              'Republic of the Congo', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
                              'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
                              'Sao Tome and Principe', 'Saudi Arabia', 'Schaumburg-Lippe', 'Senegal', 'Serbia',
                              'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
                              'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                              'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Texas', 'Thailand',
                              'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
                              'Turkmenistan', 'Tuvalu', 'Two Sicilies', 'Uganda', 'Ukraine',
                              'Union of Soviet Socialist Republics', 'United Arab Emirates', 'United Kingdom',
                              'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Württemberg', 'Yemen',
                              'Zambia', 'Zimbabwe']


def reformat_file(name_of_the_file: str) -> None:
    text = open(name_of_the_file, "r").read().replace('.', '. ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    while '\n\n' in text:
        text = text.replace('\n\n', '\n')
    open(name_of_the_file, "w").write(text)


def extract_text_from_file(name_of_the_file: str) -> str:
    return open(name_of_the_file, "r").read()


def get_sentences_from_text(text: str) -> list:
    text = text.replace('. ', '.')
    text = text.replace('\n', ' ')

    while '  ' in text:
        text = text.replace('  ', ' ')

    punctuation_marks_in_sentence = ['/', ',', ':', ';', '(', ')', '"', "'", '-']
    punctuation_marks_in_the_end_of_sentence = ['.', '!', '?']
    sentences = ['']
    for i in text:
        if i != '\n':
            if i not in punctuation_marks_in_sentence:
                sentences[-1] += i
            if i in punctuation_marks_in_the_end_of_sentence:
                sentences[-1] = sentences[-1][:-1]
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


reformat_file("frankenstain.txt")
text = extract_text_from_file("frankenstain.txt")
sentences = get_sentences_from_text(text)
names = sorted(get_names_of_heroes(sentences))
print(names)
