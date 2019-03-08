dict={'name':'rasmiranjan','designation':'programmer','age':25}
dict1={'name':'rasmiranjan','designation':'programmer','age':25,'hey':'extra'}
print(dict['name'])
print(dict['designation'])
print(dict['age'])

#update dictionary
dict['name']='rasmiranjan rath'
print(dict['name'])
print(cmp(dict,dict1))
#add a new element
dict['location']='bengaluru'
print(dict['location'])

print(type(dict))

print(cmp(dict,dict1))

#delete an element
del dict['name']
# print(dict['name']) it will throw error

dict.clear() #it will clear the dictionary