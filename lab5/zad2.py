sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for k in sample_dict:
 print(f'{k:<10} = {sample_dict[k]:>8}')

 keys = ['name','surname']
 D={}
 for x in range(len(keys)):
  if keys[x] in sample_dict:
   D[keys[x]] = sample_dict.get(keys[x])
print(D)

for x in range(len(keys)):
 del sample_dict[keys[x]]

if 'Jones' in sample_dict.values():
 print('jones wystepuje w slowniku')
else:
 print('jones nie wystepuje w slowniku')

sample_dict['location'] = sample_dict['city']
del sample_dict['city']

print(sample_dict)