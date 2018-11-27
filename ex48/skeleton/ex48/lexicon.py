class sentence(object):
    def __init__(self):
        self.directions = ['north', 'south', 'east', 'west', 'down', 'up',
                           'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stops = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']


    def convert_number(self, num):
        try:
            return int(num)
        except ValueError:
            return None

    def sentence_parse(self, sentence):
        sent_list = sentence.split(" ")
        result = []

        for word in sent_list:
            if word in self.directions:
                result.append(("direction", word))
            elif word in self.verbs:
                result.append(("verb", word))
            elif word in self.stops:
                result.append(("stop", word))
            elif word in self.nouns:
                result.append(("noun", word))
            elif self.convert_number(word):
                result.append(("number", self.convert_number(word)))
            else:
                result.append(("error", word))
        return result

    def scan(self, sentence):
        return self.sentence_parse(sentence)

# sent = lexicon()
#
# print(sent.scan("ASDFADFASDF"))
