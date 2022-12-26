import pytest
from scripts.helpful_scripts import get_account
from scripts.deploy_dex import deploy_dex
from scripts.deploy_tokens import deploy_token
from brownie import reverts


@pytest.fixture
def dex_contracts():
    return deploy_dex()


def test_create_pair(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    account = get_account()
    current_pairs_amount = factoryV2.allPairsLength({"from": account})
    assert current_pairs_amount == 0
    token1 = deploy_token()
    token2 = deploy_token()
    create_pair_tx = factoryV2.createPair(
        token1.address, token2.address, {"from": account})
    create_pair_tx.wait(1)
    current_pairs_amount = factoryV2.allPairsLength({"from": account})
    assert current_pairs_amount == 1


def test_could_not_create_pair_twice(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    account = get_account()
    token1 = deploy_token()
    token2 = deploy_token()
    create_pair_tx = factoryV2.createPair(
        token1.address, token2.address, {"from": account})
    create_pair_tx.wait(1)
    with reverts("UniswapV2: PAIR_EXISTS"):
        create_pair_tx = factoryV2.createPair(
            token1.address, token2.address, {"from": account})
        create_pair_tx.wait(1)


def test_could_not_create_same_token_pair(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    account = get_account()
    token1 = deploy_token()
    with reverts("UniswapV2: IDENTICAL_ADDRESSES"):
        create_pair_tx = factoryV2.createPair(
            token1.address, token1.address, {"from": account})
        create_pair_tx.wait(1)


def test_set_feeToSetter(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    account = get_account()
    current_fee_to_setter = factoryV2.feeToSetter({"from": account})
    assert current_fee_to_setter == get_account()
    new_account = get_account(index=2)
    setFeeToSetter_tx = factoryV2.setFeeToSetter(
        new_account, {"from": account})
    setFeeToSetter_tx.wait(1)
    current_fee_to_setter = factoryV2.feeToSetter({"from": account})
    assert current_fee_to_setter == new_account


def test_only_feeToSetter_can_change_feeToSetter(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    new_account = get_account(index=2)
    current_fee_to_setter = factoryV2.feeToSetter({"from": new_account})
    assert current_fee_to_setter != new_account
    with reverts("UniswapV2: FORBIDDEN"):
        setFeeToSetter_tx = factoryV2.setFeeToSetter(
            new_account, {"from": new_account})
        setFeeToSetter_tx.wait(1)


def test_change_feeTo(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    account = get_account()
    old_fee_to = factoryV2.feeTo({"from": account})
    new_fee_to_account = get_account(index=5)
    assert old_fee_to != new_fee_to_account
    setFeeTo_tx = factoryV2.setFeeTo(new_fee_to_account, {"from": account})
    setFeeTo_tx.wait(1)
    new_fee_to = factoryV2.feeTo({"from": account})
    assert new_fee_to_account == new_fee_to


def test_only_feeToSetter_can_change_feeTo(dex_contracts):
    factoryV2, routerv2 = dex_contracts
    new_account = get_account(index=5)
    current_fee_to_setter = factoryV2.feeTo({"from": new_account})
    assert current_fee_to_setter != new_account
    with reverts("UniswapV2: FORBIDDEN"):
        setFeeTo_tx = factoryV2.setFeeTo(new_account, {"from": new_account})
        setFeeTo_tx.wait(1)
