def bubble_sort(cucak):
    people = list(cucak.items())
    n = len(people)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if int(people[j][1]) > int(people[j+1][1]):
                people[j], people[j+1] = people[j+1], people[j]
                swapped = True
        if not swapped:
            break
    
    for person in people:
        print(person[0])

cucak = {"Anna": "34", "Samvel": "13", "Vahe": "20", "Nune": "10"}
bubble_sort(cucak)
