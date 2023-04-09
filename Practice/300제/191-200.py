#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data :
    for j in i :
        print(j*1.00014)
print("\n")

#192
for i in data :
    for j in i :
        print(j*1.00014)
    print('-'*4)
print("\n")

#193
result = []
for i in data :
    for j in i :
        result.append(j*1.00014)
print(result)
print("\n")

#194
result = []
for i in data :
    sub = []
    for j in i :
        sub.append(j*1.00014)
    result.append(sub)
print(result)
print("\n")

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:] :
    print(i[3])
print("\n")

#196
for i in ohlc[1:] :
    if i[3] > 150 :
        print(i[3])
print("\n")

#197
for i in ohlc[1:] :
    if i[3] >= i[0] :
        print(i[3])
print("\n")

#198
volatility = []
for i in ohlc[1:] :
    volatility.append(abs(i[2]-i[1]))
print(volatility)
print("\n")

#199
for i in ohlc[1:] :
    if i[3] > i[0] :
        print(abs(i[2]-i[1]))
print("\n")

#200
sum = 0
for i in ohlc[1:] :
    sum = sum + i[3]-i[0]
print(sum)