   

# def function(a):
#     previous = 0
#     for i in range(0, a):
#         current =  previous + i
#         previous = current 
#         print(f"Current number :{current}, Previous number : {previous}, sum of both : {current + previous}")

# a = int(input("Enter the Range: "))        
# function(a)


# a = input("Enter the String: ")
# l = len(a)
# for i in range(l - 1, -1, -1):
#     print(a[i], end = " ")

# def remove_chars(word, n):
#     print('Original string:', word)
#     # Extract string from index n to the end
#     res = word[n:]
#     return res

# print("Removing characters from a string")
# print(remove_chars("pynative", 1))
# print(remove_chars("pynative", 2))

# a = 5
# b = 10
# print(f"Before Swap: a = {a}, b = {b}")

# # Simultaneous assignment (Tuple Unpacking)
# a, b = b,a

# print(f"After Swap: a = {a}, b = {b}")

# a = int(input("Enter the number: "))
# b = 1
# for i in range(1, a+1):
#     b = i*b
# print(b)

# list = [1, 2, 3, 4, 5]
# list.append("anand")
# list.append(29)
# list.insert(2, "Second")
# print(list)
# list.pop(2)
# print(list)


# arr = 2,3,4,1,7,8,6,0,10
# listed = list(set(arr))
# listed.sort()
# print(listed[-2])

# import numpy as np
# n = np.array([[1,2,3],[4,5,6],[8,7,9]])
# print(n.ndim)
# print(n.shape)
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
add = a + b
sub = a - b 
mul = a * b
print(add)
print(sub)
print(mul)

