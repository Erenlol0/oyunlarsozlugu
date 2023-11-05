import random

oyunlar_sozlugu = {
    "SPRAY": "Kullanılan silahın sekmesini engelleyerek ateş etmek",
    "NT": "İyi denemeydinin kısaltması anlamına gelir   ",
    "ACE": "Karşı takım oyuncularının 5 tanesinide bir kişinin elemesi durumu",
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()
if word in oyunlar_sozlugu.keys():
    print(oyunlar_sozlugu[word])
elif word == "RANDOM":
    print(random.choice(oyunlar_sozlugu.values()))

else:
    ("Böyle bir kelimemiz bulunmamakta.")
