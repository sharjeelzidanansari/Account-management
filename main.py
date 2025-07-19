from validation import login
from account_logic import  withdraw, deposit, check_balance 
def main():
  while True:
    print("***Welcome to ABC Bank***")
    login()
    choice=input("Enter the choice (1/2/3):")
    if choice=='1':
        deposit()
        break
    elif choice=='2':
        withdraw()
        break
    elif choice=='3':
        check_balance()
        break
    else:
        print("Wrong option selected. Try again")
        
if __name__=='__main__':
   main()
