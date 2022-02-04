
welcomet= ("Welcome to Group 4’s App! This is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes to your diet.")
print(welcomet)
#%%
#Message2
#Ingredient List
meats = ["Beef","Chicken","Duck","Fish","Lamb", "Pork"]
fruits = ["Apple","Pear", "Banana", "Grapes", "Oranges"]
vegetables = ["Beansprout", "Carrot", "Corn","Ginger","Potatoes","Lentils"]
others = ["Cane Sugar", "Beans", "Coffee", "Tea", "Eggs", "Honey"]
#End of Ingredients List

print("To view available ingredients for selection, type 'menu'.")
print("To enter ingredients for calculation, type 'start'.")

uselect = input("Menu or start:")

def showmenu():
    if uselect == "menu":
        umenu = input("You can choose from meats, fruits, vegetables or others:")
        if umenu == "meats":
            print(meats)
            review = input("Do you wish to view other categories? Y/N:")
            if review =="Y":
                showmenu()
                    
        elif umenu == "fruits":
            print(fruits)
            review = input("Do you wish to view other categories? Y/N:")
            if review =="Y":
                showmenu()
                
        elif umenu!= "vegetables":
            print(vegetables)
            review = input("Do you wish to view other categories? Y/N:")
            if review =="Y":
                showmenu()
                
        elif umenu!="others":
            print(others)
            review = input("Do you wish to view other categories? Y/N:")
            if review =="Y":
                showmenu()
                
        else:
            tryagain=input("Invalid input, try again? Y/N:")
            if tryagain == "Y":
                showmenu()
            if tryagain =="N":
                exit


if uselect == "menu":
    showmenu()
    
elif uselect =="start":
    print("Test")      

#%%
#Message3

upax= int(input("How many meals are you preparing for? (1 meal per person if >1 pax)"))
# number used to divide 

while upax != int():
    upax = int(input(""))
    

#%%
#Message4

meats = ["Beef","Chicken","Duck","Fish","Lamb", "Pork"]
fruits = ["Apple","Pear", "Banana", "Grapes", "Oranges"]
vegetables = ["Beansprout", "Carrot", "Corn","Ginger","Potatoes","Lentils"]
others = ["Cane Sugar", "Beans", "Coffee", "Tea", "Eggs", "Honey"]

i_name= input("Please input ingredient name:")

while True:
    if i_name in (meats):
        print("You have selected", (i_name))
    

else:
    print("Invalid selection, please try again")
    
    
#%%
#Message5
# Average safe carbon footprint per meal is ~0.365kg (2 tons carbon emission, 20% into food consumption ~400kg P.A / 365/ 3)

i_weight= float(input("Please input weight of ingredient in kg"))

print("The carbon footprint of your", i_name, "is", i_weight *#carbon footprint of ingredient per kg )
print("The carbon footprint of your meal is", i_weight * #carbon footprint / upax )


