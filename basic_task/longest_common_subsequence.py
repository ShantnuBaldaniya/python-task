def lcs(s1, s2, m, n):

    if m == 0 or n == 0:
        return ''
    if s1[m-1] == s2[n-1]:
        return lcs(s1, s2, m-1, n-1) + s1[m-1]
    else:
        a = lcs(s1, s2, m-1, n)
        b = lcs(s1, s2, m, n-1)
        if len(a) > len(b):
            return a
        else:
            return b
s1 = "ABCDGH"
s2 = "AEDFHR"
result = lcs(s1, s2, len(s1), len(s2))
print(result)

