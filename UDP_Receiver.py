#coding:utf-8
from socket import * 
import random

HOST = 'localhost'
PORT = 8000
BUFF = 1024
resp_list = ['a', 'b', 'c']  #a:收到没有比特差的报文段， b：有比特差， c：模拟超时
data = ''
resp_num = 0

ADDR = (HOST, PORT)

#创建UDPsocket
receiver_socket = socket(AF_INET, SOCK_DGRAM)
#服务器端绑定端口
receiver_socket.bind(ADDR)

while True:
    data, addr = receiver_socket.recvfrom(BUFF)
    #随机响应
    resp = random.choice(resp_list)
    recv_num = int(data[0])
    if resp == 'a':
        #随机接收端所需要的报文段的序号
        resp_num = recv_num
        receiver_socket.sendto(str(resp_num), addr)
        print 'receive data:' + str(data) + ', responce data number:' + str(resp_num)
    elif resp == 'b':
        #报文有比特差，翻转接收序号，并发送回去
        resp_num = abs(recv_num - 1)
        receiver_socket.sendto(str(resp_num), addr)
        print 'receive data:' + str(data) + ', responce data number:' + str(resp_num)
    
        
receiver_socket.close()
