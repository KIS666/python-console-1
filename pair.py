boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys)!=len(girls):
  print('Кто-то может остаться без пары:(')
  exit()
boys.sort()
girls.sort()
for name_boy, name_girl in zip(boys, girls):
  print(name_boy,'и', name_girl)
