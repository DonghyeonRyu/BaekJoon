#232
def make_url(string) :
    url = "www." + string + ".com"
    return url

make_url("naver")

#233
def make_list(string) :
    list = []
    for i in string :
        list.append(i)
    return list
make_list("abcd")

#234
def pickup_even(num_list) :
    num_odd = []
    for i in num_list :
        if i %2 == 0 :
            num_odd.append(i)
    return print(num_odd)

pickup_even([3, 4, 5, 6, 7, 8])
print('\n')

#235
def convert_int(num) :
    return print(int(num.replace(",","")))

convert_int("1,234,567")
print('\n')