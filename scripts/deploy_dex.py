from brownie import UniswapV2Factory, UniswapV2ERC20, UniswapV2Router02
from brownie import config, network
from scripts.helpful_scripts import get_account, get_contract


def deploy_dex():
    account = get_account()
    factoryV2 = UniswapV2Factory.deploy(account.address, {"from": account})
    v2erc20 = UniswapV2ERC20.deploy({"from": account})
    routerv2 = UniswapV2Router02.deploy(
        factoryV2.address,
        get_contract("WETH").address,
    )

    return factoryV2, v2erc20, routerv2


def main():
    deploy_dex()
