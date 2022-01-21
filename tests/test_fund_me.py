from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    # Arrange
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100

    # Act
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    
    # Assert
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    # Act
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    
    # Assert
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    # To perform test only in local development not in testnet
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")

    # Act
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()

    # Arrange and Assert. In this case, it is raising exception.
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})

