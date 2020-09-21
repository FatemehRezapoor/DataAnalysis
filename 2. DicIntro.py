# July 2020
# Overview of the Dic commands

# 1. CREATE DIC
MyDic={'one':'1','Two':'do'} # key : Value
print(MyDic)

# 2. READ A VALUE
print(MyDic['one'])

# 3. CHECK IF KEY EXISTS
print('Three' in MyDic)
print('Two' in MyDic)

# 4. ADD ELEMENT TO THE DIC
MyDic.update({'Three':3})
print(MyDic)

# 5. DELETE ELEMENTS BY INDEX
del MyDic['Two']
print(MyDic)

# 6. LOOPS IN DIC
for keys in MyDic:
    print(keys)

for value in MyDic.values():
    print(value)

for key,value in MyDic.items():
    print(key,value)




