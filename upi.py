class upi_transaction:
    # Arguments for construction?
    def __init__(self,sender_handle, receiver_handle, amounts):
            # Create a UUID
            self.transaction_id = 'Some_random generated stuff'
            # self.sender_handle =self.sender_handle
            # self.receiver_handle = self.receiver_handle
            # self.amounts = amounts  

class upi_payment_transaction(upi_transaction):
    # Arguments for construction?
    # Pass the responsibilty to UPI Transaction
    def __init__(self,sender_handle, receiver_handle, amounts):
        super().__init__()

class upi_receipt_transaction(upi_transaction):
    # Arguments for construction?
    def __init__(self,sender_handle, receiver_handle, amounts):
            super().__init__()


class upi_transaction_response:
     def __init__(self):
          pass

def create_handle(user_id:str,bank_id:str):
    return (user_id,bank_id) 

def read_user_id(upi_handle:tuple):
    return upi_handle[0]

def read_bank_id(upi_handle:tuple):
    return upi_handle[1]

def test_compare(handle1 ,handle2):
    return handle1[0]==handle2[0] and handle1[1] == handle2[1]

def main():
    user1 = create_handle("3635635764","sbi")
    # print(read_user_id(user1))
    # print(read_bank_id(user1))
    user2 = create_handle("3635635764","sbi")
    assert test_compare(user1,user2)
    
main()


# Practice Assignment - Create a dictionary of UPI Handles
# Key must be phone no. or account number tuple as value
# Store amount as well using a function