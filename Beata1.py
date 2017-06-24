print('Hello, Django girls!')
if 3 > 2:
    print('to działa!')
    pass
    print('5 jest jednak większe od 2 ')
else:
    print('5 nie jest większe od 2')
name = 'Sonja'
if name =='Ola':
    print('Hej Ola!')
elif name == 'Sonja':
    print('Hej Sonja!')
else:
    print('Hej nieznajoma!')
glosnosc = 32
if glosnosc < 20:
    print("Prawie nic nie słychać.")
elif 20 <=glosnosc < 40:
    print("0, muzyka leci w tle.")
elif 40 <= glosnosc < 60:
    print("Idealnie, mogę usłyszeć wszystkie detale")
elif 60 <= glosnosc < 100:
    print("Troszeczke za głośno")
else:
    print ("ojoj! Moje uszy! :(")
def hej():
    print ('Hej!')
    print ('jak się masz?')
hej()
def hej(imie):
    if imie =='Ola':
        print('Hej Ola!')
    elif imie =='Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')
hej('Beata')
def hej(imie):
    print ('Hej' + imie +'!')
dziewczyny = ['Rachel', 'Ola', 'Sonja', 'Beata', 'Ty']
for imie in dziewczyny:
    hej(imie)
    print('Kolejna dziewczyna')
for i in range(1 ,6):
    print(i)
