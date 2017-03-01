import nltk


DATA = """
Open consumer-web page
Search for a zip-code
Verify results exist
"""

fixtures = ['open app', '', '']

training_data = [
    ("open the url", "open"),
    ("start the application", "open"),
    ("search for the text", "find"),
    ("verify that the result exists", "verify"),
    ("check if data is present in the page", "verify"),
    ("validate the result", "verify")
]


def action(sentence):
    return {'action':str(sentence.split()[0]).strip()}


def get_nouns(sentence):
    tagged_sent = nltk.tag.pos_tag(sentence.split()[1:])
    nouns = []
    for (item, tag)  in tagged_sent:
        if tag == 'NN':
            nouns.append(item)
    return item



def main():
    training_set = [(action(f), l) for (f, l) in training_data]
    noun_set = [get_nouns(f) for (f, l) in training_data]
    cl = nltk.NaiveBayesClassifier.train(training_set)
    data_set = DATA.split('\n')
    for sent in data_set:
        if len(sent) > 0:
            print cl.classify(action(sent.lower()))


if __name__ == '__main__':
    main()