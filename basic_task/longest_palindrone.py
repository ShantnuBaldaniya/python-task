def longest_palindromic_subsequence(s):
    def lps(i, j):
        
        if i > j:
            return 0
        if i == j:
            return 1

        
        if s[i] == s[j]:
            return 2 + lps(i+1, j-1)
        else:
            return max(lps(i+1, j), lps(i, j-1))

    return lps(0, len(s)-1)
print(longest_palindromic_subsequence("bbbbabaabbab")) 
print(longest_palindromic_subsequence("cbbd"))