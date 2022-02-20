# Solidity进阶

2022.2.20

## 主要内容

Solidity语法

## [Solidity源文件布局](https://solidity-cn.readthedocs.io/zh/develop/layout-of-source-files.html)

* **pragma (版本杂注)**

  * 源文件可以被版本杂注pragma所注解，表明要求的编译器版本
  * 例如:```pragma solidity ^0.4.0;```
  * 源文件将既不允许低于 0.4.0 版本的编译器编译，也不允许高于(包含) 0.5.0 版本的编译器编译(第二个条件因 使用 ^ 被添加)

* **import(导入其它源文件)**

  * Solidity 所支持的导入语句import，语法同 JavaScript(从 ES6 起)非常类似

  * ```import "filename";```

    从“filename”中导入所有的全局符号到当前全局作用域中

  * ```import * as symbolName from "filename";```

    创建一个新的全局符号 symbolName，其成员均来自 “filename” 中全局符号

  * ```import {symbol1 as alias, symbol2} from "filename";```
    创建新的全局符号alias和symbol2，分别从"filename"引用 symbol1 和 symbol2

  * ```import "filename" as symbolName;```
    这条语句等同于 import * as symbolName from "filename";

## [Solidity值类型](https://solidity-cn.readthedocs.io/zh/develop/types.html)

* **布尔(bool)**:可能的取值为字符常量值 true 或 false

- **整型(int/uint)**:分别表示有符号和无符号的不同位数的整型变量; 支持关键字 uint8 到 uint256(无符号，从 8 位到 256 位)以及 int8 到 int256，以 8 位为步长递增
- **定长浮点型(fixed / ufixed)**: 表示各种大小的有符号和无符号的定长浮点型;在关键字 ufixedMxN 和 fixedMxN 中，M 表示该类型占用的位数，N 表示可用的小数位数
- **地址(address)**:存储一个 20 字节的值(以太坊地址大小)
- **定长字节数组**:关键字有 bytes1，bytes2，bytes3，...，bytes32
- **枚举(enum)**:一种用户可以定义类型的方法，与C语言类似，默认从0 开始递增，一般用来模拟合约的状态
- **函数(function)**:一种表示函数的类型

## [Solidity引用类型](https://solidity-cn.readthedocs.io/zh/develop/types.html#index-13)

* **数组(Array)**

  * 数组可以在声明时指定长度(定长数组)，也可以动态调整大小(变长数组、动态数组)

  - 对于**存储型(storage)**的数组来说，元素类型可以是**任意**的(即元素也可以是数组类型，映射类型或者结构体);对于**内存型 (memory)**的数组来说，元素类型**不能是映射(mapping)类型**

* **结构(Struct)**

  * Solidity 支持通过构造结构体的形式定义新的类型

* **映射(Mapping)**

  * 映射可以视作哈希表 ，在实际的初始化过程中创建每个可能的 key，并将其映射到字节形式全是零的值(类型默认值)

## Solidity地址类型

* address

  - 地址类型存储一个 20 字节的值(以太坊地址的大小);地址类型也有成员变量，并作为所有合约的基础

* address payable(v0.5.0引入)

  - 与地址类型基本相同，不过多出了 transfer 和 send 两个成员变量

* 两者区别和转换

  - Payable 地址是可以发送 ether 的地址，而普通 address 不能允许从 payable address 到 address 的隐式转换，而反过来的直接转换是不可能的(唯一方法是通过uint160来进行中间转换)

  - 从0.5.0版本起，合约不再是从地址类型派生而来，但如果它有payable的回退函数，那同样可以显式转换为 address 或者 address payable 类型

* ```<address>.balance (uint256)```:该地址的 ether 余额，以Wei为单位

* ```<address payable>.transfer(uint256 amount)```:向指定地址发送数量为 amount 的 ether(以Wei为单位)，失败时抛出异常，发送 2300 gas 的矿工费，不可调节

  * **注意是向address send代币！**

* ```<address payable>.send(uint256 amount) returns (bool)```:向指定地址发送数量为 amount的 ether(以Wei为单位)，失败时返回 false，发送 2300 gas 的矿工费用，不可调节

  * **注意是向address send代币！**
  * **send没有异常，所以默认是执行成功的！**

* ```<address>.call(bytes memory) returns (bool, bytes memory)```:发出底层函数 CALL，失败时返回 false，**发送所有可用 gas**，可调节 

  * 失败没有异常

* ```<address>.delegatecall(bytes memory) returns (bool, bytes memory)```:发出底层函数 DELEGATECALL，代理调用，失败时返回 false，**发送所有可用 gas**，可调节 

* ```<address>.staticcall(bytes memory) returns (bool, bytes memory)```:发出底层函数 STATICCALL ，失败时返回 false，**发送所有可用 gas**，可调节

* 地址成员变量用法

  * **balance 和 transfer**

    * 可以使用balance属性来查询一个地址的余额，可以使用transfer函数向一个payable地址发送 以太币Ether(以 wei 为单位) 

    * ```solidity
      address payable x = address(0x123);
      address myAddress = address(this);
      if (x.balance < 10 && myAddress.balance >= 10) 
      	x.transfer(10);
      ```

  * **send**

    * send 是 transfer 的低级版本。如果执行失败，当前的合约不会因为异 常而终止，但 send 会返回 false

  * **call**

    * 也可以用call来实现转币的操作，通过添加.gas()和.value()修饰器: 

    * ```solidity
      nameReg.call.gas(1000000).value(1 ether)(abi.encodeWithSignature("register(string)", "MyName"));
      ```

