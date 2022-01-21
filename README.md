# Brownie Fund Me Project

This is project will enable the learners to understand how to work with Solidity Smart Contract
and Python. It will help the learners to:
- Understand the basics of Solidity Smart Contracts
- Automating tasks with help of Python scripts
- Learn to work with Interface - AggregatorV3Interface and Library - SafeMath
- Get familiar with Ganache - Personal Ethereum Blockchain
- Get familiar with Brownie which is powerful Python based development and testing 
framework for smart contracts
- Perform testing in the development environment, testnet and mainnet(by forking in local PC)
- Learn about forking and mocking test methods
- Verification of Smart Contracts using Etherscan API while working in the testnet
- Use of Ethereum Blockchain API services from Infura and Alchemy

Smart Contracts and Python Scripts: 

- <code>FundMe.sol</code>: Crowdfunding Smart Contract.
- <code>deploy.py</code>: This script allows to deploy the smart contract to the blockchain.
- <code>helpful_scripts.py</code>: This script is created for refactoring purpose.
- <code>fund_and_withdraw.py</code>: This script allows for funding as well as withdrawal of money.
- <code>test_fund_me.py</code>: This script allows to perform various tests.
- <code>MockV3Aggregator.sol</code>: This is the mock Smart Contract for Price Feed to get the price
from Ethereum to USD in the local environment. Basically enables for mocking test.
- <code>brownie-config.yaml</code>: This is the file Brownie looks for while it is running the Python 
script(s). Brownie checks for all custom configurations done by us. 

Watch https://www.youtube.com/watch?v=M576WGiDBdQ from 05:06:35 till 06:03:17 for complete understanding.
Code Author: Patrick Collins
