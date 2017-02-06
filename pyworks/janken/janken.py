import random
#randomモジュールのインポート.この機能でランダムな動きを行う機能を使えるようにしている
data = ['goo','choki','pa']
#データの準備."="をつけて"data"という名前をつけておく
data_choice = random.choice(data)
# 2行目で用意したリストから無作為に でーた1つ選んでいる
print(data_choice)
