# acc_number:int
acc_number=0
acc_name:str
type:str

def bankdata():
    
    global acc_number,acc_name,type
    
    acc_number=input("Enter Your Account Number: ")
    acc_name=input("Enter Your Account Name: ")
    acc_type=input("Enter Your Account Type: \n enter 1 for current- \n entr 2 for saving- ")
    # total_ammount=input("Total")
    
    if acc_type == 1:
        type="current"
    elif acc_type == 2:
        type="saving"
    else : 
        type="none"

def statement():
    
        print("your account number",acc_number)
        
        
bankdata()

statement()