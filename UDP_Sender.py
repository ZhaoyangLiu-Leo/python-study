#coding:utf-8
from socket import *
import time

HOST = 'localhost'
PORT = 8000
BUFF = 1024
flag = 0
data = ''
timeout = 5
send_num = 0

ADDR = (HOST, PORT)
send_socket = socket(AF_INET, SOCK_DGRAM)
send_socket.settimeout(timeout)    #设置超时时间

data = str(send_num) + '.' + raw_input('Send Data:')
while True:
    try:
        send_socket.sendto(data, ADDR)
        resp, ADDR = send_socket.recvfrom(BUFF)
        resp_num = int(resp)
        if resp_num == send_num:
            #序号一致，构造下一个报文段
            print 'ACK, data:"' + data + '" is received correctly!'
            send_num = abs(send_num - 1)
            data = str(send_num) + '.' + raw_input('Send Data:')
        else:
            #不一致，等待下一次循环，再次发送相同数据
            print 'Receive the ACK of the previous number, the data will be resend!'
    except Exception as errno:    # 捕获超时异常
        #print errno.__repr__()
        print 'Time out, data will be resend!'
        continue
        
send_socket.close()
