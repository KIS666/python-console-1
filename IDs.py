ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
att_id=[]
for i in ids.values():
  for j in range(len(i)):
    att_id.append(i[j])
print(list(set(att_id))) 
