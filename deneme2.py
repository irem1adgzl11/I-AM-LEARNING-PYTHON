name = "İrem"
surname ="Adıgüzel"
age = "19"
cumle = "Benim adım " + name + " ve Soyadım " + surname + ". " + "Yaşım ise " + age + "."
print(cumle)

#uzunca bir paragrafı yorum satırı yapmak istersek "command k c" yaparız.

password = "abc123"
print(password[0]) # Köşeli parantez password ile 0'ınıcı ya da istediğimiz herhangi bir elemanı yazdırabiliriz.
print(password[-1]) # Sonuncu elemanı yazdırmak istiyorsak tek tek saymaya gerek yok -1 ile yazdırabiliriz. 
print(password[0:3]) # Bir başlangıç ve bitiş noktası belirleyip istediğimiz kadarını yazdırabiliriz.
print(password[:4]) # Başlangıç belirtmeyip baştan istediğimiz yere kadar yazdırabilririz.
print(password[2:]) # Son belirtmeyip istediğimiz elamandan sonuncuya kadar yazdırabiliriz.
print(password[0:5:2]) # Üçüncü bir değer girersek kaçar kaçr gideceğini söylemiş oluruz.
print(password[::-1]) # Başlangıç ve son belirtmeden sondan birer birer yazmasını istemiş oluruz yani yazıyı tersten yazdırmış oluruz.