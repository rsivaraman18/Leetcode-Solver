def time_fun():
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        return date,time

class Banking():
    bank_name = 'Siva International Bank'

    def __init__(self):
        print('\t**************',Banking.bank_name,'*************')

    

    def create_account(self,name,location,age,pan,contact):
        Accno = len(customers) +1 + 1000
        new_data = { 'AccNo': Accno,     'Name': name,  'Location': location,  'Age': age,  'Pan': pan, 'Contact': contact,
                    'Balance': 500,  'DOJ': '12 am', 'Transaction': ['Initial deposit -- 500',] }
        customers[new_data['AccNo']] = new_data
        print(">>>>> New Account Created for",name)   
        print('\t Account Holder Name is  {} \n \t Acc Number is {} \n\t Balance is {}'.format(name,new_data['AccNo'],new_data['Balance'])) 
        print('>>>>> Thank You >>>>> ')      


    def display(self):
        if customers:
            for key,value in customers.items():
                print('{} --> {}'.format(key,value))         
        else:print('No Customers in the Bank')
        print(' >>>>> Thank You >>>>> ') 


    def balance(self,acc):
        account_details = customers.get(acc)
        if account_details:
            print("\t Balance : ",account_details['Balance'])      
        else:
            print(" \t Account not found.")
        print(' >>>>> Thank You >>>>> ') 



    def cust_details(self,acc):
        account_details = customers.get(acc)
        if account_details:
            print(">>>>> Customer Details for {}:".format(name))
            for key, value in account_details.items():
                print("\t{} >> {}".format(key,value))
        else:
            print(">>>>> Account not found.")
        
        print(' >>>>> Thank You >>>>> ') 


            
                   
        
    def withdrawl(self,acc,withdrawl):
        account_details = customers.get(acc)
        if account_details:
            balance = account_details['Balance']
            if balance > withdrawl:
                cur_bal = balance-withdrawl
                account_details['Balance'] = cur_bal
                transact = account_details['Transaction']
                t = time_fun()
                transact.append('On {}at {} withdrawl Rs{}'.format(t[0],t[1],withdrawl))
                print("\tCurrent Balance is {}".format(cur_bal))
            else:
                print('\tInsufficient Balance \n\t Balance {}'.format(balance))
        else:
            print(">>>>> Account not found.")
        
        print(' >>>>> Thank You >>>>> ') 


    def Deposit(self,acc,deposit):
        account_details = customers.get(acc)
        if account_details:
            balance = account_details['Balance']
            cur_bal = balance+deposit
            account_details['Balance'] = cur_bal
            t = time_fun()
            transact = account_details['Transaction']
            transact.append('On {} at {} Deposited Rs{}'.format(t[0],t[1],deposit))
            print("\tCurrent Balance is {}".format(cur_bal)) 
        else:
            print(">>>>> Account not found.")
        
        print(' >>>>> Thank You >>>>> ') 

    
    def Mini_statement(self,acc):
        account_details = customers.get(acc)
        if account_details:
            Transactions = account_details['Transaction']
            for transact in Transactions:
                print('\n\t',transact)
            print('\t','Balance ',account_details['Balance'])
        else:
            print(">>>>> Account not found.")
        
        print(' >>>>> Thank You >>>>> ') 

    def quit(self):
        print('Thankyou ...')


customers = { }




choices = {1:'Create_account',2:'Display All Customers',3:'Balance',4:'Mini_statement',5:'Withdrawl',6:'Deposit',7:"Quit",8:"Quit"}

while True:
    try:
        user = int(input(' 1 - Create Account \n 2 - Display All Customers   \n 3 - Balance \n 4 - Customer Details \n 5 - Withdrawl \n 6 - Deposit  \n 7 - Mini Statement \n 8 - Quit  \nEnter Your Choice: '))
        print()
        if user in choices:
            new_user = Banking()
            
            if user ==1:
                print('>>> Please Fill the Details to Create a New Account')
                name = input('\t Your Good Name: ').title()
                location = input('\t Your Location: ').title()
                age  = input('\t Your Age: ')
                pan  = input(' \t Your PAN Number: ')
                contact = input('\t Your Contact Number: ')
                new_user.create_account(name,location,age,pan,contact)


            elif user ==2:
                print('>>>>>Display All Customers')
                new_user.display()

            elif user==3:
                print('\t Account Balance')
                acc  = int(input('\t Your Account Number: '))
                new_user.balance(acc)


            elif user==4:
                print('Customer Details')
                acc  = int(input('\t Your Account Number: '))
                new_user.cust_details(acc)


            elif user==5:
                print('Withdrawl')
                acc  = int(input('\t Your Account Number: '))
                withdrawl =  int(input('\t Withdrawl Amount: '))
                new_user.withdrawl(acc,withdrawl)

            elif user==6:
                print('Deposit')
                acc  = int(input('\t Your Account Number: '))
                deposit =  int(input('\t Deposit Amount: '))
                new_user.Deposit(acc,deposit)
            
            elif user==7:
                print('Mini Statement')
                acc  = int(input('\t Your Account Number: '))
                new_user.Mini_statement(acc)


            elif user==8:
                print('Thanks For Visting Our Bank')
                print('Have a nice Day')
                break



                
                
                
            
            
        else:
            print("Please Select a Proper Choice between 1 to 7")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7 only")

            