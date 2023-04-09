#181
apart =[["101호", "102호"], ["201호","202호"],["301호","302호"]]
print(apart)
print("\n")

#182
stock = [["시가",100,200,300],["종가", 80,210,330]]
print(stock)
print("\n")

#183
stock = {'시가':[100,200,300], '종가':[80,210,330]}
print(stock)
print("\n")

#184
stock = {'10/10':[80,110,70,90], '10/11':[210,230,190,200]}
print(stock)
print("\n")

#185 
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart :
    for j in i :
        print(j, "호")
print("\n")

#186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1] :
    for j in i :
        print(j, "호")
print("\n")

#187
for i in apart[::-1] :
    for j in i[::-1] :
        print(j,"호")
print("\n")

#188
for i in apart :
    for j in i :
        print(j, "호")
        print("-----")
print("\n")

#189
for i in apart :
    for j in i :
        print(j, "호")
    print("-----")
print("\n")

#190
for i in apart :
    for j in i :
        print(j, "호")
print('-----')
