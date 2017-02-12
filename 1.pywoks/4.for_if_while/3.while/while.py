import rnadom

rand_num = 0

#パターン1
while rand_num != 4:
    rand_num = random.randint(0,9)
    print(rand_num)

#パターン2
while True:
    rand_num = random.randint(0,9)
    print(rand_num)
    if rand_num != 4:
        continue
    else:
        break






