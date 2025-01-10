import json
from inventory import Inventory



class Inventory_Management():
    def __init__(self, inventory, filename="mappings.json"):
        self.inventory = inventory
        self.filename = filename
        self.inventory = self.load_from_file()
        
    def get_departments(self):
        return list(self.inventory.keys())
    
    def create_department(self, department):
        if department not in self.inventory:
            self.inventory[department] = {}
            self.save_to_file()
            
    def edit_department(self, old_name, new_name, department):
        if old_name in self.inventory:
            self.inventory[new_name] = self.inventory.pop(old_name)
        else:
            print(f'{old_name} not found...')
            
        
    def remove_department(self, department):            
        if department in self.inventory:
            del self.inventory[department]
            self.save_to_file()
                
    def view_departments(self):
        if not self.inventory:
            print("\n No departments to display")
        else:
            print("Departments:", self.inventory.keys())
    
    def handle_department(self):
        pass
            
    def get_sections(self, department):
        return list(self.inventory[department].keys())
            
    def create_section(self, department, section):    
        if section not in self.inventory[department]:
            self.inventory[department][section] = {}
            self.save_to_file
    
    def product_management(self, departments, sections, brand, model, price, quantity):    
        #ADD PRODUCTS
        
        for department in departments:
            if department in self.inventory:
                # Iterate through the sections
                for section in sections:
                    if section in self.inventory[department]["sections"]:
                        # If the brand does not exist, initialize it
                        if brand not in self.inventory[department]["section"][section]["brands"]:
                            self.inventory[department]["section"][section]["brands"][brand] = {"model": {}}
                        
                        # Add the model under the specified brand
                        self.inventory[department]["section"][section]["brands"][brand]["model"][model] = {
                            "Price": price,
                            "Qty": quantity
                        }
            
        self.save_to_file()
        
        print("Added")
        print(f'{quantity}')
        print(f'{brand}')
        print(f'{model}')
        print(f'for: {price} ea.')


    def order_inventory(self, departments, section, brand, model, quantity):
        pass
    def inventory_tracking(self, departments, section, brand, model):
        pass
    def notifications(self, departments, section, brand, model):
        pass
    
    
    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.inventory, file, indent=2)
            
    
    def load_from_file(self):
        with open(self.filename, "r") as file:
            return json.load(file)
        
