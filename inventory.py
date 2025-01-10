class Inventory():
    def __init__(self, departments, sections, brand, model, price, quantity):
        self.departments = departments
        self.section = sections
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
        
    def update_product(self, brand, model, price, qty):
        self.brand = brand
        self.model = model
        self.price = price
        self.qty = qty
        
    def __str__(self):
        pass
    