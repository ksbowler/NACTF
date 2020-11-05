f = open("country.txt")
cun = [s.strip() for s in f.readlines()]
flag = "nactf{"
i = 0
for temp in cun:
	t = temp.split()
	#flag += t[-2][0]
	print(t[-2][0])
	flag += t[-2][0]
	i += 1
flag += "}"

print(flag)
print(len(flag))
