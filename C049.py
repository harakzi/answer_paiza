"""
もっと簡略化したバージョン
"""


# 行数格納
input_line = int(input())

# 初期値設定
first_num = 1
input_num_list = []
Answer_list = []

# input_line=3のとき⇒0,1,2
# まず i=0 のとき
for i in range(input_line):

    # もしi=0だった場合⇒初期値から引く必要がある
    if i == 0:
        # list = [3]
        input_num_list.append(int(input()))

        # Answer_listに2が格納される
        Answer_list.append(abs(input_num_list[i] - first_num))  # ここで一旦for部分に戻る(Answer_list＝2のまま)
        # Answer_list = [2]

    # i = 1以降 input_num_list = [3], Answer_list = [2] が格納中
    else:
        # 次の引数として1がinputされる(i=1)
        input_num_list.append(int(input()))  # list = [3,1]  i = 1
        # A_list = [2, 2]
        Answer_list.append(abs(input_num_list[i] - input_num_list[i-1]))


Answer = sum(x for x in Answer_list)

print(Answer)


