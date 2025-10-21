def multiplication_table_while(number):
    i = 0
    while i <=12:
        print(f"{number} x {i} = {number * i}")
        i +=1

  
#input
num = int(input("Enter Number Here:"))
multiplication_table_while(num)