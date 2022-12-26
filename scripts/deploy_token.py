from brownie import Token, config, network
from scripts.helpful_scripts import get_account


def deploy_token():
    return Token.deploy(
        1e21,
        "Test Token",
        "Test",
        {"from": get_account()},
        publish_source=config["networks"][network.show_active()].get(
            "verify", False),
    )


def main():
    deploy_token()
