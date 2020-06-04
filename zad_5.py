file = open('zad03.txt')
cats = []
class cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


for lines in file:
    line = lines.split(",")
    cats.append(cat(line[0], line[1], line[2]))

for cat in cats:
  print(cat.name, cat.age, cat.color)