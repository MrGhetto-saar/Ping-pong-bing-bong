import pygame
pygame.init()

scene_lebar = 600
scene_tinggi = 400
scene_judul = "Ballin"
gambar_latar = "XP walpaper.jpeg"
MUSIK_LATAR = "bosnov-ringtone.mp3"
FPS = pygame.time.Clock()
gambar_player = "Sigma_ahh_Teto-removebg.png"
gambar_player2 = "El_Plastic.jpg"
GAME_ON = True
GAME_OVER = False

SCENE = pygame.display.set_mode((scene_lebar, scene_tinggi))
LATAR = pygame.transform.scale(pygame.image.load(gambar_latar),
    (scene_lebar, scene_tinggi))
pygame.display.set_caption(scene_judul)

pygame.mixer.init()
pygame.mixer.music.load(MUSIK_LATAR)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        super().__init__()
        self.lebar = lebar
        self.tinggi = tinggi
        self.gambar = pygame.transform.scale(pygame.image.load(gambar), (self.lebar, self.tinggi))
        self.kecepatan = kecepatan
        self.rect = self.gambar.get_rect() ## ini kotaknya
        self.rect.x = x # posisi X
        self.rect.y = y # posisi Y
    def tampil(self):
        SCENE.blit(self.gambar, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def gerak_kiri(self):
        TOMBOL = pygame.key.get_pressed()
        if TOMBOL[pygame.K_q] and self.rect.y > 0:
            self.rect.y -= self.kecepatan
        if TOMBOL[pygame.K_a] and self.rect.y < scene_tinggi-self.tinggi:
            self.rect.y += self.kecepatan
    def gerak_kanan(self):
        TOMBOL = pygame.key.get_pressed()
        if TOMBOL[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.kecepatan
        if TOMBOL[pygame.K_DOWN] and self.rect.y < scene_tinggi-self.tinggi:
            self.rect.y += self.kecepatan

PLAYER_KIRI = Player(gambar_player,10, 10, 80, 150, 20)
PLAYER_KANAN = Player(gambar_player2, scene_lebar-100, 10, 80, 150, 20)

while GAME_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False

        if GAME_OVER == False:
            SCENE.blit(LATAR, (0,0))
            PLAYER_KANAN.tampil()
            PLAYER_KIRI.tampil()
            PLAYER_KIRI.gerak_kiri()
            PLAYER_KANAN.gerak_kanan()


        FPS.tick(60)
        pygame.display.update()


