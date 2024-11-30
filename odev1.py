#1-markalar adına liste oluşturma
markalar=["toyota", "bmw" , "renault" , "mercedes"]
#2-listedeki eleman sayısını bulma
print(len(markalar))
#3.1- ilk terimi
print(markalar[0])
#3.2- son terimi
print(markalar[3])
#4- renault markasını togg ile güncelle
markalar[2] = "togg"
#5-togg listenin elmanı mı
sonuc = "togg" in markalar
print(sonuc)
#6- listenin sonuna ford ve citroen markalarını ekle
print(markalar + ["ford","citroen"])
#7- son elemanı sil
del(markalar[-1])
print(markalar)
#8- verileri liste içinde sakla
ogrenci1=["Yiğit", "Bilgi", 2010, [70, 80, 90]]
ogrenci2=["Ada", "Bilgi", 2011, [70, 70, 90]]
ogrenci3=["Çınar", "Turan", 2017, [60, 60, 90]]
#9- öğrencilerin yaşlarını hesaplayınız.
yigitinyasi=2024-ogrenci1[2]
adaninyasi=2024-ogrenci2[2]
cinarinyasi=2024-ogrenci3[2]
print(yigitinyasi)
print(adaninyasi)
print(cinarinyasi)
#10- öğrencilerin not ortalaması
yigitinnotortalamasi=(ogrenci1[3][0]+ogrenci1[3][1]+ogrenci1[3][2])/3
adaninnotortalamasi=(ogrenci2[3][0]+ogrenci2[3][1]+ogrenci2[3][2])/3
cinarinnotortalamasi=(ogrenci3[3][0]+ogrenci3[3][1]+ogrenci3[3][2])/3
print(yigitinnotortalamasi)
print(adaninnotortalamasi)
print(cinarinnotortalamasi)