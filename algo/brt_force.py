from algo.super import Super

class BF(Super):

    @staticmethod
    def find(substring, text):
        length = len(text)
        length_sm = len(substring)

        # Проходим по индексам строки, но останавливаемся, если длина оставшейся части меньше подстроки
        for i in range(length - length_sm + 1):
            # Проверяем, равен ли срез строки подстроке
            if text[i:i + length_sm] == substring:
                yield i