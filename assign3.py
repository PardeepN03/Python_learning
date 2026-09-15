# q1
# p = input("Enter your number or word : ")
# if(p==p[: : -1]):
#     print("The word or number is palindrome")
# else:
#     print("The word or number is palindrome")



# q2 
# list = [1,2,3,4,5]
# total=0
# for i in list:
#     total+=i
# average = total/len(list)
# print(average) 



# q3 
# list1 = [1,2,7]
# list1.insert(3,57)
# list2 = [3,4,5]
# # result = [1,2,3,57,5,7]
# result = list1 + list2
# result.sort()

# print(result)


# q4
# (A) to print all even num
# t = (1,2,3,4,5,6,7,8)
# for i in t:
#     if(i%2==0):
#         print(i)

# (B) to print all even num        
# t = (1,2,3,4,5,6,7,8)
# for i in t:
#     if(i%2!=0):
#         print(i) 




# q4
# students = {}

# while True:
#     print("A. Add a student")
#     print("B. Update marks")
#     print("C. Search for a student")
#     print("D. Display all students and marks")
#     print("E. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "A":
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students[name] = marks

#     elif choice == "B":
#         name = input("Enter student name: ")
#         marks = int(input("Enter new marks: "))
#         students[name] = marks

#     elif choice == "C":
#         name = input("Enter student name: ")

#         if name in students:
#             print("Marks =", students[name])
#         else:
#             print("Student not found")

#     elif choice == "D":
#         print(students)

#     elif choice == "E":
#         break

#     else:
#         print("Invalid choice")



# q6
# words =["apple","banana","kiwi","cherry","mango"]
# # {"apple": 5, "banana": 6, "kiwi": 4, ...}
# word_length = {}
# for word in words:
#     word_length[word] = len(word)
#     print(len(word))    


# q7
# word = input("Enter your word : ")
# count = 0
# for i in word:
#     if i == " ":
#         count+=1
# print(count)    


# q8
# list1 =[1,2,3,4] 
# list2 =[5,6,7,8]
# s1 = set(list1)
# s2 = set(list2)
# common = s1.union(s2)
# print(common)