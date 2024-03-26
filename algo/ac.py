from algo.super import Super
from algo.kmp import KMP


class AC(Super):

    @staticmethod
    def find(substring, text):
        sm_length = len(substring)
        length = len(text)
        kmp = KMP()
        pre = kmp.make_pre(substring, text)
        ell = 1
        while substring[ell - 1] == substring[ell]:
            ell += 1
            if ell == sm_length:
                ell = 0

        i = ell
        j = k = 0
        while j <= length - sm_length:
            while i < sm_length and substring[i] == text[i + j]:
                i += 1
            if i >= sm_length:
                while k < ell and substring[k] == text[j + k]:
                    k += 1
                if k >= ell:
                    yield j
            j += (i - pre[i])
            if i == ell:
                k = max(0, k - 1)
            else:
                if pre[i] <= ell:
                    k = max(0, pre[i])
                    i = ell
                else:
                    k = ell
                    i = pre[i]
