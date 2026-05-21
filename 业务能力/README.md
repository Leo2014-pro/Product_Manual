# 全球收款


### 模块定义

全球收款系统用于接收来自不同国家与网络的资金，并统一进入账本系统。

### 设计目标

- 打通全球资金入口
- 支持法币 + 数字资产统一入账
- 降低跨境收款复杂度
- 提供统一资金视图

### 法币收款能力

支持以下收款方式：
- 本地银行账户收款（Local Collection Accounts）
- SWIFT 跨境汇款
- 本地清算网络（Local Rails）
- 多币种账户体系（Multi-Currency Accounts）
支持币种：
- USD / EUR / GBP / SGD / HKD 等

### 数字资产收款能力

支持主流数字币（包含不限于）：
- USDT
- USDC
- BTC
- ETH
能力包括：
- 多链地址管理（ERC20 / TRC20 等）
- 链上交易监听（On-chain Listener）
- 自动入账到资产系统
- 交易与账本映射（Ledger Mapping）

### 示例流程（电商收款）

- 用户支付 USD 或 USDT
- 进入收款账户（Bank / Wallet Address）
- 系统自动识别资金类型
- 写入统一账本系统
- 进入商户资产账户
- 可用于后续支付或结算