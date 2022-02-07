# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 09:25:09 2022

@author: User
"""
#Matthias Wesley's Code


welcome_msg = print("Welcome to Group 4’s App! \nThis is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes to your diet:")  


def menu(): # Message 2
    
    while True: 
        user_input = input("To view which ingredients you can input, type ‘menu'.\nIf you are ready to start entering your ingredients instead, type ‘start’: ")
        if user_input == 'menu':
            category()
            
        if user_input == 'start':
            carbon_calculator()
            break
            
        
        if user_input not in ('menu','start'):
            print("You have entered an invalid response. Please type menu or start.")
            continue
        
        else:
            break

def category():
    
        while True:
            menu_input = input("Select One of the 4 categories of ingredients available. \n1. Meat.\n2. Vegetables.\n3. Fruits.\n4. Dairy.\nCategory: ")
        
            if menu_input == '1':
                print("\nThese are the types of Meat available:\nLamb. \nBeef. \nPork. \nTurkey. \nChicken. \nFish.")
                
                permission()
    
            if menu_input == '2':
                print("\nThese are the types of Vegetables available:\nLentils. \nBeans. \nCarrot. \nBeansprout. \nCorn. \nSugarcane.")
                
                permission()
    
            if menu_input == '3':
                print("\nThese are the types of Fruits available:\nApple. \nOrange. \nStrawberry. \nPear. \nPineapple. \nGrapes. \nBanana.")
                
                permission()
        
            if menu_input == '4':
                print("\nThese are the types of Dairy available:\nCheese. \nEggs. \nMilk. \nChocolate. \nYoghurt.")
                
                permission()
        
            if menu_input not in ('1','2','3','4'):
                    print("You have entered an invalid response. Please enter a valid number between 1 - 4.")
                    continue

def permission():                
        while True:
            choice_input = input("Do you wish to explore other categories of ingredients? \nType 'y' for yes or 'n' to exit to the main menu: ")
        
            if choice_input == 'y':
                category()
        
            if choice_input == 'n':
                menu()
            
            else:
                print("You have entered an invalid response. Please type 'y' or 'n': ")

                
def carbon_calculator(): # Message 3
    
    while True:
        meals_input = input("Enter the number of meals you wish to prepare.\nfor eg. 1 person = 1 meal \n5 people = 5 meals\n\nNumber of meals: ")
        
        try:
            meals_input = int(meals_input)
            break
        
        except ValueError:
            print("you have entered a non-integer. Please enter only integers.")
            continue
        
    meats = ['lamb', 'beef', 'pork', 'turkey', 'chicken', 'fish']
    vegetables = ['lentils','beans','carrot','beansprout','corn','sugarcane']
    fruits = ['apple', 'orange', 'strawberry', 'pear', 'pineapple', 'grapes', 'banana']
    dairy = ['cheese', 'eggs', 'milk', 'chocolate', 'yoghurt']
    combined = meats + vegetables + fruits + dairy

#%%
    while True: # Message 4
        data_input = input("Please input the ingredient of your choice: ")
        
        if data_input not in combined:
            print("\nSorry. We currently do not have the data for the ingredient you have specified.")
            print("\nThese are the data for the ingredients we have:\n")
            print('Meats: ', *meats)
            print('Vegetables: ', *vegetables)
            print('Fruits: ', *fruits)
            print('Dairy:', *dairy)
            continue
    
        else: # Message 5
            print("What is the weight of the ingredient?")
            while True:
                weight_input = input("Please enter the weight in kilograms: ")
                try:
                    weight_input = float(weight_input)
                    break
                except ValueError:
                    print("You have entered an invalid response. Please type a number.")
                    continue
            break
                
                
        
menu()        
    
    

    
        




                
                        
                
    

  
        
        
        
    
       

       
    

              
          
    
    
    
                    
