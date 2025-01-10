from UserInputs import User_Inputs
from Inventory_Management import Inventory_Management

def main():
    
    inventory_management = Inventory_Management(inventory={})

    while True:

        user_inputs = User_Inputs(inventory_management)
        user_inputs.greeting()
        
        print("1: Dashboard")
        print("2: Departments")
        print("3: Inventory Control")
        print("4: Reports")
        print("5: Users")
        print("6: Exit")

        main_selection = int(input("Enter Choice: "))


        match main_selection:
            case 1:
                pass 
            case 2:
                user_inputs.department_management()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass

if __name__ == "__main__":
    main()




