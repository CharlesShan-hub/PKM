# ERC20代币合约

2022.2.20

## 源码粘贴

```solidity
pragma solidity ^0.4.16;
interface tokenRecipient { 
	function receiveApproval(address _from, uint256 _value, address _token, bytes _extraData) external; 
	}

  contract TokenERC20 {
    // Public variables of the token
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    // 18 decimals is the strongly suggested default, avoid changing it 
    uint256 public totalSupply;
    
    // This creates an array with all balances
    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;
    // This generates a public event on the blockchain that will notify clients 
    event Transfer(address indexed from, address indexed to, uint256 value);
    // This generates a public event on the blockchain that will notify clients
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);
    // This notifies clients about the amount burnt 
    event Burn(address indexed from, uint256 value);
  }
  
  /**
   * Constructor function
   *
   * Initializes contract with initial supply tokens to the creator of the contract 
   */
  function TokenERC20( uint256 initialSupply, string tokenName,
    string tokenSymbol ) public {
    totalSupply = initialSupply * 10 ** uint256(decimals); //Update total supply with the decimal amount
    balanceOf[msg.sender] = totalSupply; // Give the creator all initial tokens
    name = tokenName; // Set the name for display purposes
    symbol = tokenSymbol; // Set the symbol for display purposes 
  }
  
  
  /**
   * Internal transfer, only can be called by this contract 
   */
  function _transfer(address _from, address _to, uint _value) internal { 
  	// Prevent transfer to 0x0 address. Use burn() instead 
  	require(_to != 0x0);
    // Check if the sender has enough
    require(balanceOf[_from] >= _value);
    // Check for overflows
    require(balanceOf[_to] + _value >= balanceOf[_to]); // Save this for an assertion in the future
    uint previousBalances = balanceOf[_from] + balanceOf[_to]; // Subtract from the sender
    balanceOf[_from] -= _value;
    // Add the same to the recipient
    balanceOf[_to] += _value;
    emit Transfer(_from, _to, _value);
    // Asserts are used to use static analysis to find bugs in your code. They should never fail
    assert(balanceOf[_from] + balanceOf[_to] == previousBalances);
  }
  
  
  /**
  * Transfer tokens 
  *
  * Send `_value` tokens to `_to` from your account 
  *
  * @param _to The address of the recipient
  * @param _value the amount to send 
  */
  function transfer(address _to, uint256 _value) public returns (bool success) { 
    _transfer(msg.sender, _to, _value);
    return true;
  }
  
  
  /**
  * Transfer tokens from other address 
  *
  * Send `_value` tokens to `_to` on behalf of `_from`
  *
  * @param _from The address of the sender 
  * @param _to The address of the recipient 
  * @param _value the amount to send
  */
  function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
    require(_value <= allowance[_from][msg.sender]); // Check allowance 
    allowance[_from][msg.sender] -= _value;
    _transfer(_from, _to, _value);
    return true;
  }
  
  
  /**
  * Set allowance for other address 
  *
  * Allows `_spender` to spend no more than `_value` tokens on your behalf 
  *
  * @param _spender The address authorized to spend
  * @param _value the max amount they can spend 
  */
  function approve(address _spender, uint256 _value) public returns (bool success) {
  	allowance[msg.sender][_spender] = _value;
  	emit Approval(msg.sender, _spender, _value);
  	return true; 
  }
  
  
  /**
  * Set allowance for other address and notify
  *
  * Allows `_spender` to spend no more than `_value` tokens on your behalf, and then ping
the contract about it 
  *
  * @param _spender The address authorized to spend
  * @param _value the max amount they can spend
  * @param _extraData some extra information to send to the approved contract
  */
  function approveAndCall(address _spender, uint256 _value, bytes _extraData) public returns (bool success) {
  tokenRecipient spender = tokenRecipient(_spender);
  if (approve(_spender, _value)) {
  	spender.receiveApproval(msg.sender, _value, this, _extraData);
  	return true; 
  }
  
  
  /**
  * Destroy tokens 
  *
  * Remove `_value` tokens from the system irreversibly 
  *
  * @param _value the amount of money to burn
  */
  function burn(uint256 _value) public returns (bool success) {
  	// Check if the sender has enough
  	require(balanceOf[msg.sender] >= _value); 
  	// Subtract from the sender
  	balanceOf[msg.sender] -= _value; 
  	// Updates totalSupply
  	totalSupply -= _value;
  	emit Burn(msg.sender, _value);
  	return true; 
  }


	/**
	* Destroy tokens from other account 
	*
	* Remove `_value` tokens from the system irreversibly on behalf of `_from`. 
	*
	* @param _from the address of the sender
	* @param _value the amount of money to burn
	*/
   function burnFrom(address _from, uint256 _value) public returns (bool success) {
   	// Check if the targeted balance is enough 
    require(balanceOf[_from] >= _value); 
    // Check allowance
    require(_value <= allowance[_from][msg.sender]);
    // Subtract from the targeted balance
    balanceOf[_from] -= _value; 
    // Subtract from the sender's allowance
    allowance[_from][msg.sender] -= _value; 
    // Update totalSupply
    totalSupply -= _value;
    emit Burn(_from, _value);
    return true;
   }
}
```

