import random

#ilk kahraman seçilirse alınıcak hasarları denetleneyen fonksiyon
def hasar1(can1, can2, isim2,saldıran1,saldıran2):
    #while oyuncuların canlarını kontrol eder
    while can1 > 0 and can2 > 0:
        print("———–", saldıran1 ,"Saldırı !! ———–")
        damage1 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
        #1.oyuncu yanlış değer girerse uyarı vericek
        if damage1 < 1 or damage1 > 50:
            print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
            continue
        #1.oyuncu doğru değer verirse else den devam edicek
        else:
            ıhtımal = 100 - damage1
            sans = random.randint(1, 100)
            #if sağlanırsa 1. oyuncu hasar vericek
            if sans <= ıhtımal:
                print(saldıran1,damage1,"hasar verdi!!")
                can2 = can2 - damage1
                can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #2. oyuncuya geçiş
                print("———–", saldıran2, "Saldırı !! ———–")
                damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                if damage2 < 1 or damage2 > 50:
                    #2. oyuncu yanlış değer girerse kod burdan çalışmaya devam edicek
                    while damage2 < 1 or damage2 > 50:
                        print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
                        print("———–", saldıran2, "Saldırı !! ———–")
                        damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                    else:
                        ıhtımal = 100 - damage2
                        sans = random.randint(1, 100)
                        #if sağlanırsa 2. oyuncu hasar vericek
                        if sans <= ıhtımal:
                            print(saldıran2,damage2,"hasar verdi!!")
                            can1 = can1 - damage2
                            can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                            #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                        elif sans >= ıhtımal:
                            print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                            can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #2. oyuncu doğru değer girerse kod burdan çalışmaya devam edicek
                else:
                    ıhtımal = 100 - damage2
                    sans = random.randint(1, 100)
                    #if sağlanırsa 2. oyuncu hasar vericek
                    if sans <= ıhtımal:
                        print(saldıran2,damage2,"hasar verdi!!")
                        can1 = can1 - damage2
                        can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                        #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                    elif sans >= ıhtımal:
                        print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                        can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
            #elif sağlanırsa 1.oyuncu saldırıyı kaçırıcak
            elif sans >= ıhtımal:
                print("Ooopsy!", saldıran1, "saldırıyı kaçırdı!")
                can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #1.oyuncu saldırıyı kaçırdı ve sıra 2. oyuncuya geçti
                print("———–", saldıran2, "Saldırı !! ———–")
                damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                if damage2 < 1 or damage2 > 50:
                    # 2. oyuncu yanlış değer girerse kod burdan devam edecek
                    while damage2 < 1 or damage2 > 50:
                        print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
                        print("———–", saldıran2, "Saldırı !! ———–")
                        damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                    else:
                        ıhtımal = 100 - damage2
                        sans = random.randint(1, 100)
                        #if sağlanırsa 2.oyuncu hasar verecek
                        if sans <= ıhtımal:
                            print(saldıran2,damage2,"hasar verdi!!")
                            can1 = can1 - damage2
                            can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                        #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                        elif sans >= ıhtımal:
                            print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                            can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #2. oyuncu doğru bir değer girerse kod burdan devam edicek
                else:
                    ıhtımal = 100 - damage2
                    sans = random.randint(1, 100)
                    #if sağlanırsa 2. oyuncu hasar vericek
                    if sans <= ıhtımal:
                        print(saldıran2, damage2, "hasar verdi!!")
                        can1 = can1 - damage2
                        can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
                    #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                    elif sans >= ıhtımal:
                        print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                        can_goster(rumuz1, rumuz2, can1, can2, rumuz1_can_cubuk, rumuz2_can_cubuk)
        if can1 < 1 and can2 < 1:
            #2 oyuncununda canı 0 veya 0ın altına inerse oyun berabere kalıcak
            print("BERABERE")
        elif can2 < 1:
            #2. oyuncunun canı 1in altına inerse oyunu 1. oyuncu kazanıcak
            print("KAZANAN", saldıran1)
        elif can1 < 2:
            #1. oyuncunun canı 1in altına inerse 2. oyuncu kazanacak
            print("KAZANAN", saldıran2)
