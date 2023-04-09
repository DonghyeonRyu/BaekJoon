#221
def print_reverse(string) :
    print(string[::-1])

#222
def print_score(score) :
    print(sum(score)/len(score))

#223
def print_even(num) :
    for i in num :
        if i %2 == 0:
            print(i)

print_even ([1, 3, 2, 10, 12, 11, 15])
print("\n")

#224
def print_keys(dic) :
    for i in dic.keys() :
        print(i)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})
print("\n")

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(list, day) :
    print(list[day])

print_value_by_key  (my_dict, "10/26")
print("\n")

#226
def print_5xn(string) :
    split = int(len(string)/5)
    for i in range(split + 1) :
        print(string[i*5:i*5+5])

print_5xn("아이엠어보이유알어걸")

#227
def print_mxn(string, num) :
    split = int(len(string)/num)
    for i in range(split+1) :
        print(string[i*num:i*num+num])

print_mxn("아이엠어보이유알어걸", 3)
print('\n')

#228
def calc_monthly_salary(annual_salary) :
    month_money = int(annual_salary/12)
    return print(month_money)

calc_monthly_salary(12000000)