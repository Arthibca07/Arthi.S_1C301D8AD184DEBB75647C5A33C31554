#1.1 implment a recursive funtion to calculate the factorial of the given number

def fact_rect(n):
   if n==0 or n==1:
     return 1
   else:
     return n*fact_rect(n-1)
num=int(input("Enter the number : "))
res=fact_rect(num)
print("factorial of {} is {}".format(num,res))