import random

def generate_name(count=1):
  names = []
  with open('lastnames_100.txt') as f:
    lastnames = f.read().splitlines()
  with open('firstnames_100.txt') as f:
    firstnames = f.read().splitlines()
  for i in range(count):
    names.append('{} {}'.format(random.choice(firstnames), random.choice(lastnames)))
  if len(names) == 1:
    names = names.pop()
  return names

if __name__ == '__main__':
  name = generate_name()
  print(name)
  names = generate_name(count=5)
  print(names) 
