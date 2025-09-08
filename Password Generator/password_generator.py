# PASSWORD GENERATOR :

import random
import os

file_path = r"G:\mini projects\passwords.txt"
while True:
 final = []

 Letters = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
 Numbers = '1','2','3','4','5','6','7','8','9','0'
 Symbols = '!','@','#','$','%','^','&','*','(',')','/','/','[',']','{','}','?'

 print("-------------------"
       "\nPASSWORD GENERATOR"
      "\n--------------------")
 user = int(input("ENTER THE LENGTH OF THE CHARACTER OF YOUR PASSWORD : "))
 letters = str(input("YOU WANT TO INCLUDE LETTERS (y/n) : ").lower())
 if letters == 'y':
  final += Letters


 numbers = str(input("DO YOU WANT TO INCLUDE NUMBERS (y/n) : ").lower())
 if numbers == 'y':
  final += Numbers
  


 symbols = str(input("DO YOU WANT TO INCLUDE SYMBOLS (y/n) : ").lower())
 if symbols == 'y':
  final += Symbols
  
 if not final:
   print("KINDLY PLEASE SELECT ANY ONE OF THE FOLLOWING...! ")
 else: 
    count = int(input("ENTER HOW MANY PASSWORDS DO YOU WANT : "))
    with open(file_path, "a") as file:
       for _ in range(count):
          password = ""
          for i in range(user):
             password += random.choice(final)
          print("password : ",password)
          file.write(password + '\n') 
    print("PASSWORD SAVED...!")
 

 user_in = str(input("DO YOU WANT TO ANOTHER PASSWORD GENERATION (y/n): ").lower())
 if user_in == 'n':
   print("------THANK YOU FOR USING MY PASSWORD GENERATOR------")
   break
   
   




