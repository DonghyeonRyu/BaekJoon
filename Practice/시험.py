#Q1
list = "a:b:c:d"
list_split = list.split(":")
list_join = "#".join(list_split)
print(list_join)
print('\n')

#Q2
a = {'A':90, 'B':80}
print(a.get('C', 70))
print('\n')

#Q3
a = [1,2,3]

#Q4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A :
    if i >= 50 :
        sum = sum + i
print(sum)
print('\n')

#Q5
def Fib(num) :
    if num == 0 :
        return 0
    if num == 1 :
        return 1
    return Fib(num-2) + Fib(num-1)

print(Fib(10))
print('\n')

#Q6
def Sum(*args) :
    result = 0
    for i in args :
        result = result + i
    return print(result)

Sum(65,45,2,3,45,8)
print('\n')

#Q7
def cross() :
    num = input("구구단을 출력할 숫자를 입력하세요 : ")
    for i in range(1,10) :
        print(i * int(num), end=' ')
    
cross()
print('\n')

#Q8
f=open("C:/Python/abc.txt",'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open("C:/Python/abc.txt", 'w')
for line in lines :
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()
