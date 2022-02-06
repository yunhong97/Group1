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

userchoice1=input("View the available ingredients? Y/N:")
if userchoice1 in ('Y','y'):
    print(categories)
    subcategories=input("Please select a subcategory:")
    if subcategories in ('Meat','meat'):
        print(meatlist)
    elif subcategories in ('Fruits','fruits'):
        print(fruitlist)
    elif subcategories in ('Vegetables','vegetables'):
        print(vegetablelist)
    else:
       print("View the available ingredients? Y/N:")
if userchoice1 in ('N' ,'n'):
    userchoice2=input("Enter your ingredients? Y//N:")
    if userchoice2 in ('Y','y'):
        ingredient1=input("Ingredient 1:")
        ingredient2=input("Ingredient 2:")
        ingredient3=input("Ingredient 3:")
        ingredient4=input("Ingredient 4:")
        ingredient1=input("Ingredient 5:")
        ingredient2=input("Ingredient 6:")
        ingredient1=input("Ingredient 7:")
        ingredient2=input("Ingredient 8:") #SOS how to break the loop
    elif userchoice2 in ('N','n'):
        print("End.")
    else:
        print("End.")

#%%
# MESSAGE 3

userchoice3=float(input("How many meals to prepare? (1 person is equivalent to 1 meal):"))
#supposed to calculate limit here?

#%%
# MESSAGE 4

print("Enter ingredients below.")
ingredient1=input("Ingredient 1:")
try:
    weight1=input("Weight of ingredient 1:")
except ValueError:
    print ('Please input a valid number.')
