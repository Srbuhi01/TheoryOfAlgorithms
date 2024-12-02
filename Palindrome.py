def solution(inputStr):
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
            odd_chars.append(char)
    
    if odd_count > 1:
        for char in odd_chars:
            if odd_count <= 1:
                break
            char_counts[char] -= 1
            odd_count -= 1
    
    half_palindrome = []
    middle_char = ""
    
    for char, count in char_counts.items():
        if count % 2 != 0:
            middle_char = char
        half_palindrome.append(char * (count // 2))
    
    half_palindrome = ''.join(half_palindrome)
    palindrome = half_palindrome + middle_char + half_palindrome[::-1]
    
    return palindrome

print(solution("ցbb"))
print(solution("aavvvvcc"))
print(solution("aabb"))
