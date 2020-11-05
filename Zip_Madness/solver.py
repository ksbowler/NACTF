import subprocess
for i in range(1000,0,-1):
	f = open("direction.txt")
	wh = f.read()
	mei = ["unzip", "-o", str(i)+wh+".zip"]
	x = subprocess.call(mei)
