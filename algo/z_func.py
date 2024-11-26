from algo.super import Super

class Z(Super):

    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        paragraph = substring + "#" + text
        paragraph_l = len(paragraph)
        
        # Инициализация массива Z
        z_arr = [0] * paragraph_l
        left = 0
        right = 0

        # Вычисление Z-функции
        for j in range(1, paragraph_l):
            if j <= right:
                z_arr[j] = min(right - j + 1, z_arr[j - left])
            
            # Попытка расширить Z-блок
            while j + z_arr[j] < paragraph_l and paragraph[z_arr[j]] == paragraph[j + z_arr[j]]:
                z_arr[j] += 1

            # Обновление границ текущего Z-блока
            if j + z_arr[j] - 1 > right:
                left = j
                right = j + z_arr[j] - 1

            # Если длина совпадения равна длине подстроки, это совпадение
            if z_arr[j] == sm_length:
                yield j - sm_length  # Исправлено: возвращаем j - sm_length