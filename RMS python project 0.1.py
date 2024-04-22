#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#RMS
import tkinter as tk

class RMS:

    def __init__(self,restaurant_name,restaurant_menu,root):
        self.rest_name=restaurant_name
        self.user_order=''
        self.menu=restaurant_menu
        self.total_bill=0
        self.root=root
        self.create_widgets()

    def create_widgets(self):

        self.name=tk.Label(self.root,text='Made By: Rupali Kore',font=('Helvetica',14))
        self.name.pack()
        self.welcome_label=tk.Label(self.root,text=f'Welcome to the {self.rest_name.title()}',font=('Helvetica',15))
        self.welcome_label.pack()
        
        self.label2=tk.Label(self.root,text='Menu',font=('Helvetica',16))
        self.label2.pack()

        # Show Menu Button
        self.show_menu_button = tk.Button(self.root, text="Show Menu", command=self.display_menu)
        self.show_menu_button.pack()

        # Order Process Button
        self.order_process_button = tk.Button(self.root, text="Start Order", command=self.order_process)
        self.order_process_button.pack()

        


        self.bill_label = tk.Label(self.root, text='', font=('Helvetica', 18))
        self.bill_label.pack()
        
    
    def welcome_user(self):
        #welcome user
        print('Welcome to the',self.rest_name.title())
        
    def take_order(self):
        #take order
        self.user_order=input('Please place your order here:')
        
    def display_menu(self):
       #display menu
        print('Menu:')
        print("*"*30)
        for i in self.menu:
            print(i.title(),self.menu[i],sep='\t')
        print("*"*30)
        
        
    def preparing_order(self):
        #preparing order
        import time
        print('Preparing your', self.user_order.title())
        time.sleep(0.2)
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]
        
    def serve_order(self):
        #serve order
        print('Your order is ready!')  
        
    def display_bill(self):
        #display bill
        print('Your bill:', self.total_bill)
        
    def verify_bill(self):
        self.user_pay=int(input('Please pay your bill here:'))
        #verify bill
        while self.user_pay<self.total_bill:
            self.total_bill=self.total_bill-self.user_pay
            print('Payment Failed! Please pay more', self.total_bill)
            self.user_pay=int(input('Please pay your bill here:'))
        if self.user_pay>self.total_bill:
            print('Here is your change', self.user_pay-self.total_bill)
        else:
            pass
    def ty(self):
        #thank you
        print('Thank you for visiting',self.rest_name.title())
    
    
        
    def order_process(self):
        
        self.take_order()
        
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.ask_user=input("Do you want to order again?")
            while self.ask_user.lower()=='yes':
                self.repeat_order()
                self.ask_user=input('Do you want to order again?')
                
            self.display_bill()
            self.verify_bill()
            self.ty()
        else:
            print('Invalid Order!')
            self.order_process()
            
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu: 
            self.preparing_order()
            self.serve_order() 
        else:
            print('Invalid order') 
            self.repeat_order()
            
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Restaurant order process')
    menu={'hot coffee': 180, 'cappuccino': 160, 'espresso': 130, 'drip coffee': 170, 'cold coffee':200}
    mc=RMS(restaurant_name='Moonlight cafe',restaurant_menu=menu,root=root)
    root.mainloop()
    


# In[ ]:





# In[ ]:




