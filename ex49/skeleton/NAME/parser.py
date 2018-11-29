class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

class Sentence_Parser(object):
    def peek(self, word_list):
        if word_list:
            word = word_list[0]
            return word
        else:
            return None

    def match(self, word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(self, word_list, word_type):
        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)

    def parse_verb(self, word_list):
        self.skip(word_list, 'stop')

        if self.peek(word_list)[0] == 'verb':
            return self.match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")

    def parse_object(self, word_list):
        self.skip(word_list, 'stop')
        next = self.peek(word_list)[0]

        if next == 'noun':
            return self.match(word_list, 'noun')
        elif next == 'direction':
            return self.match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, word_list):
        self.skip(word_list, 'stop')
        next_word = self.peek(word_list)[0]

        if next_word == 'noun':
            return self.match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected verb next.")

    def parse_sentence(self, word_list):
        subj = self.parse_subject(word_list)
        verb = self.parse_verb(word_list)
        obj = self.parse_object(word_list)

        return Sentence(subj, verb, obj)


sentence = Sentence_Parser()

x = sentence.parse_sentence([('verb', 'go'), ('direction', 'north')])
print(x.subject, x.verb, x.object)