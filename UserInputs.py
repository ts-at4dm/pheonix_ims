from inventory import Inventory
from Inventory_Management import Inventory_Management
import time

class User_Inputs():
    def __init__(self, inventory_management):
        self.inventory_management = inventory_management
    
    def greeting(self):
        print("Pheonix Inventory Management System")    
        print("Select from the following options")    
        pass


    def department_management(self):

        def create_department(self):
            while True:
                #Get the current list of departments
                departments = self.inventory_management.get_departments()

                #Checks to see if there are any departments listed
                if not departments:
                    print("No departments available.")
                    print("Would you like to create a department(s)?")
                    choice = input("y/n?: ")
                    #If the user enters y for yes, the system will then go through
                    #asking how many departments they would like to create and the names. 
                    if choice == 'y':
                        print("Please enter the number of departments you wish to create:")
                        try:
                            dep_num = int(input(":> "))
                            for dep in range(dep_num):
                                dep_name = input("Enter the name of the new department: ")
                                if dep_name in self.inventory_management.get_departments():
                                    print(f"{dep_name} already exists, please try again.")
                                    print(f'You have {dep_num} department(s) remaining...')
                                else:
                                    self.inventory_management.create_department(dep_name)
                                    print(f'{dep_name} added successfully!')
                                    dep_num -= 1  # Decrease department count only after adding a valid department
                                    print(f'You have {dep_num} department(s) remaining...')
                        except ValueError:
                            print("Invalid input, please enter a valid number.")

                    #If the user enters n for no, the system will return them to the main menu.    
                    elif choice == "n":
                        print("Returning to the main menu...")
                        time.sleep(2) #delays the return for 2 seconds
                        break
                else:
                    print("Departments")
                    for i, dep in enumerate(departments, start = 1):
                        print(f'{i}: {dep}')
            
            
            

              
            
            #If there are departments to display, the system will display all of the departments and then
            #prompt the user to choose which department they would like to enter, or ask them if they
            #would like to create more departments.    
                
                
                print("To select a department, enter the number below.")
                print("Type 'add' or 'remove' below to add/remove a department")
                print("Enter return to return to the main menu.")    
                choice = input(":> ")
                
                if choice.isdigit():
                    dep_num = int(choice)
                    if 0 <= dep_num <= len(departments):
                        sel_dep = departments[dep_num - 1]
                        sections = self.inventory_management.get_sections(sel_dep)
                        if not sections:
                            print("No available Sections to display...")
                            print("Would you like to create a section?")
                            create_Sec = input("y/n: ")
                            if create_Sec == 'y':
                                print("Enter the number of sections you wish to create:")
                                try:
                                    sec_num = int(input(":> "))
                                    for sec in range(sec_num):
                                        sec_name = input("Enter the name of the new section")
                                        if sec_name in self.inventory_management.get_sections(sel_dep):
                                            print(f'{sec_name} already exists, please try again.')
                                            print(f'You have {sec_name} section(s) remaining...')
                                        else:
                                            self.inventory_management.create_section(sec_name)
                                            print(f'{sec_name} added successfully!')
                                            sec_num -= 1
                                            print(f'You have {sec_num} section(s) remaining...')
                                except ValueError:
                                    print("Invalid Input, please enter a valid number.")
                                    
                            elif create_Sec == 'n':
                                print("Returning to departments menu...")
                                time.sleep(2)
                                break
                                
                            else:
                                print('Invalid input, please try again.')
                        else:
                            print(f'{dep_name} {sec_name}')
                            for i, sec in enumerate(sections, start = 1):
                                print(f'{i}: {sec}')
                elif choice == 'add':
                    print("Please enter the number of departments you wish to create: ")
                    try:
                        dep_num = int(input(":> "))
                        for dep in range(dep_num):
                            dep_name = input("Enter the name of the new department: ")
                            if dep_name in self.inventory_management.get_departments():
                                print(f'{dep_name} already exists, please try again.')
                                print(f'You have {dep_num} department(s) remaining...')
                            else:
                                self.inventory_management.create_department(dep_name)
                                print(f'{dep_name} added successfully!')
                                dep_num -= 1  # Decrease department count only after adding a valid department
                                print(f'You have {dep_num} departments remaining...')
                    except ValueError:
                        print("Invalid input, please enter a valid number.")
                                        #Department edit place holder
#===========================================================================================================                        
                elif choice == 'remove':
                    print('Please enter the number of the department you wish you remove.')
                    try:
                        dep_remove = int(input(":>"))
                        if 1 <= dep_remove <= len(departments):
                            dep_to_remove = departments[dep_remove - 1]
                            print(f'Are you sure you wish to remove {dep_to_remove} department?: ')
                            choice = input("y/n: ")
                            if choice == 'y':
                                self.inventory_management.remove_department(dep_to_remove)
                                print(f'{dep_to_remove} department has been removed...')
                            else:
                                break
                    except ValueError:
                        print("Invalid input, please enter a valid number.")
                        
                elif choice == 'return':
                    print("Returning to the main menu...")
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice. Please type 'add', 'remove', or 'return'.")            
                    
                  
    def section_management(self):
        pass