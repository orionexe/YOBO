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

    print("Para Çekmek için 1 ")
    print("Para Yatırmak için 2 ")
    print("Bakiye Sorgulamak için 3 ")
    print("Canlı Döviz Kuru için 4")
    print("Destek Hattı için 9")

