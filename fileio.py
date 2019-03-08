import os
fo=open('data.txt','wb')

#print file name
print(fo.name)
#write data to file

fo.write( "Python is a great language.\nYeah its great!!\n");
fo.close()
#read from file
fr=open("data.txt","r+")
data=fr.read()
print(data)
print(fr.tell())
#rename file name ,need to import os
os.rename('data.txt','info.txt')
fr.close()
print(os.getcwd())
