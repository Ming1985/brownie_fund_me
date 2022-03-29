from scripts.helpful_scrips import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network, accounts, exceptions
from scripts.deploy import deploy_fund_me
import pytest

# 测试合约是否可以进行fund和withdraw操作
def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100 
    # 执行合约的fund函数. 等待结果
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # assert 判断地址的付款是否被保存到array, 是否等于entrancefee
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    # 执行合约的withdraw函数 等待结果 判断array中最终的余额是否为0
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

# 测试onlyOwner
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # 如果不是本地网络, 跳过这个测试
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})