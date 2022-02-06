#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:17:09 2022

@author: minhui
"""


# MESSAGE 1
 
print('''Welcome to Group 4's App!
This is an app to calculate your carbon footprint from your shopping! The goal is to help you save the Earth by making minute alterations to your shopping habits!''')

#%%
# MESSAGE 2
categories=["Meat", "Fruits", "Vegetables"]
meatlist=["Chicken", "Pork", "Beef"]
fruitlist=["Apple", "Orange", "Pear"]
vegetablelist=["Bokchoy", "Celery", "Spinach"]
ingredient_input = [] # to store user input of ingredients 

#%%
def main():
    while True:
        userchoice1=input("View the available ingredients? Y/N:")
        if userchoice1 not in ('y','Y','N','n'):
           continue # goes to userchoice1 ('View the available ingredients? y/n)
           
        if userchoice1 in ('Y','y'):
            while True:
                print(categories)
                subcategories=input("Please select a subcategory:")
                
                if subcategories in ('Meat','meat'):
                    print(meatlist)
                    break
                    
                elif subcategories in ('Fruits','fruits'):
                    print(fruitlist)
                    break
                    
                elif subcategories in ('Vegetables','vegetables'):
                    print(vegetablelist)
                    break
                    
                else:
                    print('Please input a proper subcategory')
                    continue
        
        if userchoice1 in ('N' ,'n'):
            userchoice2=input("Enter your ingredients? Y//N:")  # a bit confused as to what is this for. I thought it was for the carbon calculator but at the bottom there is another way for user to input ingredients
            counter = 0
            if userchoice2 in ('Y','y'): 
                while True:
                    counter +=1 
                    ingredient=input(f"Ingredient {counter}:")
                    ingredient_input.append(ingredient) # to add it into the list of ingredients inputted by user
                    if permission() == 'yes':
                        continue
                    else:
                        carbon_calculator()
                        break
                    
       
            if userchoice2 in ('N','n'):
                print("End.")
                break 
            else:
                print("End.")
                break 
            
#%%    
def permission():
    while True:
        permission = input ('Add another ingredient?')
        if permission in ('Y','y'):
            return 'yes'
        if permission in ('N','n'):
            break
        else:
            print ('Please enter y or n!')
            
#%%
# MESSAGE 3
def carbon_calculator():
    userchoice3=float(input("How many meals to prepare? (1 person is equivalent to 1 meal):"))
    #supposed to calculate limit here? you can calculate here or later. so long as if there is a variable to store meal count, gud enuf

# MESSAGE 4
    print("Enter ingredients below.") # do you want to loop here as well? if so, can refer to line 79 to 84
    ingredient1=input("Ingredient 1:") 
    
    while True:
        weight1 = input("Weight of ingredient 1:")
        try:
            weight1=float(weight1) # this is to check for value error
            break
        except ValueError:
            print ('Please input a valid number.')
            continue
        break

main()



