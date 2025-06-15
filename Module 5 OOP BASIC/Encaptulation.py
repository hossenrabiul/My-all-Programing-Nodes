# Encaptulation --> hide details
# access modifier --> public, protect, private
class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name    # public attricute
        self.balance = initial_deposit
        self._branch = 'banani 11' # protected
        self.__balance = initial_deposit  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdrwa(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'fokir tak nai'
        
rapsun = Bank('chotoo vai', 5000)
print(rapsun.holder_name)
# rapsun.balance = 0
# print(rapsun.__balance)
rapsun.deposit(40000)
print(rapsun.get_balance())
rapsun.holder_name = 'voro vai'
print(rapsun.holder_name)
# print(rapsun.withdrwa(40000))
# print(rapsun.get_balance()) 
# print(dir(rapsun))
print(rapsun._Bank__balance)