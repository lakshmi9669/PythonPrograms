test_list = [1, 3, 5, 6, 3, 5, 6, 1,4,9]
print ("The original list is : " ,test_list)
res = []
res1 = []
for i in test_list:
   if i not in res:
      res.append(i)
   else:
      res1.append(i)
print ("The list after removing duplicates : " , res)
print("duplicates only: " ,res1)
# res1.sort()#sort method use
# print(res1)



# num = input("enter numbers")
# Number = num.split()
# duplicates = []
# noduplicates = []
# for i in Number:
#    if i not in duplicates:
#       duplicates.append(i)
#    else:
#       noduplicates.append(i)
# print ("The list after removing duplicates : " , duplicates)
# print("duplicates only: " ,noduplicates)




