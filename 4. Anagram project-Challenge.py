# July 2020
# OBJECCTIVE: 1. Given a list of words from a dictionary file, seperate words in to the class of words with the same length, 2. For each class find all anagrams 3. Count the total number of anagrams in each class
import timeit
import datetime
import time
import collections
# 1. OPEN THE FILE
word=open('words','r')
print(word)

# 2. READ THE LINES
wordlist=word.readlines()
print(len(wordlist[1]))
print(wordlist[1])

# 3. CLEAN THE DATA
wordclean=sorted(list(set((word.strip().lower() for word in wordlist))))

# 4. FIND THE MAX LENGTH
# Do not need in coding but to check the length of the key in dictionary it is a good idea to know the max length of a word
max_len= max(set(len(i) for i in wordclean))
print(max_len)

# 5. SAVE WORDS BASED ON LENGTH IN DICTIONARY
import collections
len_dic=collections.defaultdict(list)
for word in wordclean:
    len_dic[len(word)].append(word)

# NO NEED IN CODE: But to check the number of keys
print(len(len_dic))
#print(len_dic[1])

# 6. DEFINE SIGNITURE
def signature(word):
    return ''.join(sorted(word))
anagraml=[]
def anagram(word):
   return (w for w in len_dic[len(word)] if signature(w)==signature(word))
print(*(anagram('game')))
#print(anagraml)



# LEARN: We do not need \n at the end of each phrase

print('A\n'.strip())
#LEARN: We want the letters to be small case
print('A'.lower())

# NOW: DELETE \n + CHANGE TO LOWER CASE + ELIMINATE DUPLICATE WITH SET
wordclean=list(set((word.strip().lower() for word in wordlist)))
print(wordclean[:5])

# 5. NOW LET'S SORT THEM
wordsort = sorted(wordclean)
print((wordsort)[:5])
#print(wordunique)

# 6. LEARN: TO CHECK IF THE NUMBERS ARE ANAGRAM, THE SORTED OF THOSE VALUES ARE THE SAME.
print(sorted('salam') == sorted('malas'))
print(sorted('sara'))
# TO PRINT ALL VALUES TOGETHER

def signature(word):
    return ''.join(sorted(word))
print(signature('topoli'))

# 7. NOW LET'S LOOK FOR ANAGRAM IN WORDCLEAN
def anagram(word):
    return (w for w in wordsort if signature(w)==signature(word))
t = time.process_time()
print(*(anagram('game')))
elapsed_time = time.process_time() - t
# 8. CHECK HOW LONG THE PROCESS TAKES
print(elapsed_time)

# 9. HOW TO SAVE TIME: Create and Save results in dictionary

word_dic=collections.defaultdict(list)

""" 
LEARN: COLLECTION EXAMPLE: ***
Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc. These are built-in collections. The defaultdict works exactly like a python dictionary, except for it does not throw KeyError when you try to access a non-existent key. Instead, it initializes the key with the element of the data type that you pass as an argument at the creation of defaultdict. The data type is called default_factory.
EX: 
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())
# OUTPUT: [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function which returns an empty list. The list.append() operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list. 
"""

# In place of using a for loop for each user input, we create a dictionary for ONCE and use for the comparison
for word in wordsort:
    word_dic[signature(word)].append(word)
print((word_dic))
# Now for each user input, it only looks for the index in the word_dic and will not go through aa for loop
def anagram_fast(word):
    return word_dic[signature(word)]
t = time.process_time()
print(anagram_fast('game'))
elapsed_time = time.process_time() - t
print(elapsed_time)


