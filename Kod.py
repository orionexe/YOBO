
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
            print("Hatalı kullanıcı adı veya şifre, Lütfen tekrar deneyiniz.")
            
def bakiyesorgu() :
    print(ahmethesap["bakiye"])
ahmethesap={
        "ad-soyad" : "Ahmet YILMAZ" ,
        "kullanıciadi" : "ahmet16" ,
        "sifre" :"1661" ,
        "Bakiye" : 5000
} 
giris(ahmethesap["kullanıciadi"], ahmethesap["sifre"])

print("Para Çekmek için 1'e basınız")
print("Para Yatırmak için 2'ye basınız")
print("Bakiye Sorgulamak için 3'e basınız")
print("Canlı Döviz Kuru için 4'e basınız")
print("Destek Hattı için 9'a basınız")
print("İşlem yapmak istemiyorsanız 0 a basınız.")
print(" ")

while True :
    islem= input("Yapmak istediginiz islemi seçiniz:")

    if islem == "0" :
        print("Hoşçakalın")
        break
    if islem == "1" :
        cek= int(input("Çekeceğiniz tutarı giriniz:"))
        if ahmethesap["Bakiye"] < cek :
            print("Yetersiz Bakiye")
        else :
            ahmethesap["Bakiye"] -= cek
            print("İşleminiz tamamlandı")

    elif islem == "2" :
        yatir= int(input("Yatıracağınız tutarı giriniz:"))
        ahmethesap["Bakiye"] += yatir
        print("İşleminiz Tamamlandı") 
    elif islem == "3" :
        bakiyesorgu() 
    elif islem == "9" :
        print("0551 552 4703 numarasını tuşlayarak canlı destek hattımıza ulaşabilirsiniz")
    else:
        print("Hatalı işlem yaptınız.") 
