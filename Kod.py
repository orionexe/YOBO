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

    print("para çekmek için 1 ")
    print("para yatırmak için 2 ")
    print("bakiye sorgulamak için 3 ")
    

