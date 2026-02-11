import pygame
import random

pygame.init()

pygame.mixer.init() #Ses ekleyebilmek için


# Ekran Boyutları
genislik = 800
yukseklik = 600
ekran = pygame.display.set_mode((genislik,yukseklik))

# skor değişkeni
skor = 0 

# Yazı tipi ve boyutu
font_buyuk = pygame.font.SysFont("Arial", 64)
font_kucuk = pygame.font.SysFont("Arial", 32)


# Kruvasan ekleme 
kruvasan_resmi = pygame.image.load("kruvasan.png").convert_alpha() # .convert_alpha() eklemek şeffaf kısımları görünmez yapar.

kruvasan_boy = 100
kruvasan_resmi = pygame.transform.scale(kruvasan_resmi, (kruvasan_boy, kruvasan_boy))


pygame.display.set_caption("Hareketli Karakter")

# yem asseti 
yem_resmi = pygame.image.load("kruvasan.png").convert_alpha()
yem_boyut = 70
yem_resmi = pygame.transform.scale(yem_resmi, (yem_boyut, yem_boyut))

# yemlerin başlangıç konumu
yem_x = random.randint(0, genislik - yem_boyut)
yem_y = random.randint(0, yukseklik - yem_boyut)



# Düşman ekleyelim
dusman_resmi = pygame.image.load("kahve.png").convert_alpha()
dusman_boyut = 60
dusman_resmi = pygame.transform.scale(dusman_resmi, (dusman_boyut, dusman_boyut))

# Düşmanların başlangıç konumu
dusman_x = random.randint(0, genislik - dusman_boyut)
dusman_y = -dusman_boyut  # Ekranın üstünden başlasın
dusman_hiz = 4



# Kare (oyuncu) özellikleri
kare_x = 400
kare_y = 300
kare_boyut = 70
hiz = 5 # Kare her tuşa basıldığında kaç piksel gidecek?

# Saat Nesnesi 
# Oyunun hızını saniyede 60 kareye sabitlemek için
saat = pygame.time.Clock() 


# Pencere Başlığı
pygame.display.set_caption("İlk Oyun Pencerem")

font = pygame.font.SysFont("Arial", 32)

# Ses dosyasını ekle
toplama_sesi = pygame.mixer.Sound("toplama_sesi.wav")

calisiyor = True
while calisiyor:
    # Oyunun hızını sabitle (FPS)
    saat.tick(60)
    
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False

    # Hareket Kontrolü (Klavye)
    tuslar = pygame.key.get_pressed()

    if tuslar[pygame.K_LEFT] and kare_x > 0:
        kare_x -= hiz
    if tuslar[pygame.K_RIGHT] and kare_x < genislik - kruvasan_boy:
        kare_x += hiz
    if tuslar[pygame.K_UP] and kare_y >0:
        kare_y -= hiz
    if tuslar[pygame.K_DOWN] and kare_y < yukseklik - kruvasan_boy:
        kare_y += hiz
 
    # Çarpışma kontrolü

    if (kare_x < yem_x + yem_boyut and
        kare_x + kruvasan_boy > yem_x and
        kare_y < yem_y + yem_boyut and 
        kare_y + kruvasan_boy > yem_y):
        
        # Eğer çarptıysa:
        skor += 1
        print(f"Puan: {skor}") 
        toplama_sesi.play()  # Yem alındığında pop sesi çal

        # Yemleri yeni rastgele bir yere ışınla
        yem_x = random.randint(0, genislik - yem_boyut)
        yem_y = random.randint(0, yukseklik - yem_boyut)
    
    # Düşman yukarıdan aşağı doğru hareket etsin 
    dusman_y += dusman_hiz
    
    # En aşağı inince tekrar yukarı çıksın
    if dusman_y > yukseklik:
        dusman_y = -dusman_boyut
        dusman_x = random.randint(0, genislik - dusman_boyut)
    
    # Düşmana çarparsa ne olacak?
    if (kare_x < dusman_x + dusman_boyut and
        kare_x + kruvasan_boy > dusman_x and
        kare_y < dusman_y + dusman_boyut and
        kare_y + kruvasan_boy > dusman_y):

        print("HAHAH! YOU BURN!")
        calisiyor = False # Oyunu kapatır.


    # Arka planı boya
    ekran.fill((241, 215, 198))

    # Yemleri çiz
    ekran.blit(yem_resmi, (yem_x, yem_y))
    # Kruvasanı çiz
    ekran.blit(kruvasan_resmi, (kare_x, kare_y))

    # Skoru ekrana yazdır
    skor_yazisi = font.render(f"Puan: {skor}", True, (111, 78, 55)) # Kahverengi yazı
    ekran.blit(skor_yazisi, (20, 20))

    # Düşmanı çiz
    ekran.blit(dusman_resmi, (dusman_x,dusman_y))

    pygame.display.flip()

pygame.quit()  