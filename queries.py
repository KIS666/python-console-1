from collections import Counter
queries = [
'смотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара',
  'сериалы этим летом', 'курс по питону', 'сериалы про спорт'
]
kolvo = []
for i in queries:
  sp = i.split(' ')
  kolvo.append(len(sp))
c_kolvo = Counter(kolvo)
sum = 0
for j in c_kolvo.values():
  sum +=j
print(f'кол-во запросов {sum} ')
for l in c_kolvo.keys():
  j_proc = round(100*c_kolvo.get(l) /sum, 3)
  print(f'запросов из {l} слов - {j_proc}%')
