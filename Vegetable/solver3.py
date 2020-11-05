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

def _c(temp):
	t = temp[1:]
	t.append(temp[0])
	return t

def _s(temp):
	t = [temp[1],temp[0]]
	return t + temp[2:]
	
#HOSTはIPアドレスでも可
HOST, PORT = "challenges.ctfd.io", 30267
s, f = sock(HOST, PORT)
print(read_until(f,"5.\n"))
s.send(b'3\n')
print(read_until(f,"r:\n"))
print(read_until(f))
recv_m = read_until(f).split(", ")
#print(recv_m)
perf = sorted(recv_m)
print(perf)
#print(read_until(f,"x+1\n"))
print(read_until(f))
mes = ""
p = int(len(recv_m) - 1)
for i in range(1,len(recv_m)):
	print(i)
	#print("Find : ",perf[p])
	while True:
		#print(type(recv_m[0]) , type(perf[p]))
		#print(recv_m[0] == perf[p])
		if recv_m[0] == perf[p]:
			if p == len(recv_m) -1 or recv_m[1] == perf[p+1]:
				#後ろi+1個sortできた
				for j in range(i):
					mes += "c "
					recv_m = _c(recv_m)
				break
				
		if recv_m[0] > recv_m[1]:
			#print("swap")
			mes += "s "
			recv_m = _s(recv_m)
		#print("slide")
		mes += "c "
		recv_m = _c(recv_m)
		#print(recv_m)
		#break
	#break
	p -= 1
	#print(recv_m)
	if p == 0: break

print("mes :",mes)
mes += "\n"
s.send(mes.encode())
for _ in range(10): print(read_until(f))

#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() ot .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

