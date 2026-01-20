import pygame

pygame.init()

# Ekran Boyutları
genislik = 800
yukseklik = 600
ekran = pygame.display.set_mode((genislik,yukseklik))

# Pencere Başlığı
pygame.display.set_caption("İlk Oyun Pencerem")

calisiyor = True
while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False

    ekran.fill((33,44,100))

    pygame.display.flip()

pygame.quit()
