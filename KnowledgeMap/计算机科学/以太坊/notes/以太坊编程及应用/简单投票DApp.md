# 简单投票DApp

2022.2.24

## 主要内容

ganache，简单投票DApp

## 教程搬运

### ganache

* [ganache下载](https://trufflesuite.com/ganache/index.html)
* [ganache文档](https://trufflesuite.com/docs/index.html)

### 需求描述

接下来我们要开始真正做一个 DApp，尽管它这是很简单的一个投票应用，但会包含完整的工作流程和交互页面。构建这个应用的主要步骤如下:

* 我们首先安装一个叫做 ```ganache``` 的模拟区块链，能够让我们的程序在开发环境中运行。 
* 写一个合约并部署到 ```ganache``` 上。
* 然后我们会通过命令行和网页与 ```ganache``` 进行交互。

我们与区块链进行通信的方式是通过 RPC(Remote Procedure Call)。 web3js 是一个 JavaScript 库，它抽象出了所有的 RPC 调用，以便于你可以通过 JavaScript 与区块链进行交互。另一个好处是，web3js 能够让你使用你最喜欢的 JavaScript 框架构建非常棒的 web 应用。

### 环境准备

* npm, node

* npm 安装 ganache-cli、web3 和 solc

  ```bash
  npm install web3@0.20.1 --save-dev
  npm install ganache-cli --save-dev
  npm install solc --save-dev
  ```

* 运行ganache

  ```bash
  kimshan@MacBook-Pro simpleVoteDapp % ./node_modules/.bin/ganache-cli       
  Ganache CLI v6.12.2 (ganache-core: 2.13.2)
  
  Available Accounts
  ==================
  (0) 0x6e935Fe1D9100C9e5269965739acf5EEeBC0c825 (100 ETH)
  (1) 0xd89beCa67E54764f8be803f99462bDE33b909c01 (100 ETH)
  (2) 0x9d6CaB0AC8c60B6dD16c51c690A2E7E175c8Db22 (100 ETH)
  (3) 0x1FD2A415b64DaF4e2c0b93DbCE1A7F2356260BD3 (100 ETH)
  (4) 0x9c369361959F8825459A2226C63BBB15Ea9D9AD4 (100 ETH)
  (5) 0xD0069105CD87687C0c35EC9c3bb47aa986078FF7 (100 ETH)
  (6) 0xf3DA6112701ac5D0b03fa4f7e59d518FE5142125 (100 ETH)
  (7) 0xA6760C663eb5366862C1cDA5f154f69E869C30D2 (100 ETH)
  (8) 0x08B597D06ff2c7ccE73440F77641927963C3A2a6 (100 ETH)
  (9) 0xAB34bc3f85f75a858F8ed3213A11A5eAaA94Da33 (100 ETH)
  
  Private Keys
  ==================
  (0) 0x652cf3bacd3e1e360e8e5ed26a3948fc524dd371e8b075423556383489c1ec82
  (1) 0xd3381454c394929292dad9d346fab30ce6a3a091ce74a0d3e002383b69f8c256
  (2) 0xff0d0032a0e4359bef2ce92805f0c63a3a3ef8a00ac6ba167b703362fd3176bf
  (3) 0xbc65b672d553581defc563733a09c6e7265c49975015a5fe27e8bed0a7f11bf9
  (4) 0xa6253723dcc45590f873f89716dca6adfb568798287a41ce5780076d0e147bea
  (5) 0x15f8284d3d4da7782eae65874dae1ef68a5c74279e3492f642182e29d9c69345
  (6) 0x608e2831e7a409669e6c275d0b3027416fd583fee8db17ebf711846d848d4f4c
  (7) 0x67624d355016a9e2f4630ac015419bff2192ceb0182f2b4860f65f6e73bb7a4c
  (8) 0xf681214f7da9986e8c84efd270c38d690947ce302c205423d6c7c499f590cabe
  (9) 0xb2c57cc4be439c221bdd5693d609b64e31ff94b72aef69d1d8ccae07f2d88318
  
  HD Wallet
  ==================
  Mnemonic:      tag logic rhythm trim moon region heavy sea interest wool motor shrimp
  Base HD Path:  m/44'/60'/0'/0/{account_index}
  
  Gas Price
  ==================
  20000000000
  
  Gas Limit
  ==================
  6721975
  
  Call Gas Limit
  ==================
  9007199254740991
  
  Listening on 127.0.0.1:8545
  ```

  为了便于测试，ganache 默认会创建 10 个账户，每个账户有 100 个以太。你需要用其中一个账户创建交易，发送、接收以太。

  当然，你也可以安装 GUI 版本的 ganache 而不是命令行版本，在这里下载 GUI 版本:http://truffleframework.com/ganache/

### Solidity合约

我们会写一个叫做 Voting 的合约，这个合约有以下内容:

* 一个构造函数，用来初始化一些候选者。
* 一个用来投票的方法(对投票数加 1)
* 一个返回候选者所获得的总票数的方法

当你把合约部署到区块链的时候，就会调用构造函数，并只调用一次。与 web 世界里每次部署代码都会覆盖旧代码不同，在区块链上部署的合约是不可改变的，也就是说，如果你更新合约并再次部署，旧的合约仍然会在区块链上存在，并且数据仍在。新的部署将会创建合约的一个新的实例

```solidity
pragma solidity ^0.4.21;
contract Voting{
    mapping (bytes32 => uint8) public votesReceived;
    bytes32[] public candidateList;
    constructor(bytes32[] candidateNames) public {
        candidateList = candidateNames;
    }
    function totalVotesFor(bytes32 candidate) view public returns (uint8) {
        require(validCandidate(candidate));
        return votesReceived[candidate];
    }
    function voteForCandidate(bytes32 candidate) public {
        require(validCandidate(candidate)); 
        votesReceived[candidate] += 1;
    }
    function validCandidate(bytes32 candidate) view public returns (bool) {
        for(uint i = 0; i < candidateList.length; i++) {
            if (candidateList[i] == candidate) {
                return true;
            }
        }
        return false;
    }
}
```

Line 1. 我们必须指定代码将会哪个版本的编译器进行编译

Line 3. mapping 相当于一个关联数组或者是字典，是一个键值对。mapping votesReceived 的键是候选者的名字，类型为 bytes32。mapping 的值是一个 未赋值的整型，存储的是投票数。

Line 4. 在很多编程语言中(例如 java、python 中的字典<HashTable 继承 自字典>)，仅仅通过 votesReceived.keys 就可以获取所有的候选者姓名。但 是，但是在 solidity 中没有这样的方法，所以我们必须单独管理一个候选者数组 candidateList。

Line 14. 注意到 votesReceived[key] 有一个默认值 0，所以你不需要将其 初始化为 0，直接加 1 即可。

你也会注意到每个函数有个可见性说明符(visibility specifier)(比如本例 中的 public)。这意味着，函数可以从合约外调用。如果你不想要其他任何人 调用这个函数，你可以把它设置为私有(private)函数。如果你不指定可见性，

编译器会抛出一个警告。最近 solidity 编译器进行了一些改进，如果用户忘记了 对私有函数进行标记导致了外部可以调用私有函数，编译器会捕获这个问题。

你也会在一些函数上看到一个修饰符 view。它通常用来告诉编译器函数是 只读的(也就是说，调用该函数，区块链状态并不会更新)。

### 编译代码

In the node console

```bash
> var Web3 = require('web3')
> var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
> web3.eth.accounts
['0x5c252a0c0475f9711b56ab160a1999729eccce97'
'0x353d310bed379b2d1df3b727645e200997016ba3']
> code = fs.readFileSync('Voting.sol').toString()
> solc = require('solc')
> compiledCode = solc.compile(code)
```

首先，在终端中运行 node 进入 node 控制台，初始化 web3 对象，并向区块链查询获取所有的账户。

确保与此同时 ganache 已经在另一个窗口中运行为了编译合约，先从 Voting.sol 中加载代码并绑定到一个 string 类型的变 量，然后像右边这样对合约进行编译。

当你成功地编译好合约，打印 compiledCode 对象(直接在 node 控制台 输入 compiledCode 就可以看到内容)，你会注意到有两个重要的字段，它们

很重要，你必须要理解:

1. ```compiledCode.contracts[':Voting'].bytecode```: 这就是 Voting.sol 编译好后的字节码。也是要部署到区块链上的代码。

2. ```compiledCode.contracts[':Voting'].interface```: 这是一个合约的接口或 者说模板(叫做 abi 定义)，它告诉了用户在这个合约里有哪些方法。在未来无论 何时你想要跟任意一个合约进行交互，你都会需要这个 abi 定义。你可以在这里看到 ABI 的更多内容。

在以后的项目中，我们将会使用 truffle 框架来管理编译和与区块链的交互。但是，在使用任何框架之前，深入了解它的工作方式还是大有裨益的，因为框架会将这些内容抽象出去。

### 部署合约

让我们继续课程，现在将合约部署到区块链上。为此，你必须先通过传入 abi 定义来创建一个合约对象 VotingContract。然后用这个对象在链上部署并初始化合约。

Execute this in your node console:

```bash
> abiDefinition =
JSON.parse(compiledCode.contracts[':Voting'].interface) 
> VotingContract = web3.eth.contract(abiDefinition)
> byteCode = compiledCode.contracts[':Voting'].bytecode
> deployedContract = VotingContract.new(['Alice','Bob','Cary'],{data: byteCode, from: web3.eth.accounts[0], gas: 4700000})
> deployedContract.address
'0x0396d2b97871144f75ba9a9c8ae12bf6c019f610'
// Your address will be different
 
> contractInstance = VotingContract.at(deployedContract.address)
```

VotingContract.new 将合约部署到区块链。第一个参数是一个候选者数组，候选者们会竞争选举，这很容易理解。让我 们来看一下第二个参数里面都是些什么:

1. data: 这是我们编译后部署到区块链上的字节码。

2. from: 区块链必须跟踪是谁部署了这个合约。在这种情况下，我们仅仅是

   从调用 web3.eth.accounts 返回的第一个账户，作为部署这个合约的账 户。记住，web3.eth.accounts 返回一个 ganache 所创建 10 个测试账 号的数组。在交易之前，你必须拥有这个账户，并对其解锁。创建一个账 户时，你会被要求输入一个密码，这就是你用来证明你对账户所有权的东 西。在下一节，我们将会进行详细介绍。为了方便起见，ganache 默认 会解锁 10 个账户。

3. gas: 与区块链进行交互需要花费金钱。这笔钱用来付给矿工，因为他们帮你把代码包含了在区块链里面。你必须指定你愿意花费多少钱让你的代 码包含在区块链中，也就是设定 “gas” 的值。你的 “from” 账户里面的 ETH 余额将会被用来购买 gas。gas 的价格由网络设定。

我们已经部署了合约，并有了一个合约实例(变量 contractInstance)，我们可以用这个实例与合约进行交互。

在区块链上有上千个合约。那么，如何识别你的合约已经上链了呢?

答案是找到已部署合约的地址:deployedContract.address. 当你需要跟合约进行交互时，就需要这个部署地址和我们之前谈到的 abi 定义。

### 控制台交互

In your node console:

```bash
> contractInstance.totalVotesFor.call('Rama')
{ [String: '0'] s: 1, e: 0, c: [ 0 ] }
> contractInstance.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
'0xdedc7ae544c3dde74ab5a0b07422c5a51b5240603d31074f5b75c0ebc786bf53'
> contractInstance.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
'0x02c054d238038d68b65d55770fabfca592a5cf6590229ab91bbe7cd72da46de9'
> contractInstance.voteForCandidate('Rama', {from: web3.eth.accounts[0]})
'0x3da069a09577514f2baaa11bc3015a16edf26aad28dffbcd126bde2e71f2b76f'
>
contractInstance.totalVotesFor.call('Rama').toLocaleString()'3'
```

### 为候选者投票并查看投票数

继续课程，在你的 node 控制台里调用 voteForCandidate 和 totalVotesFor 方法并查看结果。

每为一位候选者投一次票，你就会得到一个交易 id,比如: ‘0xdedc7ae544c3dde74ab5a0b07422c5a51b5240603d31074f5b75c0ebc786bf53’。这个交易 id 就是交易发生的凭据，你可以在将来的任何时候引用这 笔交易。这笔交易是不可改变的。

对于以太坊这样的区块链，不可改变是其主要特性之一。在接下来的章节， 我们将会利用这一特性构建应用。

### 网页交互

至此，大部分的工作都已完成，我们还需要做的事情就是创建一个简单的 html，里面有候选者姓名并调用投票命令(我们已经在 nodejs 控制台里试过)。 你可以在右侧找到 html 代码和 js 代码。将它们放到 chapter1 目录，并在浏 览器中打开 index.html。

index.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>Voting DApp</title>
  <link
href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/boot
strap.min.css' rel='stylesheet' type='text/css'>
</head>
<body class="container">
  <h1>A Simple Voting Application</h1>
  <div class="table-responsive">
    <table class="table table-bordered">
  <thead>
    <tr>
     <th>Candidate</th>
     <th>Votes</th>
    </tr>
 </thead>
<tbody>
<tr>
  <td>Alice</td>
  <td id="candidate-1"></td>
</tr>
<tr>
  <td>Bob</td>
  <td id="candidate-2"></td>
</tr> <tr>
  <td>Cary</td>
  <td id="candidate-3"></td>
 
</tr>
     </tbody>
    </table>
  </div>
  <input type="text" id="candidate" />
  <a href="#" onclick="voteForCandidate()" class="btn
btn-primary">Vote</a>
</body>
  
<script
src="https://cdn.jsdelivr.net/gh/ethereum/web3.js/dist/web3.mi
n.js">
</script>
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"> </script>
<script src="./index.js"></script>
</html>
```

Tips:
1. \<head>中用 link 形式引入 bootstrap 的 css 类型库，以下 container、table-responsive 等 class 均来自 bootstrap
2. \<th>表头单元格，\<td>表单元格，候选人名字后的单元格为得票数，用 id 区分以方便写入，之后 js 中写死了对应关系
3. \<input>一个输入框，定义 id 方便在 js 中取值
4. \<a>超链接形式的按键 btn，href=“#”为跳转至本页，即不跳转;onclick指向js 中方法 为了简化项目，我们已经硬编码了候选者姓名。如果你喜欢的话，可以调整代码使其动态选择候选者。

index.js

```js
web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
abi = JSON.parse('[{"constant":false,...}]');
VotingContract = web3.eth.contract(abi);
contractInstance = VotingContract.at('0x329f5c190380ebcf640a90d06eb1db2d68503a53');
candidates = {"Alice": "candidate-1", "Bob": "candidate-2", "Cary": "candidate-3"};

function voteForCandidate(candidate) {
    candidateName = $("#candidate").val();
       try {
           contractInstance.voteForCandidate(candidateName,
                                             {from: web3.eth.accounts[0]},
                                             function() {
             let div_id = candidates[candidateName];
             $("#"+div_id).html(
               contractInstance.totalVotesFor.call(candidateName).toString());
           });
       } catch (err) {
       } 
}
$(document).ready(function() {
  candidateNames = Object.keys(candidates);
  for (var i = 0; i < candidateNames.length; i++) {
    let name = candidateNames[i];
    let val = contractInstance.totalVotesFor.call(name).toString()
    $("#"+candidates[name]).html(val);
  } 
});
```

在第 4 行，用你自己的合约地址替换代码中的合约地址。合约地址是之前 的 deployedContract.address

如果一切顺利的话，你应该能够在文本框中输入候选者姓名，然后投票数应该加 1 。

注意:由于网络原因，web3.js 可能无法获取，可自行下载到本地导入。

如果你可以看到页面，为候选者投票，然后看到投票数增加，那就已经成功 创建了第一个合约，恭喜!所有投票都会保存到区块链上，并且是不可改变的。 任何人都可以独立验证每个候选者获得了多少投票。当然，我们所有的事情都是 在一个模拟的区块链上(ganache)完成，在接下来的课程中，我们会将这个合约部署到真正的公链上。在 Part 2，我们会把合约部署到叫做 Ropsten testnet 的公链，同时也会学习如何使用 truffle 框架构建合约，管理 dapp。

总结一下，下面是你到目前为止已经完成的事情:

1. 通过安装 node, npm 和 ganache，你已经配置好了开发环境。 
2. 你编码了一个简单的投票合约，编译并部署到区块链上。
3. 你通过 nodejs 控制台与网页与合约进行了交互。

## 自己的Dapp

下面展示的是三个主要文件。详细代码已上传

github：https://github.com/CharlesShan-hub/SimpleVoteDapp

视频介绍：https://www.bilibili.com/video/bv1LS4y1k7jv

Voting.sol

```solidity
// SPDX-License-Identifier: SimPL-2.0
pragma solidity ^0.8.0; 
contract Voting {

    // 一位候选人的记录
    struct Candidater{
        string name;
        uint8 id;
        uint8 voteCount;
    }

    // 一场投票
    struct VoteData{
        string voteName;
        Candidater[] candidaters;
    }
    mapping(address => VoteData) GetVoteData;
    
    // 所有场次的投票
    address[] public votings;

    // 管理员
    address managerAddress;
    constructor(){
        managerAddress = msg.sender;
    }
    
    // 清空一场投票
    function clearVoting()public{
        address operaterAddress = msg.sender;
        while(GetVoteData[operaterAddress].candidaters.length!=0){
            GetVoteData[operaterAddress].candidaters.pop();
        }
        for(uint8 i=0; i<votings.length;i++){
            if(votings[i]==operaterAddress){
                delete votings[i];
                break;
            }
        }
    }

    // 清空一场投票
    function clearVotingMan(address operaterAddress)public{
        while(GetVoteData[operaterAddress].candidaters.length!=0){
            GetVoteData[operaterAddress].candidaters.pop();
        }
        for(uint8 i=0; i<votings.length;i++){
            if(votings[i]==operaterAddress){
                delete votings[i];
                break;
            }
        }
    }

    // 设置一场投票
    function setVoting(uint8 _number)public{
        clearVoting();
        address operaterAddress = msg.sender;
        for (uint8 i = 0; i < _number; i++) {
            GetVoteData[operaterAddress].candidaters.push(Candidater({
                name: "default name",
                id: i,
                voteCount: 0
            }));
        }
        votings.push(operaterAddress);
    }

    // 获取自己的投票活动的列表长度
    function getMyLength()public view returns(uint){
        return GetVoteData[msg.sender].candidaters.length;
    }

    // 获取某投票活动的列表长度
    function getLength(address voteAddress)public view returns(uint){
        return GetVoteData[voteAddress].candidaters.length;
    }

    // 设置竞选者名字
    function setName(uint8 _id, string memory _name) public{
        for(uint i = 0; i < getMyLength(); i++) {
            if (GetVoteData[msg.sender].candidaters[i].id == _id) {
                GetVoteData[msg.sender].candidaters[i].name=_name;
            }
        }
    }

    // 设置竞选者名字(管理员)
    function setNameMan(uint8 _id, string memory _name,address opAddress) public{
        require(msg.sender==managerAddress);
        for(uint i = 0; i < getLength(opAddress); i++) {
            if (GetVoteData[opAddress].candidaters[i].id == _id) {
                GetVoteData[opAddress].candidaters[i].name=_name;
            }
        }
    }

    // 获取竞选者名字
    function getNameSelf(uint8 _id) view public returns(string memory){
        for(uint i = 0; i < getMyLength(); i++) {
            if (GetVoteData[msg.sender].candidaters[i].id == _id) {
                return GetVoteData[msg.sender].candidaters[i].name;
            }
        }
        return "";
    }

    // 获取竞选者名字
    function getName(uint8 _id,address voteSetter) view public returns(string memory){
        for(uint i = 0; i < getLength(voteSetter); i++) {
            if (GetVoteData[voteSetter].candidaters[i].id == _id) {
                return GetVoteData[voteSetter].candidaters[i].name;
            }
        }
        return "";
    }

    // 查看票数
    function totalVotesFor(uint8 candidate,address opAddress) view public returns (uint8) {
        for(uint i = 0; i < getLength(opAddress); i++) {
            if (GetVoteData[opAddress].candidaters[i].id == candidate) {
                return GetVoteData[opAddress].candidaters[i].voteCount;
            }
        }
        return 0;
    }

    // 获取全套参数
    function totalVoteInfo(uint8 candidate,address opAddress) view public returns (uint8,string memory,uint8) {
        for(uint i = 0; i < getLength(opAddress); i++) {
            if (GetVoteData[opAddress].candidaters[i].id == candidate) {
                return (GetVoteData[opAddress].candidaters[i].id, GetVoteData[opAddress].candidaters[i].name, GetVoteData[opAddress].candidaters[i].voteCount);
            }
        }
        return (0,"",0);
    }

    // 投票
    function voteForCandidate(uint8 candidate,address opAddress) public{
        for(uint i = 0; i < getLength(opAddress); i++) {
            if (GetVoteData[opAddress].candidaters[i].id == candidate) {
                GetVoteData[opAddress].candidaters[i].voteCount+=1;
            }
        }
    }

    // 获取总票场
    function getVotingsNumber() view public returns(uint){
        return votings.length;
    }

    // 获取总票场
    function getVotingsAddress(uint8 number) view public returns(address){
        // 0x0000000000000000000000000000000000000000
        return votings[number];//被删除的场次返回值为0x0000..00
    }
}
```

main.js

```js
//0x75Ff5F62085E14713FFFA2E13a1B8Ddd455a1eC3
//0xbb4e3e33b7dfd4b1c44173638546941ed1bb611e

var CONTRACT = "0x38801Fea804E25f63d97Bd91788856cFF10C4800";

//var Web3 = require('web3');

var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));

function getInstance(){
	var abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"clearVoting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operaterAddress","type":"address"}],"name":"clearVotingMan","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"voteAddress","type":"address"}],"name":"getLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMyLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"_id","type":"uint8"},{"internalType":"address","name":"voteSetter","type":"address"}],"name":"getName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"_id","type":"uint8"}],"name":"getNameSelf","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"number","type":"uint8"}],"name":"getVotingsAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getVotingsNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"_id","type":"uint8"},{"internalType":"string","name":"_name","type":"string"}],"name":"setName","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"_id","type":"uint8"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"address","name":"opAddress","type":"address"}],"name":"setNameMan","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"_number","type":"uint8"}],"name":"setVoting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"candidate","type":"uint8"},{"internalType":"address","name":"opAddress","type":"address"}],"name":"totalVoteInfo","outputs":[{"internalType":"uint8","name":"","type":"uint8"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"candidate","type":"uint8"},{"internalType":"address","name":"opAddress","type":"address"}],"name":"totalVotesFor","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"candidate","type":"uint8"},{"internalType":"address","name":"opAddress","type":"address"}],"name":"voteForCandidate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"votings","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]';
	var CoinContract = new web3.eth.Contract(JSON.parse(abi),CONTRACT);
	return CoinContract;
}

function initiate(){
	if(web3.eth.net.isListening()==false){
		alert("网络连接失败");
		return;
	}

	// 获取投票人,投票名单
	var address = document.getElementById('UserAddress').value;
	//0x75Ff5F62085E14713FFFA2E13a1B8Ddd455a1eC3
	var nameList = document.getElementById('NameList').value.split(',');
	//Charles Shan, Kim Shan, Hongtian Shan
	for (var i=0;i<nameList.length;i++){ 
		nameList[i] = nameList[i].replace(/^\s*|\s*$/g,"");
	}
	// 密码
	var password = document.getElementById('UserPassword').value;
	
	// 发起新投票
	var contractInstance=getInstance();
	web3.eth.personal.unlockAccount(address,password, (err,res)=>{
		if(err){
			console.log("Error: ",err);
			alert("Fail to Auth Accounts");
		}else{
			console.log("Result: ",res);
			contractInstance.methods.setVoting(nameList.length).send({from:address}, 
				function(error, transactionHash){
					if(error){
						console.log("Error: ",error);
					}else{
						console.log("Result: ",transactionHash);
						// 设置姓名
						for (var i=0;i<nameList.length;i++){ 
							contractInstance.methods.setName(i,nameList[i]).send({from:address}, 
								function(error, transactionHash){
									if(error){
										console.log("Error: ",error);
									}else{
										console.log("Result: ",transactionHash);
									}
								}
							);
						}
						alert("成功发起一场投票");
					}
				}
			);
		}
	});
}

