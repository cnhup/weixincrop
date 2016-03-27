# weixincrop
微信企业号框架

## url接入
urls.py 中 callback 

## 思路
微信回调中，框架解析xml，判断事件类型，发送相应signal，订阅者方法处理数据后可以做返回xml等操作，不同被动消息已经封装。

## 注意
消息接收者要在app加载的时候被框架调用一下。比如放到setting中或者urls中
