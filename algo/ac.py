from algo.super import Super
from algo.kmp import KMP

class AC(Super):
    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        length = len(text)

        if sm_length == 0 or length == 0 or sm_length > length:
            return  # Невозможно найти подстроку

        # Префикс-функция для подстроки (KMP)
        kmp = KMP()
        pre = kmp.func_prefix(substring)

        # Вычисление ell — наименьший индекс, при котором символы перестают повторяться
        ell = 1
        while ell < sm_length and substring[ell - 1] == substring[ell]:
            ell += 1
        if ell == sm_length:
            ell = 0

        i = ell  # Индекс в подстроке
        j = k = 0  # Индексы в тексте и для проверки ell

        while j <= length - sm_length:
            # Поиск совпадений по подстроке
            while i < sm_length and substring[i] == text[i + j]:
                i += 1
            if i >= sm_length:
                # Проверяем совпадение для первых ell символов
                while k < ell and substring[k] == text[j + k]:
                    k += 1
                if k >= ell:
                    yield j  # Найдено полное совпадение

            # Защита от выхода за пределы массива pre и сдвиг j
            if i < sm_length:
                j += max(1, i - pre[i])  # Используем максимальный сдвиг для избежания зацикливания
            else:
                j += i  # Если i вышел за пределы подстроки, сдвигаем на i (или sm_length)

            # Пересчёт индексов для следующего прохода
            if i == ell:
                k = max(0, k - 1)
            else:
                if i < sm_length and pre[i] <= ell:
                    k = max(0, pre[i])
                    i = ell
                else:
                    k = ell
                    i = pre[i] if i < sm_length else ell