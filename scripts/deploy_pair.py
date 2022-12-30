from brownie import UniswapV2Pair
from brownie import config, network
from scripts.helpful_scripts import get_account, get_contract


def deploy_pair():
    account = get_account()
    pair = UniswapV2Pair.deploy({"from": account},
                                publish_source=config["networks"][network.show_active()].get(
        "verify", False),
    )
    pair.tx.wait(1)
    return pair


def main():
    deploy_pair()
