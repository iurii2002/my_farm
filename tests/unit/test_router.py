import pytest
from web3 import Web3
from scripts.helpful_scripts import get_account, get_key_from_event
from scripts.deploy_dex import deploy_dex
from scripts.deploy_token import deploy_token
from brownie import reverts, interface


@pytest.fixture
def dex_contracts():
    return deploy_dex()


# @pytest.fixture
# def create_pair(dex_contracts):
#     factoryV2, routerv2 = dex_contracts
#     account = get_account()
#     token1 = deploy_token()
#     token2 = deploy_token()
#     create_pair_tx = factoryV2.createPair(
#         token1.address, token2.address, {"from": account})
#     create_pair_tx.wait(1)
#     pair_adr = factoryV2.getPair(token1, token2)
#     return pair_adr, routerv2


@pytest.fixture
def create_tokens():
    token1 = deploy_token()
    token2 = deploy_token()
    token3 = deploy_token()
    token4 = deploy_token()
    return token1, token2, token3, token4


def test_add_liquidity(dex_contracts, create_tokens):
    factoryV2, routerv2 = dex_contracts
    token1, token2, token3, token4 = create_tokens
    account = get_account()
    router = interface.IUniswapV2Router01(routerv2)
    factory = interface.IUniswapV2Factory(factoryV2)
    create_pair_tx = factoryV2.createPair(
        token1.address, token2.address, {"from": account})
    create_pair_tx.wait(1)

    # web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

    # latest_block = web3.eth.getBlock('latest')
    # print(latest_block)
    # deadline = web3.eth.get_block(latest_block).timestamp + 10000
    # print(deadline)

    appr1 = token1.approve(router.address, 3 * (10 ** 18), {"from": account})
    appr1.wait(1)
    appr2 = token2.approve(router.address, 3 * (10 ** 18), {"from": account})
    appr2.wait(1)

    pair = factory.getPair(token1.address, token2.address)

    print(factory.getPair(token1.address, token2.address))
    print(router.factory())
    print(factory.address)
    print(router.WETH())
    print(token1.address)
    print(token2.address)

    amount = 2 * (10 ** 18)
    print(token1.address, token2.address, amount, amount, amount *
          0.995, amount*0.995, account.address, 1771700001563)
    add_liquidity_tx = router.addLiquidity(
        token1.address, token2.address, amount, amount, amount*0.995, amount*0.995, account.address, 1771700001563, {"from": account})
    add_liquidity_tx.wait(1)

    assert 1 == 0


# function
# - addLiquidity
# - addLiquidityETH
# - removeLiquidity
# - removeLiquidityETH
# - removeLiquidityWithPermit
# - removeLiquidityETHWithPermit
# - removeLiquidityETHSupportingFeeOnTransferTokens
# - removeLiquidityETHWithPermitSupportingFeeOnTransferTokens
# - swapExactTokensForTokens
# - swapTokensForExactTokens
# - swapExactETHForTokens
# - swapTokensForExactETH
# - swapExactTokensForETH
# - swapETHForExactTokens
# - swapExactTokensForTokensSupportingFeeOnTransferTokens
# - swapExactETHForTokensSupportingFeeOnTransferTokens
# - swapExactTokensForETHSupportingFeeOnTransferTokens

# - quote
# - getAmountOut
# - getAmountIn
# - getAmountsOut
# - getAmountsIn
