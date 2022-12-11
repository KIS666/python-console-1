m = input('Введите месяц')
d = int(input('Введите день'))
if d>31:
  print('введите снова')
  exit()
if (m == 'декабрь' and 22<=d<=31) or (m == 'январь' and 1<=d<=20):
  print('Козерог')
elif (m == 'январь' and 21<=d<=31) or (m == 'февраль' and 1<=d<=18):
  print('Водолей')
elif (m == 'февраль' and 19<=d<=28) or (m == 'март' and 1<=d<=20):
  print('Рыбы')
elif (m == 'март' and 21<=d<=31) or (m == 'апрель' and 1<=d<=19):
  print('Овен')
elif (m == 'апрель' and 20<=d<=30) or (m == 'май' and 1<=d<=20):
  print('Телец')
elif (m == 'май' and 21<=d<=31) or (m == 'июнь' and 1<=d<=20):
  print('Близнецы')
elif (m == 'июнь' and 21<=d<=30) or (m == 'июль' and 1<=d<=22):
  print('Рак')
elif (m == 'июль' and 23<=d<=31) or (m == 'август' and 1<=d<=22):
  print('Лев')
elif (m == 'август' and 23<=d<=31) or (m == 'сентябрь' and 1<=d<=22):
  print('Дева')
elif (m == 'сентябрь' and 23<=d<=30) or (m == 'октябрь' and 1<=d<=22):
  print('Весы')
elif (m == 'октябрь' and 23<=d<=31) or (m == 'ноябрь' and 1<=d<=21):
  print('Скорпион')
elif (m == 'ноябрь' and 22<=d<=30) or (m == 'декабрь' and 1<=d<=21):
  print('Стрелец')
