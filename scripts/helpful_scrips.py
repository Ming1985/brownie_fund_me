from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):  # 如果是开发者网络, 则返回虚拟账户
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])  # 否则获取yaml中账户


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("Deploying mocks")
    if len(MockV3Aggregator) <= 0:
        print("the current build is", len(MockV3Aggregator))
        mocks_aggregator = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()}
        )
    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks deployed!")
