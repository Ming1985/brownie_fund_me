from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scrips import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fund me contract as parametre
    # 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e

    # if on rinkeby, use this address
    # otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS: 
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"contract deployed to {fund_me.address}")
    return fund_me



def main():
    deploy_fund_me()
