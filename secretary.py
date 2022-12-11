documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
	'3': []
}

def print_name(doc):
  p = input('Введите номер документа - ')
  for i in doc:
    if i['number'] == p:
      return i['name']

def print_namber_dirs(dir):
  s = input('Введите номер документа - ')
  for l in dir.keys():
    for i in dir.get(l):
      if i == s:
        return ((l))
  return('Такой документ не существует')

def print_passport(doc): 
  l = []
  for i in doc:
    l.append(f"{i['type']} '{i['number']}' '{i['name']}'")
  return(l)

def add_new_doc(doc, dir):
  doki = dict()
  vopr = 'да'
  while (vopr == 'да') or (vopr == 'Да'):
    doki["type"] = input('Введите тип документа - ') 
    doki["number"] = input('Введите номер документа - ')
    doki["name"] = input('Введите имя - ')
    doc.append(doki)
    
    nom_p = int(input('Введите номер полки - '))
    while nom_p > 3:
      print('Такой полки не существует')
      nom_p = int(input('Введите номер полки - '))
    for i in dir.keys():
      if int(i) == nom_p:
        dir[i].append(doki["number"]) 
        
    vopr = input('Ввести еще документ? \n')    
  return(doc, dir)
  
def main(documents, directories):
  comm = input('Введите команду - ')
  while True:
    if comm == 'p':
      print(print_name(documents))
      break
    elif comm == 's':
      print(print_namber_dirs(directories))
      break
    elif comm == 'l':
      print(print_passport(documents))
      break
    elif comm == 'a':
      print(add_new_doc(documents, directories))
      break
    else:
      comm = input('Мы не нашли такуюкоманду:(\nGопробуйте еще раз - ')
main(documents, directories)
