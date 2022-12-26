from brownie import (
    network,
    accounts,
    config,
    Contract,
    chain,
    MaticWETH,
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add('env')
    # accounts.load('id)
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {"WETH": MaticWETH}


def get_contract(contract_name):
    """This function will grab the contract addresses from the brownie config
    if defined, otherwise, it will deploy a mock version of that contract, and
    return that mock contract.

        Args:
            contract_name (string)

        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed
            version of this contract.
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            # CONTRACT.length = 0 if not deployed already
            deploy_mocks()
        contract = contract_type[-1]
        # Else choose last one
    else:
        contract_address = config["networks"][network.show_active(
        )][contract_name]
        # address
        # ABI
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks():
    account = get_account()
    weth_token = MaticWETH.deploy(account.address, {"from": account})
    print("Deployed!")
    return weth_token


def get_key_from_event(event, _key):
    for key, value in event.items():
        if key == _key:
            return value