#ikinci kahraman seçilirse alınıcak hasarları denetleyen fonksiyon
def hasar2(can1, can2, isim2,saldıran1,saldıran2):
    # while oyuncuların canlarını kontrol eder
    while can1 > 0 and can2 > 0:
        print("———–", saldıran1 ,"Saldırı !! ———–")
        damage1 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
        #1.oyuncu yanlış değer girerse uyarı vericek
        if damage1 < 1 or damage1 > 50:
            print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
            continue
        #1.oyuncu doğru değer verirse else den devam ediccek
        else:
            ıhtımal = 100 - damage1
            sans = random.randint(1, 100)
            #if sağlanırsan 1. oyuncu hasar vericek
            if sans <= ıhtımal:
                print(saldıran1, damage1, "hasar verdi!!")
                can2 = can2 - damage1
                can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #ikinci oyuncuya geçiş
                print("———–", saldıran2, "Saldırı !! ———–")
                damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                if damage2 < 1 or damage2 > 50:
                    # 2. oyuncu yanlış bir değer girerse kod burdan devam edicek
                    while damage2 < 1 or damage2 > 50:
                        print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
                        print("———–", saldıran2, "Saldırı !! ———–")
                        damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                    else:
                        ıhtımal = 100 - damage2
                        sans = random.randint(1, 100)
                        # if sağlanırsa 2. oyuncu hasar vericek
                        if sans <= ıhtımal:
                            print(saldıran2, damage2, "hasar verdi!!")
                            can1 = can1 - damage2
                            can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                            #elif sağlanırsa 2. oyuncu saldıryı kaçıracak
                        elif sans >= ıhtımal:
                            print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                            can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #2. oyuncu doğru değer girerse kod çalışmaya burdan devam edicek
                else:
                    ıhtımal = 100 - damage2
                    sans = random.randint(1, 100)
                    #if sağlanırsa 2. oyuncu hasar vericek
                    if sans <= ıhtımal:
                        print(saldıran2, damage2, "hasar verdi!!")
                        can1 = can1 - damage2
                        can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                    #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                    elif sans >= ıhtımal:
                        print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                        can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
            #elif sağlanırsa 1.oyuncu saldırıyı kaçırıcak
            elif sans >= ıhtımal:
                print("Ooopsy!", saldıran1, "saldırıyı kaçırdı!")
                can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #1.oyuncusaldırıyı kaçırdı ve sıra 2. oyuncuya geçti
                print("———–", saldıran2, "Saldırı !! ———–")
                damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                if damage2 < 1 or damage2 > 50:
                    # 2. oyuncu yanlış değer girerse kod burdan devam edecek
                    while damage2 < 1 or damage2 > 50:
                        print("Saldırı Saldırı büyüklüğü 1 ile 50 arasında olmalıdır.")
                        print("———–", saldıran2, "Saldırı !! ———–")
                        damage2 = int(input("Saldırı büyüklüğünüzü 1 ile 50 arasında seçin:"))
                    else:
                        ıhtımal = 100 - damage2
                        sans = random.randint(1, 100)
                        #if sağlanırsa 2. oyuncu hasar vericek
                        if sans <= ıhtımal:
                            print(saldıran2, damage2, "hasar verdi!!")
                            can1 = can1 - damage2
                            can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                        #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                        elif sans >= ıhtımal:
                            print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                            can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                #2. oyuncu doğru bir değer girerse kod çalışmaya burdan devam edicek
                else:
                    ıhtımal = 100 - damage2
                    sans = random.randint(1, 100)
                    #if sağlanırsa 2. oyuncu hasar vericek
                    if sans <= ıhtımal:
                        print(saldıran2, damage2, "hasar verdi!!")
                        can1 = can1 - damage2
                        can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
                    #elif sağlanırsa 2. oyuncu saldırıyı kaçıracak
                    elif sans >= ıhtımal:
                        print("Ooopsy!", saldıran2, "saldırıyı kaçırdı!")
                        can_goster(rumuz1, rumuz2, can2, can1, rumuz1_can_cubuk, rumuz2_can_cubuk)
        if can1<1 and can2<1:
            #2 oyuncunun canıda 0 veya 0ın altına inerse oyun berabere kalıcak
            print("BERABERE")
        elif can2<1:
            #2. oyuncunun canı 1in altına inerse oyunu 1. oyuncu kazanıcak
            print("KAZANAN",saldıran1)
        elif can1<2:
            # 1. oyuncunun canı 1in altına inerse oyunu 2. oyuncu kazanıcak
            print("KAZANAN",saldıran2)
#anlık can değerlerini ekrana yazdırıcak fonksiyon
def can_goster(isim1,isim2,isim1_can,isim2_can,isim1_can_cubuk,isim2_can_cubuk):
    isim1_can_cubuk = int(isim1_can / 2)
    isim2_can_cubuk = int(isim2_can / 2)
    #ilk kahraman seçilirse:
    if isimler == rumuz1:
        print(isim1, ":", "                                                                ", isim2, ":")
        print("HP[", isim1_can, "]:", "|" * isim1_can_cubuk, "         ", "HP[", isim2_can, "]:", "|" * isim2_can_cubuk)
    #ikinci kahraman seçilirse:
    else:
        print(isim2, ":", "                                                                ", isim1, ":")
        print("HP[", isim2_can, "]:", "|" * isim2_can_cubuk, "         ", "HP[", isim1_can, "]:", "|" * isim1_can_cubuk)
#ilk kkahraman seçilirse:
def p1secim():
    if isimler==rumuz1:
        hasar1(rumuz1_can,rumuz2_can,rumuz2,rumuz1,rumuz2)
#ikinci kahraman seçilirse:
def p2secim():
    if isimler==rumuz2:
        hasar2(rumuz1_can,rumuz2_can,rumuz1,rumuz2,rumuz1)
"""kimin seçildiğini ekrana yazdıran, seçilene göre hasar sırasını
belirliyen fonksiyon"""
def yazıtura():
    print("Yazı tura sonucu:", isimler, "önce başlar!")
    can_goster(rumuz1, rumuz2, rumuz1_can, rumuz2_can, rumuz1_can_cubuk, rumuz2_can_cubuk)
    p1secim()
    p2secim()
def rovans():
    tekrar = input("Rövanş oynamak ister misiniz?(evet/hayır)")
    if tekrar==evet:
        yazıtura()
    elif tekrar==hayır:
        print("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
    else:
        print("Geçersiz bir şey girdiniz")
        rovans()


#ilk olarak aldığımız değerler:
print("  ———– İlk Kahraman ———–")
rumuz1=input("Lütfen kahramanınızın adını yazın:")
print("  ———– İkinci Kahraman ———–")
rumuz2=input("Lütfen kahramanınızın adını yazın:")
rumuz1_can=int(100)
rumuz2_can=int(100)
rumuz1_can_cubuk=int(rumuz1_can/2)
rumuz2_can_cubuk=int(rumuz2_can/2)
evet="evet"
hayır="hayır"
#aynı isim seçilmesi durumunda:
while rumuz1==rumuz2:
    print(rumuz1,",alındı, lütfen başka bir isim seçin!")
    print("  ———– İkinci Kahraman ———–")
    rumuz2 = input("Lütfen kahramanınızın adını yazın:")
isimler = random.choice([rumuz1, rumuz2])
yazıtura()
rovans()