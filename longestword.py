# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 04:38:45 2018
@author: souravg
To Do: Implement a function longestWord() that takes a list of words and returns the longest one.    
"""
def longestWords(low):
    wordlength={}
    longwords=[]  # Blank List is initialized to add longest words after loop iteration
    for word in low:
        wordlength[word]=len(word)
    maxlength = max(wordlength.values())
    for key,value in wordlength.items():
        if(value == maxlength):  # Comparing lengths of each word in the passed list with the word having the maximum length and if it equals then keep adding that word in the longwords list
            longwords.append(key)
    return longwords 
WordsList = ['Data','Science','Course','is','excellent','and','wonderful']
LongestWordsList = longestWords(WordsList)
print(LongestWordsList)  #Output :  ['excellent', 'wonderful'] because both having lengths equal to 9 which is the maximum length of the words found in the input list
