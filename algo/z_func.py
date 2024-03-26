from algo.super import Super


class Z(Super):

    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        paragraph = substring + "#" + text
        paragraph_l = len(paragraph)
        z_arr = [0] * paragraph_l
        left = 0
        right = 0
        for j in range(paragraph_l):
            z_arr[j] = 0

        for j in range(1, paragraph_l):
            if j <= right:
                z_arr[j] = min(right - j + 1, z_arr[j - left])
            while j + z_arr[j] < paragraph_l \
                    and paragraph[z_arr[j]] == paragraph[j + z_arr[j]]:
                z_arr[j] += 1

            if j + z_arr[j] - 1 > right:
                left = j
                right = j + z_arr[j] - 1

            if z_arr[j] == sm_length:
                yield j - sm_length - 1
