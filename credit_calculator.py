proc = int(input('Введите процентную ставку клиента: '))
r = int(
  input(
    'Выберите регион: \n1 - Камчатский Край \n2 - Приморский Край \n3 - Бурятия \n4 - Якутия \n5 - Татарстан \n6 - Московская Область \n7 - Карелия'
  ))
if r > 7:
  print('Неверный выбор')
  exit()
if r <= 4:
  proc = 2
else:
  cil = int(input('Введите кол-во детей: '))
  zp = input('Зарплата в нашем банке? ')
  str = input('Страховка в нашем банке? ')

  if cil > 3:
    proc -= 1
  if zp == 'да':
    proc -= 0.5
  if str == 'да':
    proc -= 1.5
print('Процентная ставка клиента = ', proc)
