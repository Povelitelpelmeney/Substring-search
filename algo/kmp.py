from algo.super import Super


class KMP(Super):
    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        length = len(text)
        pre = KMP.make_pre(substring, text)
        k1 = 0
        i1 = 0
        while i1 < length - 1:
            if substring[k1] == text[i1]:
                k1 += 1
                i1 += 1
                if k1 == sm_length:
                    yield i1 - sm_length
                    k1 = pre[k1 - 1]
            elif k1 > 0:
                k1 = pre[k1 - 1]
            else:
                i1 += 1

    @staticmethod
    def make_pre(substring, text):
        sm_length = len(substring)
        paragraph = substring + "#" + text
        pre = []
        pre.append(0)
        k = 0
        for i in range(1, sm_length + 1):
            while k > 0 and paragraph[k] != paragraph[i]:
                k = pre[k - 1]
            if paragraph[k] == paragraph[i]:
                k += 1
            pre.append(k)
        return pre