function vote(){
	if(web3.eth.net.isListening()==false){
		alert("网络连接失败");
		return;
	}

	// 获取投票人,投票名单
	var address = document.getElementById('UserAddress').value;
	// 投票场所地址
	var addressv = document.getElementById('VoteGame').value;
	if(addressv=="Select"){
		return;
	}
	//0x75Ff5F62085E14713FFFA2E13a1B8Ddd455a1eC3
	var voteID = document.getElementById('VoteID').value;
	// 密码
	var password = document.getElementById('UserPassword').value;
	
	// 进行投票
	var contractInstance=getInstance();
	web3.eth.personal.unlockAccount(address,password, (err,res)=>{
		if(err){
			console.log("Error: ",err);
			alert("Fail to Auth Accounts");
		}else{
			console.log("Result: ",res);
			contractInstance.methods.voteForCandidate(voteID,addressv).send({from:address}, 
				function(error, transactionHash){
					if(error){
						console.log("Error: ",error);
					}else{
						console.log("Result: ",transactionHash);
						alert("成功进行一场投票");
					}
				}
			);
		}
	});
}

function refresh(){
	if(web3.eth.net.isListening()==false){
		alert("网络连接失败");
		return;
	}

	// 获取操作人
	var address = document.getElementById('UserAddress').value;
	// 投票场所地址
	var addressv = document.getElementById('VoteGame').value;
	if(addressv=="Select"){
		return;
	}

	// 清理列表
	document.getElementById('TableBody').innerHTML="";

	// 获取投票数据
	var contractInstance=getInstance();
	contractInstance.methods.getLength(addressv).call({from: address}, 
		function(error, result){
			if(error){
				console.log("Error: ",error);
			}else{
				console.log("Member Number: ",result);
				for(var num = 0;num<result;num++){
					contractInstance.methods.totalVoteInfo(num,addressv).call({from: address}, 
					function(error, result){
						if(error){
							console.log("Error: ",error);
						}else{
							var tableBody = document.getElementById('TableBody').innerHTML;
							document.getElementById('TableBody').innerHTML = tableBody+"<tr><th scope=\"row\">"+result[0]+"</th><td>"+result[1]+"</td><td>"+result[2]+"</td></tr>\n";
						}
					});
				}
			}	
		}
	);
}

