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


s = "ABABDBH"
rev_s = s[::-1]
result = lcs(s, rev_s, len(s), len(rev_s))
print("Longest Palindromic Subsequence:", result)
print("Length:", len(result))
