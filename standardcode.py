# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 01:46:13 2022

@author: 65947
"""
meat = {'beef':27}
vegetables = {'beansprout': 0.2}
fruits = {'apple': 0.11}
others = {'cane sugar': 3}
user_input = {}
user_emission = {}

#message 1
welcome_msg=print('\nWelcome to Group 4’s App! \nThis is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes to your diet :)')
print()
print('='*50)

#message 2
def main_menu():
    while True:
        choice = input("To view which ingredients you can input, type 'menu'\nIf you are ready to start entering your ingredients instead, type 'start': ").lower()
        if choice == 'menu':
            print()
            print('='*50)
            menu_input()
            break
        
        if choice == 'start':
            print()
            print('='*50)
            carbon_calculator()
            break
        
        if choice not in ('menu','start'):
            print()
            print('='*50)
            print ('Please input either menu or start')
            continue
    
def menu_input():
    while True:
            print("\nMeat\nVegtables\nFruits\nOthers")
            print()
            choice=input("Which ingredient would you like to see? 1 for meat, 2 for vegetables, 3 for fruits and 4 for others? ")
            
            if choice==("1"):
                print()
                print('='*50)
                print ('You can input:')
                print ()
                for each in meat:
                    print (f'{each}')
                permission()
                break
                
            elif choice==("2"):
                print()
                print('='*50)
                print ('You can input:')
                print ()
                for each in vegetables:
                    print (f'{each}')
                permission()
                break
                
            elif choice==("3"):
                print()
                print('='*50)
                print ('You can input:')
                print ()
                for each in fruits:
                    print (f'{each}')
                permission()
                break
                
            elif choice==("4"):
                print()
                print('='*50)
                print ('You can input:')
                print ()
                for each in others:
                    print (f'{each}')
                permission()
                break
                
            else:
                print()
                print('='*50)
                print ('Please input 1 for meat, 2 for vegetables, 3 for fruits and 4 for other ingredients!')
                continue
       
def permission(): # so that user can either continue browsing (1), go straight to carbon calculator (2), or go to main menu (3)
        while True:
            print()
            print('='*50)
            start=input("Ready to start? 1 for no (you can continue browsing the menu), 2 for yes (this opens the calculator): ") 
            if start=="1":
               print()
               print('='*50)
               menu_input()
               break
               
            if start == '2':
                print()
                print('='*50)
                carbon_calculator()
                break

            
            if start not in ('1','2'):
                print()
                print('='*50)
                print ('Invalid input')
                continue
            
            
def carbon_calculator(): #message 3   
    while True:
        meals = input("How many meals are you planning to prepare? (1 person 1 meal → 5 people 5 meals): ") 
        try:
          meals=int(meals)
          break
        except ValueError:
          print()
          print('='*50)  
          print("\nYou have entered a non-numeric, please enter a valid number. Please try again.")
          continue 
   
    
    while True:
        print()
        print('='*50)
        choice=input("You can now input your ingredients. First, choose your category:\n1 for meat\n2 for vegetables\n3 for fruits\n4 for others?\n") # message 4 and 5
    
    
        if choice==("1"):
           print () 
           print('='*50)
           print ('This is what our calculator can currently track for you:')
           print()
           for each in meat:
               print (f'{each}')
           print()
           ingredient=input("Please input your ingredient's name based on what is in the list: ").lower()
           while ingredient not in meat: 
                   print () 
                   print('='*50)
                   print("Ingredient not in dataset.")
                   print()
                   print ('This is what our calculator can currently track for you:')
                   for each in meat:
                       print (f'{each}')
                   print ()
                   print('Please try again.')
                   ingredient=input("Please input your ingredient's name: ")
           else:
            print()
            print('='*50)
            print(f'You have chosen {ingredient}')
            while True: # need to check if it is a float. you can define this as a separate function and add it in as well if you wish
                weight = input("What is the total weight of this ingredient in kilograms?: ")
                try:
                    weight = float(weight)
                    break
                except:
                    print ('Please insert a number')
                    continue
                
            print()
            print('='*50)    
            print (f'This ingredient, {ingredient}, has a carbon footprint of {meat[ingredient]}kg per kilogram of ingredient')
            print (f'You have purchased {weight} kg of this ingredient. The total carbon footprint from this purchase is {weight*meat[ingredient]} kg')
            print (f'Per meal, this would be {(weight*meat[ingredient])/meals} kg')
            
            if permission2() == 'yes':
                continue
            else:
                break
            
        
        elif choice==("2"):
                print ()
                print('='*50)
                print ('This is what our calculator can currently track for you:')
                print()
                for each in vegetables:
                    print (f'{each}')   
                print()
                ingredient=input("Please input your ingredient's name: ").lower()
                while ingredient not in vegetables:
                    print () 
                    print('='*50)
                    print("Ingredient not in dataset.")
                    print()
                    print ('This is what our calculator can currently track for you:')
                    for each in vegetables:
                        print (f'{each}')
                    print ()
                    print('Please try again.')
                    print("Ingredient not in dataset.")
                    
                    ingredient=input("Please input your ingredient's name: ")
                else:
                    print()
                    print('='*50)
                    print(f'You have chosen {ingredient}')
                    while True: 
                        weight = input("What is the total weight of this ingredient in kilograms?: ")
                        try:
                            weight = float(weight)
                            break
                        except:
                            print ('Please insert a number')
                            continue
                        
                    print()
                    print('='*50)    
                    print (f'This ingredient, {ingredient}, has a carbon footprint of {vegetables[ingredient]}kg per kilogram of ingredient')
                    print (f'The total carbon footprint of your ingredient is {weight*vegetables[ingredient]} kg')
                    print (f'Per meal, this would be {(weight*vegetables[ingredient])/meals} kg')
                    
                    if permission2() == 'yes':
                        continue
                    else:
                        break
                    
        
        elif choice==("3"):
                print()
                print('='*50)
                print ('This is what our calculator can currently track for you:')
                print()
                for each in fruits:
                    print (f'{each}')
                print()
                ingredient=input("Please input your ingredient's name: ").lower()
                while ingredient not in fruits: 
                    print("Ingredient not in dataset.")
                    print () 
                    print('='*50)
                    print("Ingredient not in dataset.")
                    print()
                    print ('This is what our calculator can currently track for you:')
                    for each in fruits:
                        print (f'{each}')
                    print ()
                    print('Please try again.')
                    ingredient=input("Please input your ingredient's name: ")
                else:
                    print()
                    print('='*50)
                    print(f'You have chosen {ingredient}')
                    while True:
                        weight = input("What is the total weight of this ingredient in kilograms?: ")
                        try:
                            weight = float(weight)
                            break
                        except:
                            print ('Please insert a number')
                            continue
                    print()
                    print('='*50)    
                    print (f'This ingredient, {ingredient}, has a carbon footprint of {fruits[ingredient]}kg per kilogram of ingredient')
                    print (f'The total carbon footprint of your ingredient is {weight*fruits[ingredient]} kg')
                    print (f'Per meal, this would be {(weight*fruits[ingredient])/meals} kg')
                    if permission2() == 'yes':
                        continue
                    else:
                        break
                    
                    
        elif choice==("4"):
                print ()
                print('='*50)
                print ('This is what our calculator can currently track for you:')
                print()
                for each in others:
                    print (f'{each}') 
                print()
                ingredient=input("Please input your ingredient's name: ").lower()
                while ingredient not in others: 
                    print("Ingredient not in dataset.")
                    print () 
                    print('='*50)
                    print("Ingredient not in dataset.")
                    print()
                    print ('This is what our calculator can currently track for you:')
                    for each in others:
                        print (f'{each}')
                    print ()
                    print('Please try again.')
                    ingredient=input("Please input your ingredient's name: ")
                else:
                    print()
                    print('='*50)
                    print(f'You have chosen {ingredient}')
                    while True:
                        weight = input("What is the total weight of this ingredient in kilograms?: ")
                        try:
                            weight = float(weight)
                            break
                        except:
                            print ('Please insert a number')
                            continue
                    print()
                    print('='*50)    
                    print (f'This ingredient, {ingredient}, has a carbon footprint of {others[ingredient]}kg per kilogram of ingredient')
                    print (f'The total carbon footprint of your ingredient is {weight*others[ingredient]} kg')
                    print (f'Per meal, this would be {(weight*others[ingredient])/meals} kg') # example of how dictionary works :D
                    
                    if permission2() == 'yes':
                        continue
                    else:
                        break
                        

                    
        else:
          print()
          print('='*50)  
          print ('Please input 1 for meat, 2 for vegetables, 3 for fruits and 4 for other ingredients!')
          continue
      
        
            
            
def permission2():
    while True:
        print()
        print('='*50) 
        repeat = input ('Do you wish to input another ingredient? Input y if you wish to continue and n if you wish to exit: ')
        if repeat == 'y':
            return 'yes'
        elif repeat == 'n':
            return 'no'
        else:
            print()
            print('='*50) 
            print ('Please input either y to input another ingredient or n to exit.')
            continue
        
        

main_menu()


        
      





