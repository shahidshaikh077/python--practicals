list = ['shahid',"gururaj","azar","yash"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

list[1]="a"
print(list)

list[2]="b"
print(list)

list[3]="c"
print(list)

list.append("harsh")
print(list)

list.insert(3,6)
print(list)

list.extend([66,83,79,35])
print(list)

list.remove(66) #remove element"66"
print(list)

list.pop(0) #remove index element 
print(list)

del list[3] #remove element in list
print(list)

len(list) #show total elements in list
print(len(list))



if 83 in list: #to check element in present or not present in list
    
    print("element is present") 

else:
    print("element is not present") 


for i in list: #list travers
    print(i)

print(list.count("a")) #counting

print(list.index("a"))#index finding


list1=[2,22,21,45,43.45,89,] 
list1.sort()
print(list1)



list1.sort(reverse=True)
print(list1)

list1.sort()
print(list1)



list1.reverse() 
print(list1)

newlist=list1.copy() #copy old list in new list

list.clear() #list clear
print(list)

    
print("------------------------------------------------------------------------------------")



student=[["english",80],["marathi",89],["science",79],["hindi",79]]

for i in student:
    print(i[0],i[1])

