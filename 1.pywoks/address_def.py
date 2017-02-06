
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


