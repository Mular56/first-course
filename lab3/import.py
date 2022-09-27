import csv 
import sys 
 
print("Гpyna 4") 
filename= "D:\students4.txt"  
text_file = open("D:\students4.txt", "r") 
reader=csv.reader(text_file, delimiter="\t") 
for str in reader:  
    print(str) 
text_file.close() 
 
 
print("Гpyna 5") 
filename= "D:\students5.txt"  
text_file=open("D:\students5.txt", "r") 
reader=csv.reader (text_file, delimiter="\t") 
 
for str in reader: 
    print (str)  
text_file.close() 
 
 
 
print("Група 6") 
filename = "D:\students6.txt"  
text_file=open("D:\students6.txt", "r") 
reader=csv.reader (text_file, delimiter="\t") 
 
for str in reader:  
    print(str) 
text_file.close()

input()