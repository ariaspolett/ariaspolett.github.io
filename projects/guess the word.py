lists = ["money", "family", "hate", "marker", "crayon", "gamble", "creativity", "scrambles", "teacher", "write", "eat"]

number = int(input("enter a number between 0-10: "))

tether = list(lists[number])
print(tether)

turns = 12
correct = []

while turns > 0:
    turns -= 1
    myletter = input("enter a letter")
    for x in tether:
        for y in my_letter:
            if x == y:
                correct.append(y)
            else:
                print("-")
print(correct)