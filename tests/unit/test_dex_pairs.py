import pytest
from scripts.helpful_scripts import get_account
from scripts.deploy_dex import deploy_dex
from scripts.deploy_tokens import deploy_token
from brownie import reverts

@pytest.fixture
def dex_contracts():
    return deploy_dex()

def test_create_pair(dex_contracts):
    factoryV2, v2erc20, routerv2 = dex_contracts
    current_pairs_amount = factoryV2.allPairsLength()
    assert current_pairs_amount == 0
    token1 = deploy_token()
    token2 = deploy_token()
    factoryV2.createPair(token1.address, token2.address)
    current_pairs_amount = factoryV2.allPairsLength()
    assert current_pairs_amount == 1