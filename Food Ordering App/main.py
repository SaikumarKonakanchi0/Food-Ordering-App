import sys
from admin import *
from user import *

admin = Admin_Panel()
user = User_Panel()

while True:
    print("Press 1 for Admin Login")
    print("Press 2 for User Login")
    print("Press 3 for Exit")
    print("*" * 100)
    
    choice = int(input("Enter Your Choice: "))
    print("*" * 100)
    
    if choice == 1:
        print("************************Admin Login*******************************")
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        
        if admin.admin_login(username, password):
            print("Logged in Successfully")
            while True:
                print("Press 1 for Add Food Items")
                print("Press 2 for Edit Food Items")
                print("Press 3 for Read Food Items")
                print("Press 4 for Remove Food Items")
                print("Press 5 for Logout")
                print("*" * 100)
                
                admin_choice = int(input("Enter Your Choice: "))
                print("*" * 100)
                
                if admin_choice == 1:
                    print(admin.add_food_items())
                    print("*" * 100)
                    print("Food Item Added Successfully")
                    print("*" * 100)
                
                elif admin_choice == 2:
                    print(admin.edit_food_items())
                    print("*" * 100)
                    print("Food Item Updated Successfully")
                    print("*" * 100)
                
                elif admin_choice == 3:
                    admin.read_food_items()
                    print("*" * 100)
                
                elif admin_choice == 4:
                    print(admin.remove_food_items())
                    print("*" * 100)
                    print("Food Item Removed Successfully")
                    print("*" * 100)
                
                elif admin_choice == 5:
                    print("Logged out")
                    print("*" * 100)
                    break
                
                else:
                    print("Please enter a valid choice")
        
        else:
            print("Invalid Credentials")

    elif choice == 2:
        print("**********************User LogIN*************************")
        username = input("Enter User Username: ")
        password = input("Enter User Password: ")
        
        if user.user_login(username, password):
            print("Logged in Successfully")
            while True:
                print("Press 1 for Place Order")
                print("Press 2 for Order History")
                print("Press 3 for Update User Profile")
                print("Press 4 for Logout")
                print("*" * 100)
                
                user_choice = int(input("Enter Your Choice: "))
                print("*" * 100)
                
                if user_choice == 1:
                    user.place_order()
                
                elif user_choice == 2:
                    print(user.order_history())
                    print("*" * 100)
                
                elif user_choice == 3:
                    print(user.update_user())
                    print("*" * 100)
                    print("User Profile Updated Successfully")
                    print("*" * 100)
                
                elif user_choice == 4:
                    print("Logged out")
                    print("*" * 100)
                    break
                
                else:
                    print("Please enter a valid choice")
        else:
            print('Invalid Credentials')
    
    if choice == 3:
        print("Thank You for using our application")
        sys.exit()
