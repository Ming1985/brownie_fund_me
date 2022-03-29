from brownie import FundMe
from scripts.helpful_scrips import get_account

# 执行fund函数
# contract.function({"from":address, "value": xx}) 执行一个transaction
def fund():
    fund_me = FundMe[-1] # the latest deployed contract
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() # returns the minimal fund fee
    print(fund_me.getPrice())   
    print("The current Entrence fee is " ,entrance_fee)
    print("Funding")
    fund_me.fund({ "from":account, "value": entrance_fee })
    
def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    

def main():
    fund()
    withdraw()