def LongestPalindrome(text):
    def e(l, r):
        while l >= 0 and r < len(text) and text[l] == text[r]:
            l -= 1
            r += 1
        return text[l + 1:r]
    
    result = ""
    for i in range(len(text)):
        sub1 = e(i, i)      # kent erkarutyamb palindrome
        if len(sub1) > len(result):
            result = sub1
        
        sub2 = e(i, i + 1)  # zuyg erkarutyamb palindrome
        if len(sub2) > len(result):
            result = sub2

    return result

t = "aababa"
R = LongestPalindrome(t)
print(R)
