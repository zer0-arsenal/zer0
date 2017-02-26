
# coding:utf-8

#参加者の人数を入力
child = raw_input("How many participants?:")
child = int(child)

# 自分の順番を入力させる
order = raw_input("What number are you?:")
order = int(order)

# とりあえず、13回繰り返してみる
cards_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# 文字列判定用の変数
acca = ""

# 何巡目かを分かりやすくするため
line = 1


"""
while acca != "end":
    print(chaos)
    chaos = chaos + order
    if chaos > 13:
        chaos -= 13
    acca = raw_input("Repeat?:")
"""



while acca != "end":
    num = 0
    # ダウトでは13回、回ってくるまで出すカードが被ることは絶対内
    # なので、どのカードを何巡目に出すかの一覧を出すために"１３"回繰り返す?
    while num != 13:
        print line, ":", order
        order = order + child
        if order > 13:
            order -= 13
        num += 1
        line += 1

    acca = raw_input("Repeat?:")




