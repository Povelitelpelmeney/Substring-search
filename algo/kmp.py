from algo.super import Super


class KMP(Super):
    @staticmethod
    def find(text: str, substring: str):
        substring_len = len(substring)
        text_len = len(text)
        if not text_len or substring_len > text_len:
            return []
        pre = func_prefix(substring)
        i = 0
        j = 0
        while i < text_len:
            if text[i] == substring[j]:
                if j == substring_len - 1:
                    yield i - substring_len + 1
                    j = pre[j]
                else:
                    j += 1
                i += 1
            elif j:     
                j = pre[j-1]
            else:
                i += 1

    @staticmethod
    def func_prefix(string: str) -> list:
        length = len(string)
        pre = [0]*length
        i = 0
        j = 1
        while j < length :
            if string[i] == string[j]:
                pre[j] = i + 1
                i += 1
                j += 1
            elif i:        
                i = pre[i - 1]
            else:          
                pre[j] = 0
                j += 1
        return pre
