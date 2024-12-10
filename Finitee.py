def build_transition_table(pattern, alphabet):
    
    m = len(pattern)
    transition = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in alphabet:
            next_state = state
            while next_state > 0 and (next_state == m or pattern[next_state] != char):
                next_state -= 1
            if next_state < m and pattern[next_state] == char:
                next_state += 1
            transition[state][char] = next_state

    return transition

def finite_automaton_string_matching(text, pattern):
        
    alphabet = set(text)
    transition = build_transition_table(pattern, alphabet)

    state = 0
    matches = []

    for i, char in enumerate(text):
        # new state
        state = transition[state].get(char, 0)
        if state == len(pattern):
            # match index
            matches.append(i - len(pattern) + 1)

    return matches

text = "ababcabcabababd"
pattern = "ababd"
matches = finite_automaton_string_matching(text, pattern)
print("Matches found at positions:", matches)






















