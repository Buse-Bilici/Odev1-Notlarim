
# Kullanıcıdan ismini girmesini istiyoruz.
def kullanici_adini_al():
    ad = input("Lütfen adınızı girin: ")
    return ad

# Merhaba mesajımızı yazdırıyoruz
def merhaba_dunya(ad):
    print(f"\nMerhaba {ad}, Yazılım dünyasına hoş geldin!")
    print("Bu, Python programlama dilinde yazılmış bir 'Merhaba Dünya' örneğidir.\n")

# Yazılım dünyasına genel bir bakış
def yazilim_dunyasi():
    print("Yazılım dünyasında aşağıdaki temel kavramlar çok önemlidir:")
    print("- Algoritmalar: Verileri işleme ve problemleri çözme yöntemleridir.")
    print("- Veritabanları: Bilgilerin düzenli bir şekilde saklanmasını sağlar.")
    print("- API'ler (Uygulama Programlama Arayüzleri): Farklı yazılımların birbirleriyle iletişim kurmasını sağlar.\n")

# Kullanıcıdan bir programlama dili seçmesini isteyelim
def dil_secimi():
    print("Yazılım dillerinden birini seçin:")
    print("1 - Python")
    print("2 - JavaScript")
    print("3 - Java")
    print("4 - C")
    secim = input("Seçiminizi 1, 2, 3 veya 4 olarak yapın: ")

    if secim == '1':
        print("\nPython harika bir dil! Kolay öğrenilebilir ve güçlüdür.")
    elif secim == '2':
        print("\nJavaScript web geliştirme için çok popüler bir dildir.")
    elif secim == '3':
        print("\nJava, büyük ölçekli uygulamalar için yaygın olarak kullanılır.")
    elif secim == '4':
        print("\nC dili, düşük seviyeli programlama için idealdir.")
    else:
        print("\nGeçersiz seçim. Lütfen 1, 2, 3 veya 4 arasında bir seçim yapın.\n")

# Programın ana fonksiyonu
def ana_program():
    ad = kullanici_adini_al()
    merhaba_dunya(ad)
    yazilim_dunyasi()
    dil_secimi()

# Programı başlatıyoruz
if __name__ == "__main__":
    ana_program()
