# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:25:11 2019
Strings:
    Enclosed in '...' or "..." , \ used for escape Characters
    
@author: KheopS
"""

#'...' "..."
text = 'Simple text'
print(text)
text = "Simple Text"


text1 = 'dose\'t' #notice ' 'for strings and dosen't
#or we can use " "
text1 = "dosen't"
print(text1)

text2 = "A wise man said one time \"Think twice do once.\"" # notice \"
print(text2)

#use escape characters
line = "First Line.\nSecond Line."
print(line) #\n means newline

#FilePath Escape Characters
print("File is located in C:\some\name")
#O: C:\some
#ame

#A better version
print("File is located in C:\\some\\name")#\\ escape  character for \
print(r"File is located in C:\some\name") # r" " row string.

#Span Multiple lines
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(".................")

multi = """It was good times.
But bad times too.
"""
print(multi)
print(3 * "un" +"im")

#Strings are indexed
word = "Python"
print(word[0]+" "+ word[-1]) #first character
print(word[0]+" "+ word[-6]) 

#Slicing Strings
print(word[0:2]) # 0 included 2 excluded(0,1)
print(word[:])
print(word[:5])
print(word[1:4])
print(word[-6])
print(len(word)) # len() return the length of string

#String are immutable - cannot be changed.
##word[0] = 'J';
##print(word)

#If you need another string you should create it
anotherWord = 'J' + word[1:]
print(word) #Python
print(anotherWord) #Jython

#String Methods
test = " ThIs iS Just A simpLE TexT! "
#lower() -return lower version if string
print(test.lower())
testToLower = test.lower()
print(testToLower)
print()

#upper() - return upper version of string
print(test.upper())
testToUp = test.upper();
print(testToUp)
print()

#strip() - remove whitespace from the start and the end
print(test.strip())
testStrip = test.strip()
print(testStrip)

#isalfa() , isdigit(), isspace() alfa-literal digit-number space - blank
#Return bool
testAlfa = test.isalpha()
if testAlfa != True:
    print(test + "is not Alfa!")
else: "Is Alfa"

alfa = "Hi"
print("Alfa is: " + str(alfa.isalpha()))

#isspace
space = " ";
print("Space is: "+ str(space.isspace()))

#isdigit
digit = "5"
print("Digit is: "+ str(digit.isdigit()))

#startswith() endswith()
anotherText = "Find your love in Japan!"
print("anotherText start with \"Find\" ?: "+ str(anotherText.startswith("Find")))
print("anotherText ends with \"Japan!\" ?: "+ str(anotherText.endswith("Japan!")))

#find()
indexOfFind = anotherText.find("love")
print("Love is found at: ", indexOfFind)







