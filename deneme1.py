from ast import increment_lineno
from operator import truediv


print(3+3)
print(type(3+4))
print(type(3+4.4))
# type sayı int mi float mı vs onu söylüyor.
#yorum satırı böyle oluşturuluyor.
"""" 
yorum paragrafı ise
böyle oluşturuluyor.
"""
# kdv oranını bildiğimiz ürünün satış fiyatını bulma
urun1 = 2000
urun2 = 3000
kdv = 0.18
print(urun1 + (urun1 * kdv))
print(urun2 + (urun2 * kdv))

"""
 değiken isimleri sayı ile başlayamaz, sembol(@ vb.) içeremez, boşluk 
 içeremez ,altçizgi(_) içerebilir,türkçe karakter pythonda kullanılıyor fakat diğer dillerde kullanılmadığından tercih edilmemelidir.
 """
a, b, c = 2, 3, 4
print(a, b, c)
#Tek satırda birden fazla değişken tanımlanabilir.
name = "irem"
print(type(name))
isStudent = True
print(type(isStudent))
a, b, name, isStudent = 1, 2, "irem", True
print(a, b, name, isStudent)

#int
#float
#str
#bool
age = 19
weight = 54.4
name = "irem"
isStudent = True
print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))
#int to float (int in floata dönüştürülmesi)
reuslt = float(age)
print(reuslt)
#float to int
result = int(weight)
print(result)
#str to bool
result = str(isStudent)
print(result)
print(type(result))
#bool to int
#Eğer bool değerimiz true ise int'te 1'e,false ise 0'a denk gelir.
result = int(isStudent)  
print(result)