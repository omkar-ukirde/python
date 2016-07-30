#!/usr/python

my_dict = {}
word = raw_input('Enter the word : ')
print('You entered ' + word)
meaning = raw_input('Enter the meaning of ' + word + ' : ')
print(word + ' : ' + meaning)
my_dict[word] = meaning
print(my_dict)

