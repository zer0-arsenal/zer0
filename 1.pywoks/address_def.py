
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

