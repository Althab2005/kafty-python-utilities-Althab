# UNIT CONVERTOR PROJECT : 

def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9
  
def kg_to_pounds(kg):
  return kg * 2.20462

def pounds_to_kg(pounds):
  return pounds / 2.20462
  
def km_to_miles(km):
  return km * 0.621371
  
def miles_to_km(miles):
  return miles / 0.621371
  
  
while True:  
 from colorama import Fore,Style,init
 init(autoreset=True)
 print(Fore.MAGENTA + "------------------------------"
      "\n      UNIT CONVERTOR"
      "\n------------------------------"
      "\n1 . TEMPERATURE"
      "\n2 . WEIGHT "
      "\n3 . DISTANCE"
      "\n------------------------------")

 user = int(input("\n\nCHOOSE THE CONVERSION YOU WANT : "))
 if user == 1:
  print(Fore.BLUE + "\n\na . celsius --> fahrenheit"
        "\nb . fahrenheit --> celsius".upper())
  option1 = input("\nENTER THE OPTIONS YOU WANT : ")
  option1 = option1.upper()
  if option1 == 'A':
    try:
     celsius = float(input("\nENTER THE VALUE IN CELSIUS : "))
     print(Fore.CYAN+str(celsius_to_fahrenheit(celsius))+" °F")
    except ValueError:
      print(Fore.RED + '\n\nPLEASE ENTER THE VALUES IN NUMBERS....')
  elif option1 == 'B':
    try:
     fahrenheit = float(input("\nenter the value in fahrenheit : ".upper()))
     print(Fore.CYAN+str(fahrenheit_to_celsius(fahrenheit))+' °C')
    except ValueError:
      print(Fore.RED + '\nPLEASE ENTER THE VALUES IN NUMBERS....')
  else:
    print(Fore.YELLOW + "\nPLEASE SELECT THE FOLLOWING OPTIONS....!")
  
 elif user == 2:
  print(Fore.BLUE +"a . kg --> pounds"
        "\nb . pounds --> kg".upper())
  option2 = input("\n\nenter the options you want : ".upper())
  option2 = option2.upper()
  if option2 == "A":
    try:
     kg = float(input("\nENTER THE VALUES IN KG : "))
     print(Fore.CYAN+str(kg_to_pounds(kg))+' LB')
    except ValueError:
      print(Fore.RED + '\nPLEASE ENTER THE VALUES IN NUMBERS....')
  elif option2 == 'B':
    try:
     pounds = float(input("\nENTER THE VALUES IN POUNDS : "))
     print(Fore.CYAN+str(pounds_to_kg(pounds))+' KG')
    except ValueError:
      print(Fore.RED + '\nPLEASE ENTER THE VALUES IN NUMBERS....')
  else:
    print(Fore.YELLOW + "\nPLEASE SELECT THE FOLLOWING OPTIONS....!")
  
 elif user == 3:
  print(Fore.BLUE +"a . km --> miles"
        "\nb . miles --> km".upper())
  option3 = input("\n\nENTER THE OPTIONS YOU WANT : ".lower())
  option3 = option3.upper()
  if option3 == "A":
    try:
     km = float(input("\nENTER THE VALUE IN KM : "))
     print(Fore.CYAN+str(km_to_miles(km))+' MILES')
    except ValueError:
      print(Fore.RED + '\nPLEASE ENTER THE VALUES IN NUMBERS....')
  elif option3 == 'B':
    try:
     miles = float(input("\nENTER THE VALUES IN MILES : "))
     print(Fore.CYAN+str(miles_to_km(miles))+' KM')
    except ValueError:
      print(Fore.RED + '\nPLEASE ENTER THE VALUES IN NUMBERS....')
  else:
    print(Fore.YELLOW + "\nPLEASE SELECT THE FOLLOWING OPTIONS....!")
  
 else:
  print(Fore.YELLOW + "\nPLEASE SELECT ANY ONE OF THE FOLLOWING....!")
  
 user_interest = input("\n\nDO YOU WANT ANOTHER CONVERSION (Y/N) : ")
 user_interest =  user_interest.upper()
 if user_interest == "N" :
  print(Fore.GREEN + "\n\n------THANK YOU FOR USING MY UNIT CONVERTOR------") 
  break