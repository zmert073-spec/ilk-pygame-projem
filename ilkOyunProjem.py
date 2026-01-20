import pygame

pygame.init()

# Ekran Boyutları
genislik = 800
yukseklik = 600
ekran = pygame.display.set_mode((genislik,yukseklik))

pygame.display.set_caption("Hareketli Karakter")

# Kare (oyuncu) özellikleri
kare_x = 400
kare_y = 300
kare_boyut = 50 
hiz = 5 # Kare her tuşa basıldığında kaç piksel gidecek?

# Saat Nesnesi 
# Oyunun hızını saniyede 60 kareye sabitlemek için
saat = pygame.time.Clock() 


# Pencere Başlığı
pygame.display.set_caption("İlk Oyun Pencerem")

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
    if tuslar[pygame.K_RIGHT] and kare_x < genislik - kare_boyut:
        kare_x += hiz
    if tuslar[pygame.K_UP] and kare_y >0:
        kare_y -= hiz
    if tuslar[pygame.K_DOWN] and kare_y < yukseklik - kare_boyut:
        kare_y += hiz

    # Arka planı boya
    ekran.fill((33, 44, 100))

    # Ekrana beyaz bir kare çiz
    # pygame.draw.rect(nereye, renk, (x, y, genişlik, yükseklik))

    pygame.draw.rect(ekran, (255,255,255), (kare_x, kare_y, kare_boyut, kare_boyut))


    pygame.display.flip()

pygame.quit()