## 字符数组(Byte Arrays)

**定长字符数组**

* 属于值类型，bytes1，bytes2，...，bytes32分别代表了长度为1到32的字

**节序列**

* 有一个**.length**属性，返回数组长度(只读)

* ```solidity
  function test() public pure return(unit){ // 最后函数输出17
  	bytes17 a;
  	return a.length;
  }
  ```

**变长字符数组**

* 属于引用类型，包括 bytes和string，不同的是bytes是Hex字符串，而string是UTF-8编码的字符串

## 枚举(Enum)

* 枚举类型用来用户自定义一组常量值
* 与C语言的枚举类型非常相似，对应整型值
* **枚举类型、结构类型、状态变量需要在函数外声明！！**

```solidity
pragma solidity >=0.4.0 <0.6.0; 
contract Purchase {
	// 枚举类型、结构类型、状态变量需要在函数外声明！！
	enum State { Created, Locked, Inactive } 
	function test() public pure return(unit){ // 最后函数输出17
    State st = State.Created;
    return uint(st); // Created, Locked, Inactive 分别是0,1,2
  }
}
```

## 数组(Array)

- 固定大小k和元素类型T的数组被写为T[k]，动态大小的数组为T[]。

  **例如，一个由5个uint动态数组组成的数组是uint[]\[5]**(定义的时候，和C语言顺序是不一样的)

- 要**访问第三个动态数组中的第二个uint，可以使用x[2]\[1]**（访问的时候，和C语言顺序是一样的）

- 越界访问数组，会导致调用失败回退

- 如果要添加新元素，则必须使用.push()或将.length增大, (**如果存在storage里边，长度可以变，如果存在memory里边，长度不能变**)

- 变长的storage数组和bytes(不包括string)有一个push()方法。可以将一个新元素附加到数组末端，返回值为当前长度

- 数组示例

  ```solidity
  pragma solidity >=0.4.16 <0.6.0; 
  contract C {
    function f(uint len) public pure {
      uint[] memory a = new uint[](7);
      bytes memory b = new bytes(len); 
      assert(a.length == 7); 
      assert(b.length == len);
      a[6] = 8;
    } 
  }
  ```

## [结构(Struct)](https://solidity-cn.readthedocs.io/zh/develop/types.html#structs)

* 结构类型可以在映射和数组中使用，它们本身可以包含映射和数组。
* **结构不能包含自己类型的成员**，但可以作为自己数组成员的类型，也可以作为自己映射成员的值类型

```solidity
pragma solidity >=0.4.0 <0.6.0; 
contract Ballot {
  struct Voter {
    uint weight;
    bool voted;
    uint vote; 
  }
}
```

## 映射(Mapping)

* 声明一个映射:```mapping(_KeyType => _ValueType)```
* _KeyType可以是任何基本类型。这意味着它可以是任何内置值类型加上字符数组和字符串。**不允许使用用户定义的或复杂的类型，如枚举，映射，结构以及除bytes和string之外的任何数组类型**。 
* _ValueType可以是任何类型，包括映射。

```solidity
pragma solidity >=0.4.0 <0.6.0;
contract MappingExample { 
	mapping(address => uint) public balances; 
	
	function update(uint newBalance) public {
  	balances[msg.sender] = newBalance;
  }
}

  contract MappingUser {
    function f() public returns (uint) {
    MappingExample m = new MappingExample();
    m.update(100);
    return m.balances(address(this));
  }
}
```

* 下面是上课讲的例子，比较绕：

```solidity
pragma solidity ^0.4.0;
contract C{
	mapping (address=>uint)public balances;
	constructor(){
		balances[address(this)]=300;
  }
	function update(uint amount)public{
		balances[msg.sender]amount;
  }
}


contract D{
function fun() public view returns(uint,uint,uint){
  C c = new c();
  c.update(10);
  return c.balances(address(c)),c.balances(address(this)),c.balances(msg.sender);
	}
}
```

应该返回300，10，0.因为c.update传入的参数，是调用他的地址，address(c)是c的地址，在合约C创建的时候，c的balances就是300；address(this)的this是D，fun()中的c.update传入了D的地址，所以d的balances经过updated成了10；c.balances(msg.sender)获取的是用户的地址对应的balances，并没有设置过，是0。

## Solidity数据位置

* 所有的复杂类型，即数组、结构和映射类型，都有一个额外属性，“数据位置”，用来说明数据是保存在内存 memory 中还是 存储 storage 中
* 根据上下文不同，大多数时候数据有默认的位置，但也可以通过在类型名后增加关键字 storage 或 memory 进行修改
* 函数参数(包括返回的参数)的数据位置默认是memory，局部变量的数据位置默认是 storage，状态变量的数据位置强制是 storage
* 另外还存在第三种数据位置，calldata，这是一块只读的，且不会永久存储的位置，用来存储函数参数。外部函数的参数(非返回参数) 的数据位置被强制指定为 calldata ，效果跟 memory 差不多

## 数据位置总结

* 强制指定的数据位置

  - 外部函数的参数(不包括返回参数):calldata;

  - 状态变量:storage

- 默认数据位置
  - 函数参数(包括返回参数):memory;
  - 引用类型的局部变量:storage
  - 值类型的局部变量:栈(stack)
- 特别要求
  - 公开可见(publiclyvisible)的函数参数一定是memory类型，如果要求是 storage 类型则必须是 private 或者 internal 函数，这是为了防止随意的公开调用占用资源