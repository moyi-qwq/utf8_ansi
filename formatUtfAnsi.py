import os.path

FormatOfFind = ['.cpp']

def main():
	inputType = 'utf-8'
	outType = 'ansi'
	print("this exe will turn all .cpp file from utf-8 into ansi code")
	print("which enables devcpp to read it")
	qwq = int(input('to ansi/utf-8?(1/0)'))
	if qwq == 0:
		inputType,outType=outType,inputType
	for root, dirs, files in os.walk('.'):
		if root != '.': continue
		# print(root,dir,files)
		for filepath in files:
			p = -1
			while(filepath[p] != '.'): p -= 1
			if filepath.__len__() < abs(p) or filepath[p:] not in FormatOfFind: continue
			# print(filepath)
			with open(filepath,'r',encoding=inputType) as f:
				savef = f.read()
			f.close()
			# print(savef)
			with open(filepath,'w',encoding=outType) as f:
				f.write(savef)
			pass
		pass
	pass

if __name__ == '__main__':
	main()


