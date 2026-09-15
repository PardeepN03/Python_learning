# q1
# salary = int(input("Enter your Salary : "))
# if(salary<30000):
#     tax = 5
# elif(salary==30000 or salary<=70000):
#     tax = 15    
# else:
#     tax = 25

# tax_calc = salary * tax/100
# print(tax_calc)  


# q2 
# def even_no(a,b):
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)
    

# a = int(input("Enter your no. : "))
# b = int(input("Enter your no. : ")) 
# even_no(a,b) 


# q3
# def digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10


# n = int(input("Enter a number: "))
# digits(n)



# q10
# Number Guessing Game
# def guess_num():
#     secret_num = 9
#     guess = int(input("Enter your number : "))
#     for i in range(1):
       
#        if(guess>secret_num):
#             print("Too High")
#        elif(guess<secret_num):
#             print("Too Low")
#        else:
#             print("Correct")
#             break
    
# guess_num()



# q9
# def is_Prime():
#     if(n<=1):
#         return False
#     for i in range(2 , n):
#         if(n%i==0):
#             return False
#     return True

# n = int(input("Enter your number : ")) 
# print(is_Prime())



# q8
# def calculator(a,b,operations):
#     match operations:
#         case ("+"):
#             return (a+b)
#         case ("-"):
#             return (a-b)
#         case ("*"):
#             return (a*b)
#         case ("/"):
#             return (a/b)

# a = int(input("Enter your num. a : "))
# b = int(input("Enter your num. b : "))
# operations = input("Enter your operation")
# ans = calculator(a,b,operations)
# print(ans) 


# q6
# def divisible():
#     for i in range(1, 100):
#         if(i%3==0 and i%5==0):
#             print(i)

# divisible() 


# q6
# def num():
#     while(True):
#         n = (input("Enter your no. or quit : "))
#         if(n=="quit"):
#             break
#         n = int(n)
#         if(n<0):
#             print("The no. is negative")
#         elif(n>0):
#             print("The no. is positive")    
#         else:
#             print("The no. is zero") 


# num()

# practice

def is_prime():
