from algo.super import Super


class DFA(Super):

    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        length = len(text)
        alphabet = {}
        for i in range(sm_length):
            alphabet[substring[i]] = 0
        delta = [{} for _ in range(sm_length + 1)]
        for i in alphabet:
            delta[0][i] = 0
        for i in range(sm_length):
            prev = delta[i][substring[i]]
            delta[i][substring[i]] = i + 1
            for j in alphabet:
                delta[i + 1][j] = delta[prev][j]
        condition = 0
        for i in range(length):
            if text[i] in alphabet.keys():
                condition = delta[condition][text[i]]
            else:
                condition = 0
            if condition == sm_length:
                yield i - sm_length + 1
