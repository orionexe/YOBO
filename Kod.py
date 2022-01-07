
# sisteme giriş kodları #
def giris(kullaniciadi , sifre ) :
    while True :
        x= input("kullanıcı adınızı giriniz: ")
        y= input("şifrenizi giriniz ")
        if x==kullaniciadi and y==sifre :
            print(" ")
            print(f"Giriş başarılı.>>>>>> Hoşgeldiniz {kullaniciadi}<<<<<<")
            print(" ")
            break
        else:
            print("Hatalı kullanıcı adı veya şifre.")
            
def bakiyesorgu() :
    print(ahmethesap["bakiye"])
ahmethesap={
        "ad-soyad" : "Ahmet YILMAZ" ,
        "kullanıciadi" : "ahmet16" ,
        "sifre" :"1661" ,
        "bakiye" : 5000
}

giris(ahmethesap["kullanıciadi"], ahmethesap["sifre"])

print("Para Çekmek için 1")
print("Para Yatırmak için 2")
print("Bakiye Sorgulamak için 3")
print("Canlı Döviz Kuru için 4")
print("Destek Hattı için 9")
print("İşlem yapmak istemiyorsanız 0 a basınız.")
print(" ")

while True :
    islem= input("Yapmak istediginiz islemi seçiniz:")

    if islem == "0" :
        print("Hoşçakalın")
        break
    if islem == "1" :
        cek= int(input("Çekeceğiniz tutarı giriniz:"))
        if ahmethesap["bakiye"] < cek :
            print("Yetersiz Bakiye")
        else :
            ahmethesap["bakiye"] -= cek
            print("İşleminiz tamamlandı")

    elif islem == "2" :
        yatir= int(input("Yatıracağınız tutarı giriniz:"))
        ahmethesap["bakiye"] += yatir
        print("İşleminiz tamamlandı")
    elif islem == "3" :
        bakiyesorgu() 
    elif islem == "9" :
        print("0551 552 4703 numarasını tuşlayarak canlı destek hattımıza ulaşabilirsiniz")
    else:
        print("Hatalı işlem yaptınız.") 
