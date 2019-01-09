'''
Input a string which contain a list(between the bracket) and a long string. 
To check whether the long string was consist by the words in the list.
For instance:
Input = '[I love byte bytedance] Ilovebytedance'
The list is '[I love byte bytedance]'. The long string is Ilovebytedance
Output is True
'''

import sys
import re

str_input = '[I love byte bytedance] Ilovebytedance'#sys.stdin.readline().strip()

p1 = re.compile(r'[[](.*?)[]]', re.S) # Mode of getting the string between []
words_list = re.findall(p1, str_input) # workds_list is list which contain only one string 
wl_len = len(words_list[0]) # length of 'I love byte bytedance'

words_list = words_list[0].split(" ") #Split the string to word list. 'I love byte bytedance' -> ['I', 'love', 'byte', 'bytedance']
list_len = len(words_list) # Numbers of words in the list

l_str = str_input[wl_len+3:] # The start position of the long string. Because the list contain '[',']' and a space.
long_str = l_str

myList1 = sorted(words_list,key = lambda i:len(i),reverse=True)  # Sort the words list by length of each word. It will handle the 'byte' and 'bytedance' issue


def check_words(words_list, long_str):
    for i in range((list_len)):
        #print("***")
        #print(long_str)
        word = words_list[i]
        #print(word)
        while True:   
            find = long_str.find(word)
            print(find)
            if find >= 0:
                long_str = long_str[0:find] + long_str[find+len(word):]#find the word in long string, and remove it.
            else:
                break
                
    print(long_str)
    if len(long_str) > 0:
        # If there still be words, that means there are string which is long string but not in the list
        return False
    else:
        return True

check_words(myList1, long_str)
