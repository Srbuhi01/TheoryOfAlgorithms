def StrCanBePalindromic(Str):
    char_counts = {}
    for char in inputStr:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    odd_count = 0
    odd_chars = []
    for char, count in char_counts.items():
        if count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
      p = "String can be palindromic"
    else:
      p = "String can not be palindromic"   
    return p

print(StrCanBePalindromic("aAAddddavava"))
