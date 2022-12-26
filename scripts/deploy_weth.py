from brownie import config, network, MaticWETH
from scripts.helpful_scripts import get_account


def deploy_WETH():
    account = get_account()
    MaticWETH.deploy(account.address, {"from": account},
                     publish_source=config["networks"][network.show_active()].get(
                         "verify", False),
                     )


def main():
    deploy_WETH()
