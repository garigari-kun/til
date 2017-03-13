'''

Encapsulation

When you listen to the radio or watch the TV, you will almost certaninly press numberical buttons to turn to the channel you wish to listen to view.
BUT you(the user) does not need to be convered with the actual frequence value, you just press a button and the technical stuff happens in the background.



'''



class BankAccount(object):
    ''' This is a bank account classs '''

    def __init__(self, account_name='Current Account', balance=200):
        self.__account_name = account_name
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)

    def set_balance_withdraw(self, value):
        if value < self.__balance:
            self.__balance = self.__balance - value
            print('New balance: {}'.format(self.__balance))
        else:
            print('You do not have enough funds!')




account_object = BankAccount()
while True:
    print('1: Check the balance')
    print('2: Withdraw funds')

    menu_option = int(input())

    if menu_option == 1:
        account_object.get_balance()
    elif menu_option == 2:
        value = int(input('How much would you like to widhdraw: '))
        account_object.set_balance_withdraw(value)
    else:
        print("Wrong menu choice")
