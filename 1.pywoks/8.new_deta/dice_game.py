#coding:utf-8

import dice

# "input"で値と受け取る
num = input("4, 6, 8, 12, 20のどれで勝負しますか？: ")
my_dice = dice.Dice(num) # ユーザ用のサイコロ
cpu_dice = dice.Dice(num) #CPU用のサイコロ

my_pip = my_dice.shoot() #pipはサイコロに目の意味
cpu_pip = cpu_dice.shoot() #CPUの出た目

#出目を画面に出力 数字はstr関数を使って文字列に変更
print("CPU : " + str(cpu_pip) + " YOU : " + str(my_pip))

#状況によってメッセージを変える
if my_pip > cpu_pip:
    print("congratirations!")
    print("You Win!!")

elif my_pip < cpu_pip:
    print("You lose...")

else:
    print("Drow.")

