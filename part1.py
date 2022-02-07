
welcomet= ("Welcome to Group 4â€™s App! This is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes to your diet.")
print(welcomet)

#Message2
#Ingredient List
meats = ["Beef","Chicken","Duck","Fish","Lamb", "Pork"]
fruits = ["Apple","Pear", "Banana", "Grapes", "Oranges"]
vegetables = ["Beansprout", "Carrot", "Corn","Ginger","Potatoes","Lentils"]
others = ["Cane Sugar", "Beans", "Coffee", "Tea", "Eggs", "Honey"]
all_ingredients = meats + fruits + vegetables + others # makes it easier to check for message 4
#End of Ingredients List

# main function
def main():
    while True: # this is to help loop the code 
        print("To view available ingredients for selection, type 'menu'.")
        print("To enter ingredients for calculation, type 'start'.")
        
        uselect = input("Menu or start:")
        
        if uselect == "menu":
            showmenu()  # this brings you to the show menu function
            break
            
        if uselect =="start":
            carbon_calculator() # this brings you to the carbon calculator
            break
    
        else:
            print ('Please input either menu or start')
            continue # this brings you back to line 16 - print (To view...)
    
    
    
def showmenu():
        while True:
            umenu = input("You can choose from meats, fruits, vegetables or others:").lower()
            if umenu == "meats":
                print(meats)
                permission() # permission function
                break

                        
            if umenu == "fruits":
                print(fruits)
                permission()
                break
                    
            if umenu == "vegetables":
                print(vegetables)
                permission()
                break
                    
            if umenu == "others":
                print(others)
                permission()
                break
                
            if umenu not in ('meats','others','fruits','vegetables'):
                print ("Invalid input. Please type either meats, fruits, vegetables or others.")
                continue 

def permission():
        while True:
            review = input("Do you wish to view other categories? Y/N:").upper()
            if review =="Y":
                showmenu()
            if review == 'N':
                main()
            else:
                print ('Please put either yes or no')
                continue


def carbon_calculator():
    #Message3    
    upax= int(input("How many meals are you preparing for? (1 meal per person if >1 pax)"))
    # number used to divide 

    while True: 
        try: # can use try-except if you want the user to input numbers
            upax == int (upax)
            break
        
        except ValueError: #Value Error as the user is entering a string, but the code only allows integers
            print ('Please enter a whole number')
            continue
        
    
    #Message4
    
    while True:
        i_name= input("Please input ingredient name:")
        if i_name in (all_ingredients):
            print("You have selected", (i_name))
            break
        
        else:
            print("Invalid selection, please try again")
            print (f'You can choose from {all_ingredients}')
            continue
        

    #Message5
    # Average safe carbon footprint per meal is ~0.365kg (2 tons carbon emission, 20% into food consumption ~400kg P.A / 365/ 3)
    
    while True:
        i_weight= input("Please input weight of ingredient in kg ")
        
        try:
            i_weight = float (i_weight)
            break
        except:
            print ('Please input a number')
            continue
            
    print(f"The carbon footprint of your {i_name} is {i_weight}")#carbon footprint of ingredient per kg )
    print(f"The carbon footprint of your meal is {i_weight}")  #carbon footprint / upax )

# You can use f printing so that it is easier to type your print statements. Simply put f in front, type
# everything as per normal, but put {} around all your variables

main()
