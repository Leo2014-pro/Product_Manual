# 付款

### 付款

付款是商家管理所有**向用户付款**（代付）订单、跟踪资金状态的核心功能模块。

#### 数币付款订单

**功能描述**：本页面集中展示您数字货币代付订单记录，便于查询、跟踪和管理。

<figure><img src="https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=YWMzYWFkZmNmMGY1NmQ5NDU3ZjdlMTEwNTZmNDQ2NTdfSDdyaWJFZFZ4MjV1NEE1eUplbkRNSTZ0RmR2SGZHbVpfVG9rZW46WFZvSmJjU1NFb3lTR2h4OXRHWmNJNzdabmhmXzE3ODE2NzIzMTE6MTc4MTY3NTkxMV9WNA&#x26;add_watermark=true&#x26;scene_type=CCM" alt=""><figcaption></figcaption></figure>

**操作**：

* 筛选：订单号、类型、交易状态、时间搜索。
* 查看：订单提现详细字段。
  * 订单状态：平台提交后，在链上确认成功后，订单变为完成中。
  * 回调通知：回调成功后，表示已通知下游接口。
*   免审设置：可设置币种需要在商家后台进行审核，如不设置则均是免审。

    * 列表：显示设置币种免审数据。
    * 免审数量：高于该数字的提现订单均需要商家进行手工审核。
    * 币种：需要审核币种
    * 链类型：币种归属公链
    * 状态：开启、关闭

    <br>

    <figure><img src="https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=MzZmYTQwYzEyOWRjNjMxY2IxZjc2NTUzNDNkMzJmZjBfQXZWUU5KZk1BZ3FxYlVrUllLNXpxUmpLa01rSDl0cDZfVG9rZW46VVIzY2JYR0tmb3pmaTZ4UGxsYWNqaWY2bmVuXzE3ODE2NzIzMTE6MTc4MTY3NTkxMV9WNA&#x26;add_watermark=true&#x26;scene_type=CCM" alt=""><figcaption></figcaption></figure>

<figure><img src="https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTkwMzE4Njk3OGNiOWY5NmZmNmY2ZjM5NWNhYzI2MTdfQm5uVkhCVld4bDV4V2tHbjVKc2pCNXNaTEs0NjNaRlJfVG9rZW46Qk9qSGJRSWNVbzllNTR4cXdSRGNGMkpQbktmXzE3ODE2NzIzMTE6MTc4MTY3NTkxMV9WNA&#x26;add_watermark=true&#x26;scene_type=CCM" alt=""><figcaption></figcaption></figure>

* 批量付款：下载模板进行填写批量付款收款信息

<figure><img src="https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=OTQ1MmU4N2FkNjcyMzcyY2IzYTdhZTQwNTE5NzM1ZDRfZWp3S0IzMjB0bjZYbHR1QlphVjhwQzJKdFJiODhUdzlfVG9rZW46T1lQTGJrTGhQbzlTbnl4MnRVdGNDUVV2bjNmXzE3ODE2NzIzMTE6MTc4MTY3NTkxMV9WNA&#x26;add_watermark=true&#x26;scene_type=CCM" alt=""><figcaption></figcaption></figure>

* 审核/批量审核：审核通过后，代付订单进行上链付款。审核不通过订单失败。
* 切换状态：该操作仅沙河环境存在，用于API对接时，调试使用。

#### 法币付款订单

尽情期待！

### 承兑订单
