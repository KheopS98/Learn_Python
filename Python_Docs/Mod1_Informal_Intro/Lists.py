# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:45:36 2019

@author: KheopS
"""
#Create a  list

square = [1,4,9,16,25,36]
print(square)

#Like strings can be indexed and sliced
print(square[1]) #indexed
print(square[2:]) #sliced
print(square[:]) #sliced

#Lists support concatenation +
square = square + [49,64,81,100]
print(square)

#Lists are Mutable(can be changed)
#Replace 24 with  25
square[4] = 24
print(square)
print("square[4] is: " + str(square[4]))

#Add items at the end of list -- append()
square.append(121)
print(square)

#Assign with slices
letters = ['a','b', 'c', 'd', 'e', 'f','g',]
print(letters)
letters[0:3] = ['A','B','C']
print(letters)

#Remove with slices
letters[3:6] = []
print(letters)

#Clearn all list
letters[:] = []
print(letters)

#len of the list
print(len(letters)) #0 for now cuz is empty



