import math

# 行数（日数）格納
days = int(input())

# 初期値設定
list = []


# 構文使用(i=0～4)
# 以下を５回回す意
for i in range(days):

    # 引数取込⇒リストに追加
    list.append(int(input()))


# for文で取得して生成したリストを合計(for文ごとに合計に加算していく方法もありそう)
Sum = sum(x for x in list)

# 平均算出
ave = math.floor(Sum / days)
print(ave)
