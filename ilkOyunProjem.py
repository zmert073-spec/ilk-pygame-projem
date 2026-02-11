import pygame
import random

pygame.init()
pygame.mixer.init()

# Ekran Boyutları
genislik = 800
yukseklik = 600
ekran = pygame.display.set_mode((genislik, yukseklik))

# Renkler
ARKA_PLAN = (241, 215, 198)
YAZI_RENK = (111, 78, 55)
BITIS_ARKA_PLAN = (50, 50, 50)

# Değişkenler
skor = 0
oyun_durumu = "OYNANIYOR" # "OYNANIYOR" veya "BITTI"

# Assetler (Görseller ve Sesler)
kruvasan_resmi = pygame.image.load("kruvasan.png").convert_alpha()
kruvasan_boy = 100
kruvasan_resmi = pygame.transform.scale(kruvasan_resmi, (kruvasan_boy, kruvasan_boy))

yem_resmi = pygame.image.load("kruvasan.png").convert_alpha()
yem_boyut = 70
yem_resmi = pygame.transform.scale(yem_resmi, (yem_boyut, yem_boyut))

dusman_resmi = pygame.image.load("kahve.png").convert_alpha()
dusman_boyut = 60
dusman_resmi = pygame.transform.scale(dusman_resmi, (dusman_boyut, dusman_boyut))

toplama_sesi = pygame.mixer.Sound("toplama_sesi.wav")
font = pygame.font.SysFont("Arial", 32)
buyuk_font = pygame.font.SysFont("Arial", 64, bold=True)

# Başlangıç Pozisyonları
def oyunu_sifirla():
    global kare_x, kare_y, yem_x, yem_y, dusman_x, dusman_y, skor, oyun_durumu
    kare_x, kare_y = 400, 300
    yem_x = random.randint(0, genislik - yem_boyut)
    yem_y = random.randint(0, yukseklik - yem_boyut)
    dusman_x = random.randint(0, genislik - dusman_boyut)
    dusman_y = -dusman_boyut
    skor = 0
    oyun_durumu = "OYNANIYOR"

oyunu_sifirla()
hiz = 5
dusman_hiz = 4
saat = pygame.time.Clock()

calisiyor = True
while calisiyor:
    saat.tick(60)
    
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False
        
        # Oyun bittiyse ve R'ye basılırsa sıfırla
        if oyun_durumu == "BITTI" and olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_r:
                oyunu_sifirla()

    if oyun_durumu == "OYNANIYOR":
        # Hareket
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and kare_x > 0: kare_x -= hiz
        if tuslar[pygame.K_RIGHT] and kare_x < genislik - kruvasan_boy: kare_x += hiz
        if tuslar[pygame.K_UP] and kare_y > 0: kare_y -= hiz
        if tuslar[pygame.K_DOWN] and kare_y < yukseklik - kruvasan_boy: kare_y += hiz

        # Yem toplama
        if (kare_x < yem_x + yem_boyut and kare_x + kruvasan_boy > yem_x and
            kare_y < yem_y + yem_boyut and kare_y + kruvasan_boy > yem_y):
            skor += 1
            toplama_sesi.play()
            yem_x = random.randint(0, genislik - yem_boyut)
            yem_y = random.randint(0, yukseklik - yem_boyut)

        # Düşman hareketi
        dusman_y += dusman_hiz
        if dusman_y > yukseklik:
            dusman_y = -dusman_boyut
            dusman_x = random.randint(0, genislik - dusman_boyut)

        # Yanma kontrolü
        if (kare_x < dusman_x + dusman_boyut and kare_x + kruvasan_boy > dusman_x and
            kare_y < dusman_y + dusman_boyut and kare_y + kruvasan_boy > dusman_y):
            oyun_durumu = "BITTI"

        # Çizim (Oyun Alanı)
        ekran.fill(ARKA_PLAN)
        ekran.blit(yem_resmi, (yem_x, yem_y))
        ekran.blit(kruvasan_resmi, (kare_x, kare_y))
        ekran.blit(dusman_resmi, (dusman_x, dusman_y))
        skor_yazisi = font.render(f"Puan: {skor}", True, YAZI_RENK)
        ekran.blit(skor_yazisi, (20, 20))

    elif oyun_durumu == "BITTI":
        # Çizim (Bitiş Ekranı)
        ekran.fill(BITIS_ARKA_PLAN)
        
        mesaj = buyuk_font.render("HAHAH! YOU BURN!", True, (255, 50, 50))
        ekran.blit(mesaj, (genislik//2 - 250, 200))
        
        skor_sonuc = font.render(f"Final Skoru: {skor}", True, (255, 255, 255))
        ekran.blit(skor_sonuc, (genislik//2 - 80, 300))
        
        tekrar_yazi = font.render("Yeniden baslamak icin 'R' tusuna bas", True, (200, 200, 200))
        ekran.blit(tekrar_yazi, (genislik//2 - 200, 400))

    pygame.display.flip()

pygame.quit()