# coding:utf-8

# パターン1
ipaddr = "0.0.0.0"
netmask = "0.0.0.0"

ipaddr_list = ipaddr.split(".")
if ipaddr_list != 4:
    break: #ここですべての処理から抜けさせたい

ipaddr = "0.0.0.0/0"
ipaddr_list = ipaddr.split(".")
if ipaddr_list != 4:
    break
elif:
    netmask_list = ipaddr_list[3].split("/")
    netmask = netmask_list[1]


# パターン2
import sys

ipaddr = sys.argv[1]
netmask = sys.argv[2]

ipaddr_list = ipaddr.split("/")
ipaddr_len = len(ipaddr_list)

if ipaddr_len == 2:
    netmask = ipaddr_list[1]
    ipaddr = ipaddr_list[0]

# パターン3
import sys

sys = sys.argv[1:]
len1 = len(sys)

if len1 == 0:
    ipaddr = raw_input("ipaddr   = :")
    netmask = raw_input("netmask = :")

elif len1 == 1:
    ipaddr_list = sys.split("/")
    ipaddr = ipaddr_list[0]
    netmask = ipaddr_list[1]

elif len1 == 2:
    ipaddr = sys[1]
    netmask = sys[2]

else:
    print("error!!!!!!1111")
