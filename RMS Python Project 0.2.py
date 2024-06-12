#!/usr/bin/env python
# coding: utf-8

# In[11]:


class RMS:
    def __init__(self,restaurant_name,restaurant_menu):
        self.rn=restaurant_name
        self.menu=restaurant_menu
        self.total_bill=0
        self.user_order=''

    def welcome_user(self):
        #welcome user
        print('welcome to the',self.rn.title())

    def take_order(self):
        #take order
        self.user_order=input('please place your order here:')

    def display_menu(self):
        #display menu
        print('Menu:')
        print('*'*20)
        for i in self.menu:
            print(i.title(),self.menu[i])
        print('*'*20)

    def preparing_order(self):
        #preparing order
        import time
        print('preparing your:',self.user_order.title())
        time.sleep(0.3)
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]
    def serve_order(self):
        #serve order
        print('your order is ready!')
    def display_bill(self):
        #display bill
        print('your total bill:',self.total_bill)

    def verify_bill(self):
        #verify bill
        self.user_pay=int(input('please pay your bill here:'))
        while self.user_pay<self.total_bill:
            self.total_bill=self.total_bill-self.user_pay
            print('payment failed! please pay more',self.total_bill)
            self.user_pay=int(input('please pay your bill here:'))
        if self.user_pay>self.total_bill:
            print('here is your change:',self.user_pay-self.total_bill)
        else:
            pass
    def ty(self):
        print('Thanks for visiting',self.rn.title(),'!')

    def order_process(self):
        self.welcome_user()
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
            self.ask_user=input('Do you want order again?')
            while self.ask_user.lower()=='yes':
                self.repeat_order()
                self.ask_user=input('Do you want order again?')
            self.display_bill()
            self.verify_bill()
            self.ty()
        else:
            print('Invalid order!')
            self.order_process()
            
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_order()
            self.serve_order()
        else:
            print('Invalid order!')
            self.repeat_order()
        
if __name__=='__main__':
    
    ui=open('sunlight.txt','r')
    input_li=ui.readlines()
    rn=input_li[0].replace('\n','').title()
    food_items=input_li[1].replace('\n','').split(',')
    food_values=[int(i) for i in input_li[2].replace('\n','').split(',')]
    menu=dict(zip(food_items,food_values))
    mc=(RMS(restaurant_name=rn,restaurant_menu=menu))

    import tkinter as tk
    window=tk.Tk()
    window.geometry('300x90')
    window.title(mc.rn)
    label=tk.Label(window,text=mc.rn,font=('Helvetica',18))
    label.pack()
    button=tk.Button(window,text='CLICK HERE TO ORDER',command=mc.order_process)
    button.pack()
    window.mainloop()
        


# In[ ]:





# In[ ]:




