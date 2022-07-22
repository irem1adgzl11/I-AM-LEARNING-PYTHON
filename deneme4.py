# stringlerde kullanılan metodlar
yazi = "Benim adım İrem Adıgüzel."
sonuc = yazi.upper()#yazımızın tüm harflerini büyük harf yapar.
sonuc = yazi.lower()#yazımızın tüm harflerini küçük harf yapar.
sonuc = yazi.title()#yazımızın kelimelerinin baş harlerini büyük harf yapar.
sonuc = yazi.capitalize()# yazımızın ilk harfini büyük yapar.
sonuc = yazi.islower()#yazının harflerinin hepsinin küçük olup olmadığını sorarız.bool değer verir.Başına is yazarak 3,4,5,6 daki satırlardaki özellikler,de sorgulayabiliriz.
sonuc = yazi.strip()#yazının başındaki ve sonundaki boşlukları siler.
sonuc = yazi.split(".")#yazıdaki kelimelerden dizi oluşturur.İçine nokta yazarsak cümler halinde dizi oluşturmuş oluruz.
sonuc = "-".join(yazi)#yazıdaki harfler arasında - işareti koyduk.boşluk * vs koyabiliriz.
sonuc = yazi.index("İrem")# yazıda kaçıncı indexten itibaren kelime var onu gösteriyor.
sonuc = yazi.startswith("B")#tırnak işaretinin içine yazdıpımız karakter ile mi başlıyor onu sorguluyoruz.bool değer verir.
sonuc = yazi.endswith(".")#tırnak işaretinin içine yazdıpımız karakter ile mi bitiyor onu sorguluyoruz.bool değer verir.
sonuc = yazi.replace("adım","ismim")#yazi içerisinde kelime değişimi yapmak istediğimizde virgülde önce mevcut kelimeyi virgülden sonra ise istediğimizi yazarız.Bunu karakterler içinde yapabiliriz örneğin yazı içeriisndeki i harflerini ı harfine dönüştürebiliriz.
print(sonuc)
# Daha fazla metod istiyorsak internete "python Strings methods" yazarak bulabiliriz.
