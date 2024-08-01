#强大的网络数据包处理库，适用于网络分析和攻击模拟

from scapy.all import *

#创建网络数据包，目的地址为'8.8.8.8'即谷歌的公共服务器
#/：Scapy 使用 / 操作符来将不同层的数据包组合在一起
#ICMP()：创建一个 ICMP数据包
packet = IP(dst='8.8.8.8')/ICMP()
#发送数据包并接收第一个响应
response = sr1(packet)

#显示响应
response.show()