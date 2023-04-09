#215
def print_with_smile(string) :
    print(string + ":D")

#216
print_with_smile("안녕하세요")
print("\n")

#217
def print_upper_price(a) :
    print(a*1.3)

#218
def print_sum(a, b) :
    print(a+b)

#219
def print_arithmetic_operation(a, b) :
    print(a, "+", b, "=", a+b)
    print(a, "-" ,b, "=",a-b)
    print(a,"*", b ,"=", a*b)
    print(a, "/", b ,"=", a/b)

print_arithmetic_operation(3,4)
print("\n")

#220
def print_max(a, b, c) :
    if a > b :
        if a > c :
            print(a)
        else :
            print(c)
    elif b > c :
        print(b)
    else :
        print(c)

print_max(1, 2, 3)