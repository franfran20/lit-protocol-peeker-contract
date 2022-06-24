// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Peek {
    error Peek__YouCantEvenPeek();

    mapping(address => bool) public isAllowedToPeek;

    function allowMeToPeek() public {
        //ususally thered be a condition for being allowed to pick
        //say pay 1 eth or hold a certain amount of tokens or specific NFT
        isAllowedToPeek[msg.sender] = true;
    }

    function disallowMeFromPeeking() public {
        if (isAllowedToPeek[msg.sender] == false) {
            revert Peek__YouCantEvenPeek();
        }
        isAllowedToPeek[msg.sender] = false;
    }

    function amIAllowedToPeek(address _peeker) public view returns (bool) {
        if (isAllowedToPeek[_peeker]) {
            return true;
        } else {
            return false;
        }
    }
}
