def last_occurrence(pattern):
    #the last occurrence dictionary
    last = {}
    for i in range(len(pattern)):
        last[pattern[i]] = i
    return last

def Boyer_Moore(text, pattern):
    m = len(pattern)
    n = len(text)
    last = last_occurrence(pattern)  
    i = 0    # Starting index for text

    while i <= n - m: 
        j = m - 1  # Start from the end of the pattern

        # Move backwards in pattern as long as characters match
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # If `j` becomes -1,  match is found
        if j == -1:
            return f"Found at index {i}"

        # `last.get(text[i + j], -1)` gives -1 if character is not in `pattern`
        else:
            i += max(1, j - last.get(text[i + j], -1))

    return "Pattern not found"

text = "trusthardtoothbrushes"
pattern = "tooth"
print(Boyer_Moore(text, pattern))
