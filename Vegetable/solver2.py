from Crypto.Util.number import *
import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "challenges.ctfd.io", 30267
s, f = sock(HOST, PORT)
print(read_until(f,"5.\n"))
s.send(b'2\n')
while True:
	print(read_until(f,"r:\n"))
	print(read_until(f))
	recv_m = read_until(f).split(", ")
	print(recv_m)
	perf = sorted(recv_m)
	print(recv_m)
	print(read_until(f,"x+1\n"))
	print(read_until(f))
	mes = ""
	for i in range(len(perf)):
		#pref[i]をi番目に持ってきたい
		for j in range(i,len(recv_m)):
			if perf[i] == recv_m[j]:
				for k in range(j-1,i-1,-1): mes += str(k) + " "
				recv_m = perf[:i+1] + recv_m[i:j] + recv_m[j+1:]
				assert len(recv_m) == len(perf)
				break
	print("mes :",mes)
	mes += "\n"
	s.send(mes.encode())
	for _ in range(5): print(read_until(f))
	break
#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() ot .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

