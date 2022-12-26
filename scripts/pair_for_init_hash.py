# solidity code

# // calculates the CREATE2 address for a pair without making any external calls
# function pairFor(address factory, address tokenA, address tokenB) internal pure returns (address pair) {
#     (address token0, address token1) = sortTokens(tokenA, tokenB);
#     pair = address(uint(keccak256(abi.encodePacked(
#             hex'ff',
#             factory,
#             keccak256(abi.encodePacked(token0, token1)),
#             hex'96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f' // init code hash
#         ))));
# }

# input1 - 0x1dfc378641f06f4095e9434017bf335018550c55
# input2 - 0xee01c0cd76354c383b8c7b4e65ea88d00b06f36f
# output - 0x3684B4465D589660d95965ffCAFf4F9e203cbED7


def sort_token(token1, token2):
    return (token1, token2) if token1 < token2 else (token2, token1)


input1 = "0x1dfc378641f06f4095e9434017bf335018550c55"
input2 = "0xee01c0cd76354c383b8c7b4e65ea88d00b06f36f"
factory = "0xf17CC3a7f779F8cF78bA89aE08961bD972C3a177"

print(sort_token(input1, input2))
