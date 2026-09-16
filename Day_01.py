# this my frist day of cooding

#  For a given number n , print if it’s a multiple of 5 or not.

# while(True):
#     n = int(input("Enter your number : "))
#     if(n%5==0):
#         print(n,("is multiple of the 5"))
#     else:
#         print(n,("is not multiple of the 5"))
#         break    


#  For a given number n , print if it’s Odd or Even

# for i in range(5):
#     n = int(input("Enter your no. : "))
#     if(n%2==0):
#         print(n,"is even number")
#     else:
#         print(n,"is even number")    


# Print multiplication table for any number n . [using while ]

# n = int(input("Enter your number : "))
# i = 0

# while(i<=10):
#     print(n,"*",i,"=",n*i)
#     i+=1
#     if(n==0):
#         break

# Print odd numbers from 1 to 10, using continue. [using while]
# i = 0
# while(i<10):
#     i+=1
#     if(i%2==0):
#         continue
#     else:
#         print(i)


# Print odd numbers from 1 to 10, using continue. [using for]
# i = 1
# for i in range(1,11,2):
#     print(i)
#     i+=1


# Print even numbers from 1 to 10, using continue. [using for]
# n = int(input("Enter your number : "))
# i = 0
# for i in range(0,n+1,2):
#     if(n<=1):
#         break
#     else:
#         print(i)
#         i+=1
    


# Count vowels in a word. [using for]
# word = input("Enter your word : ")
# count = 0
# for ch in word:
#     if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#         count+=1
# print(count)  



#  Sum of first n natural numbers. [using for]
# n = int(input("Enter your number : "))
# sum = 0
# for i in range(n+1):
#     sum+=i
# print(sum)  


# Create a function to compute factorial of a number n
# def fact():
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# n = int(input("Enter your number : "))
# fact()       