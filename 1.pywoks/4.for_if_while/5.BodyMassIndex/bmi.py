# coding:utf-8

while True:
    height = raw_input("身長(m)?:") #Python3.0系ではinput関数を使用
    if len(height) == 0:
        break #Enterキーを押されただけの場合はここで終了させる
    height = float(height) #入力は文字列なので、小数に変換
    weight = float(raw_input("体重(kg)?:"))
    bmi = weight / pow(height,2) #組み込み関数powで累乗を計算できる

    print("BMI値は%0.1fです。" %bmi) #小数点以下は第1位までの出力にフォーマットする
    if bmi < 18.5:
        print("少し痩せすぎ")
    elif 18.5 <= bmi < 25.0:
        print("標準的な体型")
    elif 25.0 <= bmi < 30.0:
        print("少し肥満")
    else:
        print("高度の肥満")