function getGames(){
	if(web3.eth.net.isListening()==false){
		alert("网络连接失败");
		return;
	}

	// 获取操作人
	var address = document.getElementById('UserAddress').value;

	// 清空列表
	document.getElementById('VoteGame').innerHTML="<option>Select</option>\n";
	
	// 获取投票场次数据
	var contractInstance=getInstance();
	contractInstance.methods.getVotingsNumber().call({from: address}, 
		function(error, result){
			if(error){
				console.log("Error: ",error);
			}else{
				console.log("Games Number: ",result);
				for(var num = 0;num<result;num++){
					contractInstance.methods.getVotingsAddress(num).call({from: address}, 
					function(error, result){
						if(error){
							console.log("Error: ",error);
						}else{
							if(result!='0x0000000000000000000000000000000000000000'){
								var content = document.getElementById('VoteGame').innerHTML;
								document.getElementById('VoteGame').innerHTML = content+"<option>"+result+"</option>\n";
							}
						}
					});
				}
			}	
		}
	);
	

}

function init(){
	//getGames();
}
```

index.html

```html
<!doctype html>
<html lang="en">

    <head>
        <meta charset="utf-8" />
        <title>Basic Tables | Veltrix - Responsive Bootstrap 4 Admin Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta content="Premium Multipurpose Admin & Dashboard Template" name="description" />
        <meta content="Themesbrand" name="author" />

        <!-- Bootstrap Css -->
        <link href="assets/css/bootstrap.min.css" id="bootstrap-style" rel="stylesheet" type="text/css" />
        <!-- App Css-->
        <link href="assets/css/app.min.css" id="app-style" rel="stylesheet" type="text/css" />

    </head>

    <body data-topbar="dark" data-layout="horizontal" onload='init()'>

        <!-- Begin page -->
        <div id="layout-wrapper">

            <header id="page-topbar">
            	<br><br>
            </header>

            <!-- ============================================================== -->
            <!-- Start right Content here -->
            <!-- ============================================================== -->
            <div class="main-content">

                <div class="page-content">
                    <div class="container-fluid">

                        <!-- start page title -->
                        <div class="row align-items-center">
                            <div class="col-sm-6">
                                <div class="page-title-box">
                                    <h4 class="font-size-18">Simple Vote Dapp</h4>
                                </div>
                            </div>
                        </div>     
                        <!-- end page title -->
                        <div class="row">
                        	<div class="col-lg-6">
                        		<div class="col-lg-12">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title">Vote</h4>
                                        <p class="card-title-desc">Fill in your account ID and the name of the candidate you support (on the right).</p> 

                                        <!--Voter Will-->
                                        <div class="inner-repeater mb-4">
                                            <div data-repeater-list="inner-group" class="inner form-group">
                                                <label>ID of Candidate You Vote:</label>
                                                <div data-repeater-item class="inner mb-3 row">
                                                    <div class="col-md-10 col-8">
                                                        <input type="text" class="inner form-control" placeholder="A Number, eg. 0,1,2,3" id="VoteID"/>
                                                    </div>
                                                    <!--<div class="col-md-2 col-4">
                                                        <input data-repeater-delete type="button" class="btn btn-primary btn-block inner" value="Delete"/>
                                                    </div>-->
                                                </div>
                                            </div>
                                        </div>


                                        <input data-repeater-create type="button" class="btn btn-success mo-mt-2" value="Vote" onclick="vote()"/>
                                    </div>
                                </div>
                            </div>
                            <br>
                            <div class="col-lg-12">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title">Build</h4>
                                        <p class="card-title-desc">Call a vote.</p> 

                                        <!--Voter Will-->
                                        <div class="inner-repeater mb-4">
                                            <div data-repeater-list="inner-group" class="inner form-group">
                                                <label>Name of Candidate to Vote:</label>
                                                <div data-repeater-item class="inner mb-3 row">
                                                    <div class="col-md-10 col-8">
                                                        <textarea id="NameList" class="form-control" placeholder="Charles Shan, Amanda Green, Jay Chou, ..."></textarea>
                                                        <!--<input type="text" class="inner form-control" placeholder="Charles Shan, Amanda Green, Jay Chou, ..."/>-->
                                                    </div>
                                                    <!--<div class="col-md-2 col-4">
                                                        <input data-repeater-delete type="button" class="btn btn-primary btn-block inner" value="Delete"/>
                                                    </div>-->
                                                </div>
                                            </div>
                                        </div>


                                        <input data-repeater-create type="button" class="btn btn-success mo-mt-2" value="Initiate" onclick="initiate()" />
                                    </div>
                                </div>
                            </div>
                        	</div>
                        	<div class="col-lg-6">
	                            <div class="col-lg-12">
	                                <div class="card">
	                                    <div class="card-body">
	                                        <h4 class="card-title">Candidate Rankings Table</h4>
	                                        <p class="card-title-desc">Names of all candidates and the number of votes received.</p>    
	                                        
	                                        <div class="table-responsive">
	                                            <table class="table table-bordered mb-0">
	                                                <thead>
	                                                    <tr>
	                                                        <th>ID</th>
	                                                        <th>Name</th>
	                                                        <th>Number</th>
	                                                    </tr>
	                                                </thead>
	                                                <tbody id="TableBody">
	                                                </tbody>
	                                            </table>
	                                        </div>

	                                        <form>
	                                        	<br>
	                                            <div class="form-group">
	                                                <label class="control-label">Vote Account:</label>
	                                                <select class="form-control select2" id="VoteGame">
	                                                    <option>Select</option>
	                                                </select>
	                                            </div>
	                                        </form>

	                                    <!--Voting Game Choose-->
	                                    <div class="inner-repeater mb-4">
	                                    	<input data-repeater-create type="button" class="btn btn-success mo-mt-2" value="GetGames" onclick="getGames()" />
	                                        <input data-repeater-create type="button" class="btn btn-success mo-mt-2" value="Refresh" onclick="refresh()" />
	                                    </div>

	                                    </div>
	                                </div>
	                            </div>
	                            <div class="col-lg-12">
	                                <div class="card">
	                                    <div class="card-body">
	                                        <h4 class="card-title">Who Are You</h4>
	                                        <p class="card-title-desc">Input your Address.</p> 
	                                        <!--Voter Account-->
	                                        <div class="inner-repeater mb-4">
	                                            <div data-repeater-list="inner-group" class="inner form-group">
	                                                <label>Your Address:</label>
	                                                <div data-repeater-item class="inner mb-3 row">
	                                                    <div class="col-md-10 col-8">
	                                                        <input id="UserAddress" type="text" class="inner form-control" placeholder="Enter your account 0x.."/>
	                                                    </div>
	                                                </div>
	                                            </div>
	                                        </div>
	                                        <!--Voter Account-->
	                                        <div class="inner-repeater mb-4">
	                                            <div data-repeater-list="inner-group" class="inner form-group">
	                                                <label>Your Password:</label>
	                                                <div data-repeater-item class="inner mb-3 row">
	                                                    <div class="col-md-10 col-8">
	                                                        <input id="UserPassword" type="password" class="inner form-control" placeholder="Enter your password"/>
	                                                    </div>
	                                                </div>
	                                            </div>
	                                        </div>
	                                    </div>
	                                </div>
	                            </div>
                        	</div>
                        </div>
                        <!-- end row -->

                    </div> <!-- container-fluid -->
                </div>
                <!-- End Page-content -->

                
                
                <footer class="footer">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-12">
                                © <script>document.write(new Date().getFullYear())</script> Simple Vote Dapp<span class="d-none d-sm-inline-block"> - Crafted with <i class="mdi mdi-heart text-danger"></i> by Charles Shan.</span>
                            </div>
                        </div>
                    </div>
                </footer>

            </div>
            <!-- end main content-->

        </div>
        <!-- END layout-wrapper -->

        <!-- JAVASCRIPT -->
        <script src="assets/libs/jquery/jquery.min.js"></script>
        <script src="assets/libs/bootstrap/js/bootstrap.bundle.min.js"></script>
        <script src="assets/libs/metismenu/metisMenu.min.js"></script>
        <script src="assets/libs/simplebar/simplebar.min.js"></script>
        <script src="assets/libs/node-waves/waves.min.js"></script>

        <script src="assets/js/app.js"></script>
        <!--<script src="https://cdn.jsdelivr.net/gh/ethereum/web3.js/dist/web3.min.js"></script>-->
        <script src="web3.min.js"></script>
        <script src="main.js"></script>

    </body>
</html>

```

