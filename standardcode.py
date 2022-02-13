# variables to be used for calculator
carbon_per_meal = 1.7
tree_absorb_per_year = 21.7724
carbon_emission_dataset = {'beef':27,'apple':0.11,'beansprout':0.2,'cane sugar': 3}
meat = ['beef']
fruits = ['apple']
vegetables = ['beansprout']
others = ['cane sugar']
user_input = {}


# main function
def MAIN():
    
# message 1
    print ('''\nWelcome to Group 4’s App! 
This is an app to calculate your carbon footprint from your shopping, and help you save the Earth just from small changes to your diet :)
    ''')
    
    
# message 2
    while True:
        print('='*50)
        print ('''\nTo view which ingredients you can input, type ‘menu’
If you are ready to start entering your ingredients instead and calculate your carbon footprint, type ‘start’.
        ''')
        
        user_input = input ('Do you wish to view the menu (type menu) or start entering your ingredients (type start)? ')
        if user_input not in ('start','menu'):
            print('='*50)
            print ('\nPlease input menu or start!')
            continue
        
        elif user_input == 'menu':
            print('='*50)
            while menu():
                permission()
                break
            continue
            
        elif user_input == 'start':
            print('='*50)
            carbon_calculator()
            break

# menu
def menu():
    while True:
        menu = input ('''We have 4 categories of ingredients you can input:
Meat (1)
Fruits (2)
Vegetables (3)
Others (4)

Type the corresponding number to view the specific ingredients you can input under that category: ''')

        if menu not in ('1','2','3','4'):
            print('='*50)
            print ('You have entered an invalid input. Type 1 for Meat, 2 for Fruits, 3 for Vegetables and 4 for Others: ')
            continue
        else:
            if menu == '1':
                for each in meat:
                    print(each)
                print('='*50)
                return True
                break
            if menu == '2':
                for each in fruits:
                    print(each)
                print('='*50)
                return True
                break
            if menu == '3':
                for each in vegetables:
                    print(each)
                print('='*50)
                return True
                break
            if menu == '4':
                for each in others:
                    print(each)
                print('='*50)
                return True
                break
            
# to ask user if he wants to source other categories or exit to main menu              
def permission():
    while True:
        permission = input ('Do you wish to source for other categories? Type "y" for yes and "n" to exit to main menu: ')
        if permission == 'y'.lower():
            menu()
        elif permission == 'n'.lower():
            break
        else:
            print ('Please input "y" to source for other categories and "n" to exit to main menu.')
            continue
      
# to record down each ingredient from user input  
def carbon_calculator():
    while True:
        # message 3
        meals = input('How many meals do you want to take into account for? ')
        try:
            meals = int(meals)
            break
        except ValueError:
            print ('Please input a number')
            continue
        
    while True:
        # message 4
        ingredient = input ('Please input your ingredient: ')
        if ingredient not in carbon_emission_dataset:
            print ('Sorry, we currently do not have the data for this ingredient. These are our available ingredients')
            print (f''' 
Meat: {meat}
Fruits: {fruits}
Vegetables: {vegetables}
Others: {others}''')
            continue
        
        else:
            # message 5
            while True:
                weight = input ('Please enter total weight of ingredients in kilograms: ')
                try:
                    weight = float(weight)
                    break
                except ValueError:
                    print ('Please input a number')
                    continue
            break
        
            
MAIN()
        
        
    




