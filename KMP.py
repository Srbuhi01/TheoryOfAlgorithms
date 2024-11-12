def large_pref_suf(pattern):
    lps = [0] * len(pattern) 
    length = 0  
    i = 1  
    while i < len(pattern):
        if pattern[i] == pattern[length]:  
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP(pattern, text):
    F = large_pref_suf(pattern)   # LPS array 
    n = len(text)
    m = len(pattern)
    i = j = 0                           # Pointers 

    while i < n:
        if text[i] == pattern[j]:   # When  match
            if j == m - 1:  
                return i - j           #  start index of the pattern in the text
            i += 1
            j += 1
        elif j > 0:
            j = F[j - 1]  
        else:
            i += 1                    #  next character in text

    return f"Pattern not found "                      

pattern = input("Input pattern -> ")
text = input("Input text -> ")
result = KMP(pattern, text)
print(result)