## 分析——合约的变量

```solidity
contract TokenERC20 {
    // Public variables of the token
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    // 18 decimals is the strongly suggested default, avoid changing it 
    uint256 public totalSupply;
    
    // This creates an array with all balances
    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;
    
    // This generates a public event on the blockchain that will notify clients 
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    // This generates a public event on the blockchain that will notify clients
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);
    
    // This notifies clients about the amount burnt 
    event Burn(address indexed from, uint256 value);
    
    //......
  }
```

* ```name``` 和 ```symbol``` 是要发行货币的名字与代称，比如假如比特币用这个合约的话，name就是比热币，symbol就是BTC。
* ```decimals``` 规定了小数点精确位数。默认是18，最好不要修改。
* ```totalSupply``` 是一共发行的货币。
* ```balanceOf``` 是某个账户的余额。
* ```allowance``` 授权额度。代表了别人用这个账户可以转账的额度。
* ```mapping (address => mapping (address => uint256))``` 中的第一个mapping保存了每一个用户对其他用户的授权信息，第二个mapping保存了某个用户对各个用户的授权信息。
* ```Transfer```,```Approval```,```Burn ``` 是转移，同意和销毁代币的事件。

## 分析——构造函数

```solidity
/**
* Constructor function
*
* Initializes contract with initial supply tokens to the creator of the contract 
*/
function TokenERC20( 
	uint256 initialSupply, 
	string tokenName,
	string tokenSymbol ) public {
	//Update total supply with the decimal amount
	totalSupply = initialSupply * 10 ** uint256(decimals); 
	// Give the creator all initial tokens
	balanceOf[msg.sender] = totalSupply; 
	// Set the name for display purposes
	name = tokenName;
	// Set the symbol for display purposes 
	symbol = tokenSymbol;
}
```

* ERC20称为一个标准，需要允许各种代币通过它进行创建，所以代币名称与代称是传入的参数，而不是在源代码里边写死了，然后每个人新创建代币的时候都重新改源代码。
* ```totalSupply = initialSupply * 10 ** uint256(decimals); ```因为浮点类型的数容易造成缺失，所以把它转化成了整型的。
* ```balanceOf[msg.sender] = totalSupply; ```创建者拥有一些代币的控制权。

## 分析——转账

