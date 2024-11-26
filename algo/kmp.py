from algo.super import Super


class KMP(Super):
    
    @staticmethod
    def func_prefix(substring: str) -> list:
        length = len(substring)
        pre = [0] * length  # Массив префикс-функции
        i = 0  # Индекс в подстроке для текущего наибольшего совпадающего префикса
        for j in range(1, length):
            while i > 0 and substring[i] != substring[j]:
                i = pre[i - 1]  # Возврат к предыдущему возможному префиксу
            if substring[i] == substring[j]:
                i += 1
            pre[j] = i
        return pre

    @staticmethod
    def find(text: str, substring: str):
        text_len = len(text)
        substring_len = len(substring)
        
        if substring_len == 0 or text_len == 0 or substring_len > text_len:
            return  # Пустая строка или слишком короткий текст

        pre = KMP.func_prefix(substring)  # Префикс-функция для подстроки
        j = 0  # Индекс для подстроки

        for i in range(text_len):
            while j > 0 and text[i] != substring[j]:
                j = pre[j - 1]  # Возврат к предыдущему возможному префиксу

            if text[i] == substring[j]:
                j += 1  # Совпадение символов

            if j == substring_len:  # Найдено полное совпадение
                yield i - substring_len + 1
                j = pre[j - 1]  # Переход к следующему возможному совпадению
