# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 01:46:13 2022

@author: 65947
"""
#message 1
welcome_msg=print("Welcome to Group 4’s App!\nThis is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes in your diet.")

#message 2
def main_menu():
    while True:
        choice = input("\nTo view which ingredients you can input, type 'menu'\nIf you are ready to start entering your ingredients instead, type 'start':").lower()
        if choice == 'menu':
            menu_input()
            break
        
        if choice == 'start':
            carbon_calculator()
            break
        
        if choice not in ('menu','start'):
            print ('Please input either menu or start')
            continue
    
def menu_input():
    while True:
            print("\nMeat\nVegtables\nFruits\nOthers")
            choice=input("Choice of ingredient? 1 for meat, 2 for vegetables, 3 for fruits and 4 for others? ")
            
            if choice==("1"):
                print("Meat:\nBeef\nChicken\nChicken Essence\nDuck\nFish\nLamb\nPork\nPoultry\nPrawns\nTuna\nTurkey")
                permission() 
                
            elif choice==("2"):
                print("Vegetables:\nBeansprout\nCarrot\nCorn\nFlour\nGinger\nLentils\nPotatoes\nTomatoes")
                permission()
                
            elif choice==("3"):
                print("Fruits:\nApple\nApricot\nBanana\nChilli peppers\nGrapes\nOrange\nPears\nPineapple\nStrawberry")
                permission()
                
            elif choice==("4"):
                print("Others:\nSugar Cane\nBeer\nCheese\nChocolate\nCoffee\nEggs\nHoney\nIce Cream\nInstant Noodles\nMilk\nNuts\nOil\nPasta\nRice\nTea")
                permission()
            else:
                print ('Please input 1 for meat, 2 for vegetables, 3 for fruits and 4 for other ingredients!')
                continue
       
def permission(): # so that user can either continue browsing (1), go straight to carbon calculator (2), or go to main menu (3)
        while True:
            start=input("Ready to start? 1 for no, 2 for yes, 3 if you wish to go to the main menu: ") 
            if start=="1":
               menu_input()
               break
               
            if start == '2':
                carbon_calculator()
                break
                
            if start == '3':
                main_menu()
                break
            
            if start not in ('1','2','3'):
                print ('Invalid input')
                continue
            
            
def carbon_calculator(): #message 3   
    while True:
        meals = input("How many meals are you planning to prepare? (1 person 1 meal → 5 people 5 meals): ") 
        try:
          meals=int(meals)
          break
        except ValueError:
          print("\nYou have entered a non-numeric, please enter a valid number.")
          continue # this is how to loop it!
   
    
    choice=input("Choice of ingredient?\n1 for meat\n2 for vegetables\n3 for fruits\n4 for others?\n") #message 4 and 5
    if choice==("1"):
        print("Meat:\nBeef\nChicken\nChicken Essence\nDuck\nFish\nLamb\nPork\nPoultry\nPrawns\nTuna\nTurkey")
    elif choice==("2"):
        print("Vegetables:\nBeansprout\nCarrot\nCorn\nFlour\nGinger\nLentils\nPotatoes\nTomatoes")
    elif choice==("3"):
        print("Fruits:\nApple\nApricot\nBanana\nChilli peppers\nGrapes\nOrange\nPears\nPineapple\nStrawberry")
    elif choice==("4"):
        print("Others:\nSugar Cane\nBeer\nCheese\nChocolate\nCoffee\nEggs\nHoney\nIce Cream\nInstant Noodles\nMilk\nNuts\nOil\nPasta\nRice\nTea")

    if choice==("1"):
       ingredient=input("Please input your ingredient's name: ")
       meat=["beef","lamb","chicken"]
       while ingredient not in meat: 
               print("Ingredient not in dataset, try again: ")
               ingredient=input("Please input your ingredient's name: ")
       else:
            print(ingredient)
            while True: # need to check if it is a float. you can define this as a separate function and add it in as well if you wish
                weight = input("What is the total weight of this ingredient?: ")
                try:
                    weight = float(weight)
                    break
                except:
                    print ('Please insert a number')
                    continue
    
    elif choice==("2"):
            ingredient=input("Please input your ingredient's name: ")
            vegetables=["beansprout","carrot","corn"]
            while ingredient not in vegetables:
                print("Ingredient not in dataset, try again: ")
                ingredient=input("Please input your ingredient's name: ")
            else:
                print(ingredient)
                while True: 
                    weight = input("What is the total weight of this ingredient?: ")
                    try:
                        weight = float(weight)
                        break
                    except:
                        print ('Please insert a number')
                        continue
    
    elif choice==("3"):
            ingredient=input("Please input your ingredient's name: ")
            fruits=["Apple","Apricot","Banana"]
            while ingredient not in fruits: 
                print("Ingredient not in dataset, try again: ")
                ingredient=input("Please input your ingredient's name: ")
            else:
                print(ingredient)
                while True:
                    weight = input("What is the total weight of this ingredient?: ")
                    try:
                        weight = float(weight)
                        break
                    except:
                        print ('Please insert a number')
                        continue
                
    elif choice==("4"):
            ingredient=input("Please input your ingredient's name: ")
            others=["beer","cheese","chocolate"]
            while ingredient not in others: 
                print("Ingredient not in dataset, try again: ")
                ingredient=input("Please input your ingredient's name: ")
            else:
                print(ingredient)
                while True:
                    weight = input("What is the total weight of this ingredient?: ")
                    try:
                        weight = float(weight)
                        break
                    except:
                        print ('Please insert a number')
                        continue

main_menu()

#%% (ignore)
elif choice==("2"):
   input("Please input your ingredient's name: ")
   if choice!=("vegetables"):
           input("Ingredient not in dataset, try again: ")
elif choice==("3"):
   input("Please input your ingredient's name: ")
   if choice!=("fruits"):
           input("Ingredient not in dataset, try again: ")    
elif choice==("4"):
   input("Please input your ingredient's name: ")
   if choice!=("others"):
           input("Ingredient not in dataset, try again: ")    
        
        
      