```solidity
/**
* Internal transfer, only can be called by this contract 
*/
function _transfer(address _from, address _to, uint _value) internal { 
  // Prevent transfer to 0x0 address. Use burn() instead 
  require(_to != 0x0);
  // Check if the sender has enough
  require(balanceOf[_from] >= _value);
  // Check for overflows
  require(balanceOf[_to] + _value >= balanceOf[_to]); // Save this for an assertion in the future
  uint previousBalances = balanceOf[_from] + balanceOf[_to];
  // Subtract from the sender
  balanceOf[_from] -= _value;
  // Add the same to the recipient
  balanceOf[_to] += _value;
  emit Transfer(_from, _to, _value);
  // Asserts are used to use static analysis to find bugs in your code. They should never fail
  assert(balanceOf[_from] + balanceOf[_to] == previousBalances);
}

/**
* Transfer tokens 
*
* Send `_value` tokens to `_to` from your account 
*
* @param _to The address of the recipient
* @param _value the amount to send 
*/
function transfer(address _to, uint256 _value) public returns (bool success) { 
  _transfer(msg.sender, _to, _value);
  return true;
}

  
/**
* Transfer tokens from other address 
*
* Send `_value` tokens to `_to` on behalf of `_from`
*
* @param _from The address of the sender 
* @param _to The address of the recipient 
* @param _value the amount to send
*/
function transferFrom(
	address _from, 
	address _to, 
	uint256 _value) public returns (bool success) {
    require(_value <= allowance[_from][msg.sender]); // Check allowance 
    allowance[_from][msg.sender] -= _value;
    _transfer(_from, _to, _value);
    return true;
}
```

* ```_transfer```函数

  * ```_transfer```:前边加了一个“_”，说明只能在合约内部调用

* ```transfer```函数

  * ```require(_to != 0x0);``` 不能向0地址转币，如果要销毁代币需要用brun方法。
  * ```require(balanceOf[_to] + _value >= balanceOf[_to]);```防止加法溢出。
  * ```previousBalances```记录了交易前，发送方与接收方账户代币的总和，在进行余额加减运算后进行```assert(balanceOf[_from] + balanceOf[_to] == previousBalances);```（断言），来保证转账过程的原子性（确定中间不出啥幺蛾子）。

* ```transferFrom```函数：这个就是允许别人转这个账户的钱。

  * ```allowance```是```mapping (address => mapping (address => uint256))```

    ```allowance[_from][msg.sender]```是本账户允许另一账户A(```_from```)操控自己转币的上限。

## 分析——批准

```solidity
interface tokenRecipient { 
	function receiveApproval(address _from, uint256 _value, address _token, bytes _extraData) external; 
}


/**
* Set allowance for other address 
*
* Allows `_spender` to spend no more than `_value` tokens on your behalf 
*
* @param _spender The address authorized to spend
* @param _value the max amount they can spend 
*/
function approve(address _spender, uint256 _value) public returns (bool success) {
  allowance[msg.sender][_spender] = _value;
  emit Approval(msg.sender, _spender, _value);
  return true; 
}


/**
* Set allowance for other address and notify
*
* Allows `_spender` to spend no more than `_value` tokens on your behalf, and then ping
the contract about it 
*
* @param _spender The address authorized to spend
* @param _value the max amount they can spend
* @param _extraData some extra information to send to the approved contract
*/
function approveAndCall(address _spender, uint256 _value, bytes _extraData) public returns (bool success) {
  tokenRecipient spender = tokenRecipient(_spender);
  if (approve(_spender, _value)) {
  spender.receiveApproval(msg.sender, _value, this, _extraData);
  return true; 
}
```

* ```approve```，给```_spender```授权了```_value```的额度。

## 分析——销毁

```solidity
/**
* Destroy tokens 
*
* Remove `_value` tokens from the system irreversibly 
*
* @param _value the amount of money to burn
*/
function burn(uint256 _value) public returns (bool success) {
// Check if the sender has enough
require(balanceOf[msg.sender] >= _value); 
// Subtract from the sender
balanceOf[msg.sender] -= _value; 
// Updates totalSupply
totalSupply -= _value;
emit Burn(msg.sender, _value);
return true; 
}


/**
* Destroy tokens from other account 
*
* Remove `_value` tokens from the system irreversibly on behalf of `_from`. 
*
* @param _from the address of the sender
* @param _value the amount of money to burn
*/
function burnFrom(address _from, uint256 _value) public returns (bool success) {
// Check if the targeted balance is enough 
require(balanceOf[_from] >= _value); 
// Check allowance
require(_value <= allowance[_from][msg.sender]);
// Subtract from the targeted balance
balanceOf[_from] -= _value; 
// Subtract from the sender's allowance
allowance[_from][msg.sender] -= _value; 
// Update totalSupply
totalSupply -= _value;
emit Burn(_from, _value);
return true;
}
```

