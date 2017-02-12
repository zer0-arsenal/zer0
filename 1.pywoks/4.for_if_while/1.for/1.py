
list_tohoku = [5349.0,5478.0,5344.0,4644.0,4968.0,6259.0]
list_shikoku = [3148.0,2991.0,2966.0,2457.0]
avg_tohoku = 0.0
avg_shikoku = 0.0

for val in list_tohoku:
    #print(val)
    avg_tohoku += val
    
avg_tohoku /= len(list_tohoku) # "avg_tohoku"にvalの中身を加える
print(avg_tohoku)

for val in list_shikoku:
    avg_shikoku += val

avg_shikoku /= len(list_shikoku)
print(avg_shikoku)


dict_tohoku = {"aomori":5349.0,"akita":4644.0,"sendai":5344.0,\
               "Yamagata":4968.0,"fukushima":6259.0,"morioka":5478.0}

for val in dict_tohoku:
    print(val)

