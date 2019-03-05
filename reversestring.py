string="rasmiranjan";

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str 
print("original string="+string)
print("reversed string="+reverse(string))
