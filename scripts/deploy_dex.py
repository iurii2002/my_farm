from brownie import UniswapV2Factory, UniswapV2Router02
from brownie import config, network
from scripts.helpful_scripts import get_account, get_contract


def deploy_factory():
    account = get_account()
    factoryV2 = UniswapV2Factory.deploy(account.address, {"from": account},
                                        publish_source=config["networks"][network.show_active()].get(
        "verify", False),
    )

    return factoryV2


def deploy_router(factoryV2):
    account = get_account()
    routerv2 = UniswapV2Router02.deploy(
        factoryV2,
        get_contract("WETH").address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify", False),

    )

    return routerv2


def deploy_dex():
    factory = deploy_factory()
    router = deploy_router(factory.address)
    return factory, router


def main():
    deploy_dex()
    # deploy_router("0x0E20674Cb46b61De19160d0354A88354004cfaC2")
    # deploy_factory()
