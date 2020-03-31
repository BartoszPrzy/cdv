print("Kamil")
print(9)

pow=2**5
print(pow)

text="statek"
print(text*3)

imię=input("Podaj imię: ")
nazwisko=input("Podaj nazwisko: ")
print("Twoje imię: " + imię)
print("Twoje Nazwisko: " + nazwisko)
print("Imię: " + imię + "\nNazwisko: " + nazwisko)

dlugoscimie=str(len(imię))
print("Długość imienia: " + dlugoscimie)
dlugoscnazwisko=len(nazwisko)
print(dlugoscnazwisko)
print(type(imię))
print(type(nazwisko))
print(type(dlugoscimie))
print(type(dlugoscnazwisko))

first=nazwisko[0]
last=nazwisko[len(nazwisko)-1]
print(first)
print(last)


a="10"
print(type(a))
a=int(a)
print(type(a))

b=8
print(type(b))
b/=2
print(type(b))
print(b)

print("Narodowość: ",end="")
narodowsc=input()

print()
surname="Nowakowski"
print(surname[0])
print(surname[0:2])
print(surname[-2])
print(surname[-2:])
print(surname[:-2])
print(surname[:-2:2])
