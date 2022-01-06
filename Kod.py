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
            
