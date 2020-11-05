from Crypto.Util.number import *
#import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib
import math

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

def _c(temp,cnt):
	t = temp[cnt:] + temp[:cnt]
	return t

def _s(temp,x,y):
	t = temp[:x]
	t.append(temp[y])
	t += temp[x+1:y]
	t.append(temp[x])
	t += temp[y+1:]
	return t
	
#HOSTはIPアドレスでも可
HOST, PORT = "challenges.ctfd.io", 30267
s, f = sock(HOST, PORT)
print(read_until(f,"5.\n"))
s.send(b'4\n')
print(read_until(f,"r:\n"))
print(read_until(f))
recv_m = read_until(f).split(", ")
print(recv_m)
perf = sorted(recv_m)
#print(perf)
#print(read_until(f,"x+1\n"))
print(read_until(f))
recv_t = read_until(f).split()
#print(recv_t)
#for i in range(len(recv_t)):
#	print(i,recv_t[i])
x = int(recv_t[40])
y = int(recv_t[46])
if x > y: x,y = y,x
print(x,y)
assert math.gcd(len(recv_m),y-x) == 1
mes = ""
p = int(len(recv_m) - 2)
for i in range(1,len(recv_m)):
	#x番目にsortしたい奴を持ってくる
	ind = recv_m.index(perf[p])
	if x <= ind: cnt = ind - x
	else: cnt = ind + 1 + len(recv_m) - 1 - x
	if recv_m[(ind+1)%len(recv_m)] == perf[p+1]:
		p -= 1
		if p == 0: break
		continue
	mes += "c "*cnt
	recv_m = _c(recv_m,cnt)
	assert recv_m[x] == perf[p]
	goal = recv_m.index(perf[p+1]) - 1
	#隣に行く
	# x + k(y-x) = goal mod len(recv_m)
	# k = (goal - x)%len(recv_m) * inverse(y-x,len(recv_m)
	swap_cnt = ((goal - x)%len(recv_m) * inverse((y-x),len(recv_m)))%len(recv_m)
	out = []
	for k in range(swap_cnt):
		if recv_m[x] < recv_m[y]:
			if out == []: out.append(recv_m[y])
			elif len(out) == 1:
				out.append(recv_m[y])
				out[0],out[1] = out[1],out[0]
			else:
				out = [recv_m[y]] + out
		mes += "s "
		recv_m = _s(recv_m,x,y)
		if k == swap_cnt - 1: break
		mes += "c "*(y-x)
		recv_m = _c(recv_m,y-x)
		#break
	while out != []:
		#out[0]を適切なところに
		back = recv_m.index(out[0])
		c_cnt = (back - x)%len(recv_m)
		mes += "c "*(c_cnt)
		recv_m = _c(recv_m,c_cnt)
		mes += "s "
		recv_m = _s(recv_m,x,y)
		out.pop(0)
	p -= 1
	if p == 0: break

cnt = recv_m.index(perf[0])
mes += "c "*cnt
recv_m = _c(recv_m,cnt)
#print(recv_m)
mes = mes[:-1]
mes += "\n"
s.send(mes.encode())
#print("sent")
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

