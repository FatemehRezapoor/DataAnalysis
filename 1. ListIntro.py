# July 2020
# Overview of the list commands

# 1. CREATE LIST
Mylist=['Sara','1','Dokme']
print(Mylist)

# 2. READ AN INDEX
print(Mylist[0])
print(Mylist[0:2])
print(Mylist[-1]) # read from the end

# 3.RE-ASSIGN AN INDEX
for i in range(3):
    Mylist[i]=Mylist[i] + 'Dokme'
print(Mylist)

# 4. ADD ELEMENT TO THE LIST
Mylist.append('Hi')
print(Mylist)

# 5. COMBINE TWO LISTS
Mylist2=[1,2,3]
#Method 1
Mylist.extend(Mylist2)
print(Mylist)
#Method 2
Mylist + Mylist2
print(Mylist)

# 6. INSERT ELEMENTS
Mylist.insert(0,'bye')
print(Mylist)
Mylist[0:2]=[0,1]
print(Mylist)

# 7. DELETE ELEMENTS BY INDEX
del Mylist[4]
print(Mylist)
del Mylist[-2:]
print(Mylist)

# 8. REMOVE ELEMENT BY NAME
Mylist.remove(1)
print(Mylist)

# 9. SORT ELEMENTS: LIST NEEDS TO BE INT OR STR
#Mylist.sort()
#print(Mylist)

# 10. CREATE A SUBLIST (SLICE)
Mylist=[0,1,2,3,4]
Mylist2=Mylist[:2]
print(Mylist2)

# 11. CREATE A SUBLIST FROM END
Mylist2=Mylist[-1]
print(Mylist2)
Mylist2=Mylist[-3:-1]
print(Mylist2)






