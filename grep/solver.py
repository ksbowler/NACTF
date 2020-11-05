f = open("flag.txt")
flag = [s.strip() for s in f.readlines()]

for candi in flag:
	#print(candi[:6])
	#break
	if candi[:6] != "nactf{": continue
	#print(candi)
	if len(candi) != 52: continue
	#print(candi)
	check = False
	for i in range(6,16):
		if not( candi[i] == "n" or candi[i] == "a" or candi[i] == "c"):
			check = True
			break
	if check: continue
	#else: print(candi)
	for i in range(14):
		if not( candi[-i-2] == "f" or candi[-i-2] == "t" or candi[-i-2] == "c"):
			check = True
			break
	if check: continue
	else: print(candi)

