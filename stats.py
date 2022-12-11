stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max = 0
for i in stats.keys():
  if stats.get(i)>max:
    max=stats.get(i)
for i in stats.keys():
  if stats.get(i)==max:
      print(f'у {i} - максимальный объем')
