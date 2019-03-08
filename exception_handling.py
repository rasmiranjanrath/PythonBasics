try:
  fo=open('dat.txt','r+')
  str=fo.read()
  print(str)
except IOError:
	print("unable to read file")