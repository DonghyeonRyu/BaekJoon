#171
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])
print("\n")

#172
price_list = [32100, 32150, 32000, 32500]
for i in range(4) :
    print(i, " ", price_list[i])
print("\n")

#173
for i in range(len(price_list)) :
    print(3-i, price_list[i])
print("\n")

#174
for i in range(1,4) :
    print(90+i*10, price_list[i])
print("\n")

#175
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1) :
    print(my_list[i],my_list[i+1])
print("\n")

#176
my_list = ["가", "나", "다", "라", "마"]
for i in range(3) :
    print(my_list[i], my_list[i+1], my_list[i+2])
print("\n")

#177
my_list = ["가", "나", "다", "라"]
for i in range(3,0,-1) :
    print(my_list[i], my_list[i-1])
print("\n")

#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1) :
    print(int(my_list[i+1])-int(my_list[i]))
print("\n")

#179
my_list = [100, 200, 400, 800, 1000, 1300]
sum = 0
avg = 0
for i in range(len(my_list)-2) :
    sum = my_list[i]+my_list[i+1]+my_list[i+2]
    avg = sum / 3
    print(avg)
print("\n")

#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in range(len(low_prices)) :
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)