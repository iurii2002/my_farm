// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    constructor(uint256 initialSupply, string memory Name, string memory Ticker) ERC20(Name, Ticker) public {
        _mint(msg.sender, initialSupply);
    }
}
