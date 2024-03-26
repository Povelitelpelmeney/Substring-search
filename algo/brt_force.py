from algo.super import Super


class BF(Super):

    @staticmethod
    def find(substring, text):
        length = len(text)
        length_sm = len(substring)
        for i in range(length):
            if text[i: i + length_sm: 1] == substring:
                yield i
