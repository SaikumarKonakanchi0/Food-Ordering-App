#Admin Functionalities
import json
class Admin_Panel:
    def __init__(self):
        self.count=0
        self.main_food_dict={}
        self.updated_food={}

    def admin_login(self,username,password):
        if username=='Admin' and password=='Password':
            return True
        return False

    def add_food_items(self):
        self.count+=1
        food_name=input(f'Enter name of food: ')
        quantity=input(f"Enter number of Qunatity: ")
        price=float(input(f"Enter price per item of food: "))
        discount=(price*25)/100
        stock=input(f'Enter the Stock Quantity of food: ')
        food_dict={'FoodName':food_name,'Quantity':quantity,'Price':price,'Discount':discount,'Stock':stock}
        self.main_food_dict[self.count]=food_dict
        with open('Food_add.json','w') as f:
            json.dump(self.main_food_dict,f,indent=4)
        return self.main_food_dict
    
    def edit_food_items(self):
        print("****************Edit Food Items****************")
        with open('Food_Add.json','r') as f:
            data=json.load(f)
        for k,v in data.items():
            print(f'FoodID: {k} || Food_Details: {v}')
            print('*'*100)
        food_id=input('Enter the FoodID you want to update: ')
        field=input('Enter the field you want to update: ')
        updated_value=input('Enter the updated value: ')
        data[food_id][field]=updated_value
        with open('Updated_Food.json','w') as f:
            json.dump(data,f,indent=4)
        return data
    
    def read_food_items(self):
        with open('Updated_Food.json','r') as f:
            data=json.load(f)
        for k,v in data.items():
            print(f'FoodID: {k} || Food_Details: {v}')
            print('*'*100)

    def remove_food_items(self):
        with open('Updated_Food.json','r') as f:
            data=json.load(f)
        for k,v in data.items():
            print(f'FoodID: {k} || Food_Details: {v}')
            print('*'*100)
        remove_food=input('Enter FoodID which you want to delete: ')
        del data[remove_food]
        return data

