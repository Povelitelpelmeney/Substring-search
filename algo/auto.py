from algo.super import Super


class DFA(Super):

    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        length = len(text)

        # Построение алфавита на основе подстроки
        alphabet = {ch: 0 for ch in substring}

        # Инициализация таблицы переходов
        delta = [{} for _ in range(sm_length + 1)]

        # Заполнение переходов для начального состояния
        for ch in alphabet:
            delta[0][ch] = 0

        # Заполнение таблицы переходов для всех состояний
        for i in range(sm_length):
            prev = delta[i][substring[i]]
            delta[i][substring[i]] = i + 1  # Переход на следующее состояние при совпадении
            for ch in alphabet:
                delta[i + 1][ch] = delta[prev][ch]  # Переход для остальных символов

        # Поиск подстроки в строке
        condition = 0
        for i in range(length):
            if text[i] in alphabet:
                condition = delta[condition][text[i]]
            else:
                condition = 0

            if condition == sm_length:
                # Найдено совпадение, возвращаем индекс начала
                yield i - sm_length + 1
