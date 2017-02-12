import datetime

today = datetaime.datetime.now()
print(today)
print(today.weekday())
''' weekday()
曜日がわかる
0:月曜、1:火曜、2:水曜、3:木曜、4:金曜、5:土曜、6:日曜
'''
if today.weekday() < 5:
    print("頑張ろう") #条件式がTrueだった時の処理
elif today.weekday() == 4:
    print("ゆっくりやろう")
else:
    print("休日だ〜〜") #条件式がFalseだった時の処理
