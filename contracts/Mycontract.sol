// SPDX-License-Identifier: MIT 

pragma solidity >=0.7.0 <0.9.0;

contract Mycontract{
    //นิยามตัวแปร
    //type access_modifiler name;
    string private _name;
    uint private  _balance;
    constructor (string  memory name,uint balance){
        require(balance<0,"You balance is 0");
        _name =  name;
        _balance = balance;
    }
    function changeName(string memory name) public {
        _name = name;
    }
    function getname() public view returns(string memory){
        return  _name; 
    }
}