num = int(input("Enter a number:"))  
sum = 0

pmet = num
while pmet > 0:
    tigid = pmet % 10
    sum += tigid ** 3
    pmet //= 10

if num == sum:
    print(num,"Is an Amrstrong Number")
else:
    print(num,"Is not an Armstrong Number")
