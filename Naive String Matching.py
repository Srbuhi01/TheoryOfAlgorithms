InputString = input("String: ")
pattern = input("Pattern: ")

for inpstr in range(len(InputString) - len(pattern) + 1):
    for patt in range(len(pattern)):
        if pattern[patt] != InputString[inpstr + patt]:
            break
        if patt == len(pattern) - 1:
            print(f"Position is {inpstr}")
