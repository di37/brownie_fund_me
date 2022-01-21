from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    # Now the variable FundMe is just array which holds the addresses of the nodes
    # In the network blockchain where the Smart Contract 0 FundMe.sol got deployed
    fund_me = FundMe[-1]
    account = get_account()

    # Obtaining the Entrance Fee
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is: {entrance_fee}")

    # Updating the already created contract 
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    # Returning the money to the account from which money was funded
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
