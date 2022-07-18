# PALINDROME numbr or not USING RECURSION programs:
# number = input("enter number")
# rev=reversed(number)
# if list(number)==list(rev):
#    print('It is  a palindrome')
# else:
#     print('It is not a palindrome')



# word = input("Enter any word :")
# rev = reversed(word)
# if list(word) == list(rev):
#     print('It is a palindrome')
# else:
#     print('It is not a palindrome')



#Polindrome or not using SLICING
# n = input("Enter the word")
# if n == n[::-1]:
#     print("This word is palindrome")
# else:
#     print("This word is not palindrome")


#FACTORIAL OF NMBER USING RECCURSION
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result=fact(int(input("enter values")))
# print(result)




# USING FOR LOOP
# n=int(input("enter values"))
# result=1
# for i in range(n,0,-1):
#     result=result*i
# print(result)

#FIBONACCI SERIES
#using for loop
# a=0
# b=1
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c)
#
#using RECCURSION
# def a (i):
#     if i==0:
#         return 0
#     elif i==1:
#         return 1
#     else:
#         return a(i-2)+a(i-1)
# for x in range(20):
#   print(a(x))


# PRIME NMBR OR NOT
# number=int(input("enter values:"))
# for i in range(2,number):
#     if (number%i)==0:
#       print(number,"is not a prime number")
#       break
#     else:
#       print(number,"is a prime number")


#GIVEN RANGE:
# num = 72
# for i in range(2, num):
#      if (num%i)==0:
#         print(num, "is not a prime number")
#         break
#      else:
#         print(num, "is a prime number")
#         break


def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
fact=factorial(5)
print(fact)




