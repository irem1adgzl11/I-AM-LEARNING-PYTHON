from ast import increment_lineno


Name = "irem"
Surname = "Adıgüzel"
Age = "19"
print("My name is {} {}".format(Name,Surname))
print("My name is {1} {0}".format(Name,Surname))#indexlere numara vererek yerlerinde oyanama yapabiliriz.
print("My name is {n} {s}".format(n = Name,s = Surname))#indexlere harflerdirme yaparak da yerlerini belirleye biliriz.
print("My name is {} {}. I'm {} years old.".format(Name,Surname,Age))

number = 5/3
print("The result is {n:1.4}".format(n = number))#Süslü parantezin içine yazdığım 4 sonucun 4 basamaklı olmasını istediğimden.
print(f"My name is {Name} {Surname}.I'm {19} years old.")# 10. satırda yaptığımız işlemi burada başına sadece f koyarak daha kısa yazabiliriz.