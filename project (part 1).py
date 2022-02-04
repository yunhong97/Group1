# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 01:46:13 2022

@author: 65947
"""
#message 1
welcome_msg=print("Welcome to Group 4’s App!\nThis is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes in your diet.")

#message 2
def menu_input():
    menu=input("\nTo view which ingredients you can input, type 'menu':")
    if menu==("menu")or("MENU"):
        print("\nMeat\nVegtables\nFruits\nOthers")
        choice=input("Choice of ingredient? 1 for meat, 2 for vegetables, 3 for fruits and 4 for others? ")
        if choice==("1"):
            print("Meat:\nBeef\nChicken\nChicken Essence\nDuck\nFish\nLamb\nPork\nPoultry\nPrawns\nTuna\nTurkey")
        elif choice==("2"):
            print("Vegetables:\nBeansprout\nCarrot\nCorn\nFlour\nGinger\nLentils\nPotatoes\nTomatoes")
        elif choice==("3"):
            print("Fruits:\nApple\nApricot\nBanana\nChilli peppers\nGrapes\nOrange\nPears\nPineapple\nStrawberry")
        elif choice==("4"):
            print("Others:\nSugar Cane\nBeer\nCheese\nChocolate\nCoffee\nEggs\nHoney\nIce Cream\nInstant Noodles\nMilk\nNuts\nOil\nPasta\nRice\nTea")
menu_input()        

#message 3
start=input("Ready to start? 1 for no, 2 for yes: ")
while start!="2":
   menu_input()  
   start=input("Ready to start? 1 for no, 2 for yes: ")
else:
    try:
      meals=int(input("How many meals are you planning to prepare? (1 person 1 meal → 5 people 5 meals): "))
    except ValueError:
      print("\nYou have entered a non-numeric, please enter a valid number.")
      meals=int(input("How many meals are you planning to prepare? (1 person 1 meal → 5 people 5 meals): ")) #how to loop this? if user keep answer wrongly   
   
#message 4 and 5
    choice=input("Choice of ingredient?\n1 for meat\n2 for vegetables\n3 for fruits\n4 for others?\n")
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
           float(input("What is the total weight of this ingredient?: "))

elif choice==("2"):
        ingredient=input("Please input your ingredient's name: ")
        vegetables=["beansprout","carrot","corn"]
        while ingredient not in vegetables:
            print("Ingredient not in dataset, try again: ")
            ingredient=input("Please input your ingredient's name: ")
        else:
            print(ingredient)
            float(input("What is the total weight of this ingredient?: "))

elif choice==("3"):
        ingredient=input("Please input your ingredient's name: ")
        fruits=["Apple","Apricot","Banana"]
        while ingredient not in fruits: 
            print("Ingredient not in dataset, try again: ")
            ingredient=input("Please input your ingredient's name: ")
        else:
            print(ingredient)
            float(input("What is the total weight of this ingredient?: "))
            
elif choice==("4"):
        ingredient=input("Please input your ingredient's name: ")
        others=["beer","cheese","chocolate"]
        while ingredient not in others: 
            print("Ingredient not in dataset, try again: ")
            ingredient=input("Please input your ingredient's name: ")
        else:
            print(ingredient)
            float(input("What is the total weight of this ingredient?: "))
    
#%%
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
        
        
      





