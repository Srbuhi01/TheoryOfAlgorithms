pattern = input("Input pattern: ")
text = input("Input text: ")

T = set()  # unikal symbol
patlen = len(pattern)  
table = {}  # Axyusak

# Axyusaki stexcum
for i in range(patlen - 2, -1, -1):  # naxavejinic sksac
    if pattern[i] not in T:
        table[pattern[i]] = patlen - i - 1
        T.add(pattern[i])

# verjin symboli hamar
if pattern[patlen - 1] not in T:
    table[pattern[patlen - 1]] = patlen

table['*'] = patlen

print("table:", table)

n = len(text)
found = False  # gtnvel e ardyoq patterny

if n >= patlen:
    i = patlen - 1

    while i < n:
        k = 0
        for j in range(patlen - 1, -1, -1):  # ajic dzax
            if text[i - k] != pattern[j]:
                if j == patlen - 1:
                    off = table[text[i]] if text[i] in table else table["*"]
                else:
                    off = table[pattern[j]]
                i += off
                break
            k += 1
        else:  
            print(f"Pattern is found, starting index: {i - k + 1}")
            found = True
            i += patlen  # hajord hnaravor arkayutyuny
else:
    print("Pattern is not found")

if not found:
    print("Pattern is not found")
