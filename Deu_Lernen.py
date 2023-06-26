import pygame
import os
import random

pygame.init()
pygame.mixer.init(24000, -8, 1, 2048)

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('德語小火車')

FPS = 60

Position_A = 75
Position_B = 350
Position_C = 625
Position_ABC = [Position_A, Position_B, Position_C]
Position_random_q1 = random.sample(Position_ABC, len(Position_ABC))
Position_random_q2 = random.sample(Position_ABC, len(Position_ABC))


color_dark_gray = (185,185,185)
color_gray = (230,230,230)
color_white = (255, 255, 255)
color_BGmixed = (183, 255, 228)
color_brown = (249, 208, 189)

#神奇的反白製造器
def highlight(V1,V2,V3,V4):
    VV = pygame.Surface((V1,V2))
    VV.set_alpha(V3)
    VV.fill(V4)
    return VV

S1 = highlight(450,250,70,color_white)
S2 = highlight(150,135,60,color_white)#全動物頁 各動物的反白
S3 = highlight(125,75,60,color_dark_gray)#各動物頁 發音車車的反白
S4 = highlight(70,60,60,color_dark_gray)#各動物頁 返回按鈕的反白
S5 = highlight(200,100,60,color_white) #小測驗入口頁 兩按鈕的反白
S6 = highlight(200,120,60,color_white) #小測驗頁 車車的反白
S7 = highlight(180,180,60,color_white) #小測驗頁 物件的反白
S8 = highlight(240,75,60,color_white)
S9 = highlight(310,80,60,color_white)

# 偉大的換頁計數器
SWITCH = 1

SCORE = 0

BG_menu = pygame.image.load(os.path.join('background','background.png')).convert_alpha()
BG_course = pygame.image.load(os.path.join('background','BG_course.jpg')).convert_alpha()

TRUCK = pygame.image.load(os.path.join('material','pink_truck.png'))
arrow = pygame.image.load(os.path.join('material','arrow.png'))
BUTTON = pygame.image.load(os.path.join('material','button.png'))
TITLE1 = pygame.image.load(os.path.join('material','title1.png'))
TITLE2 = pygame.image.load(os.path.join('material','title2.png'))
ANIMAL_P0 = pygame.image.load(os.path.join('background','animal_P0.jpg'))
ANIMAL_P1 = pygame.image.load(os.path.join('background','animal_P1.jpg'))
ANIMAL_P2 = pygame.image.load(os.path.join('background','animal_P2.jpg'))
ANIMAL_P3 = pygame.image.load(os.path.join('background','animal_P3.jpg'))
ANIMAL_P4 = pygame.image.load(os.path.join('background','animal_P4.jpg'))
ANIMAL_P5 = pygame.image.load(os.path.join('background','animal_P5.jpg'))
ANIMAL_P6 = pygame.image.load(os.path.join('background','animal_P6.jpg'))
ANIMAL_P7 = pygame.image.load(os.path.join('background','animal_P7.jpg'))
ANIMAL_P8 = pygame.image.load(os.path.join('background','animal_P8.jpg'))
ANIMAL_P9 = pygame.image.load(os.path.join('background','animal_P9.jpg'))
ANIMAL_P10 = pygame.image.load(os.path.join('background','animal_P10.jpg'))
FRUIT_P0 = pygame.image.load(os.path.join('background','fruit_P0.jpg'))
FRUIT_P1 = pygame.image.load(os.path.join('background','fruit_P1.jpg'))
FRUIT_P2 = pygame.image.load(os.path.join('background','fruit_P2.jpg'))
FRUIT_P3 = pygame.image.load(os.path.join('background','fruit_P3.jpg'))
FRUIT_P4 = pygame.image.load(os.path.join('background','fruit_P4.jpg'))
FRUIT_P5 = pygame.image.load(os.path.join('background','fruit_P5.jpg'))
FRUIT_P6 = pygame.image.load(os.path.join('background','fruit_P6.jpg'))
FRUIT_P7 = pygame.image.load(os.path.join('background','fruit_P7.jpg'))
FRUIT_P8 = pygame.image.load(os.path.join('background','fruit_P8.jpg'))
FRUIT_P9 = pygame.image.load(os.path.join('background','fruit_P9.jpg'))
FRUIT_P10 = pygame.image.load(os.path.join('background','fruit_P10.jpg'))
GRT_P0 = pygame.image.load(os.path.join('background','greeting_P0.jpg'))
GRT_P1 = pygame.image.load(os.path.join('background','greeting_P1.jpg'))
GRT_P2 = pygame.image.load(os.path.join('background','greeting_P2.jpg'))
GRT_P3 = pygame.image.load(os.path.join('background','greeting_P3.jpg'))
GRT_P4 = pygame.image.load(os.path.join('background','greeting_P4.jpg'))
GRT_P5 = pygame.image.load(os.path.join('background','greeting_P5.jpg'))
GRT_P6 = pygame.image.load(os.path.join('background','greeting_P6.jpg'))
GRT_P7 = pygame.image.load(os.path.join('background','greeting_P7.jpg'))
GRT_P8 = pygame.image.load(os.path.join('background','greeting_P8.jpg'))
QUIZ_P0 = pygame.image.load(os.path.join('background','quiz_P0.jpg'))
QUIZ_P1 = pygame.image.load(os.path.join('background','quiz_P1.jpg'))

animal_p1 = pygame.image.load(os.path.join('material','Hund.png'))
animal_p2 = pygame.image.load(os.path.join('material','Katze.png'))
animal_p3 = pygame.image.load(os.path.join('material','Hase.png'))
animal_p4 = pygame.image.load(os.path.join('material','Huhn.png'))
animal_p5 = pygame.image.load(os.path.join('material','Affe.png'))
animal_p6 = pygame.image.load(os.path.join('material','Elefant.png'))
animal_p7 = pygame.image.load(os.path.join('material','Fisch.png'))
animal_p8 = pygame.image.load(os.path.join('material','Kuh.png'))
animal_p9 = pygame.image.load(os.path.join('material','Vogel.png'))
animal_p10 = pygame.image.load(os.path.join('material','Krokodil.png'))
animal_list = [animal_p1, animal_p2, animal_p3, animal_p4, animal_p5, 
               animal_p6, animal_p7, animal_p8, animal_p9, animal_p10]
animal_list_xx = random.sample(animal_list, len(animal_list))

fruit_p1 = pygame.image.load(os.path.join('material','apple.png'))
fruit_p2 = pygame.image.load(os.path.join('material','banana.png'))
fruit_p3 = pygame.image.load(os.path.join('material','pineapple.png'))
fruit_p4 = pygame.image.load(os.path.join('material','cherry.png'))
fruit_p5 = pygame.image.load(os.path.join('material','lemon.png'))
fruit_p6 = pygame.image.load(os.path.join('material','kiwi.png'))
fruit_p7 = pygame.image.load(os.path.join('material','mango.png'))
fruit_p8 = pygame.image.load(os.path.join('material','pear.png'))
fruit_p9 = pygame.image.load(os.path.join('material','strawberry.png'))
fruit_p10 = pygame.image.load(os.path.join('material','melon.png'))
fruit_list = [fruit_p1, fruit_p2, fruit_p3, fruit_p4, fruit_p5,
              fruit_p6, fruit_p7, fruit_p8, fruit_p9, fruit_p10]
fruit_list_xx = random.sample(fruit_list, len(fruit_list))

right = pygame.image.load(os.path.join('material','right.png'))
wrong = pygame.image.load(os.path.join('material','wrong.png'))


#MUSIC = pygame.mixer.Sound(os.path.join('music.mp3'))
Hund = pygame.mixer.Sound(os.path.join('audio','dog.mp3'))
Katze = pygame.mixer.Sound(os.path.join('audio','cat.mp3'))
Hase = pygame.mixer.Sound(os.path.join('audio','rabbit.mp3'))
Huhn = pygame.mixer.Sound(os.path.join('audio','rooster.mp3'))
Affe = pygame.mixer.Sound(os.path.join('audio','monkey.mp3'))
Elefant = pygame.mixer.Sound(os.path.join('audio','elephant.mp3'))
Fisch = pygame.mixer.Sound(os.path.join('audio','fish.mp3'))
Kuh = pygame.mixer.Sound(os.path.join('audio','ox.mp3'))
Vogel = pygame.mixer.Sound(os.path.join('audio','bird.mp3'))
Krokodil = pygame.mixer.Sound(os.path.join('audio','crocodile.mp3'))
Apfel = pygame.mixer.Sound(os.path.join('audio','apple.mp3'))
Banane = pygame.mixer.Sound(os.path.join('audio','banana.mp3'))
Ananas = pygame.mixer.Sound(os.path.join('audio','pineapple.mp3'))
Kirsche = pygame.mixer.Sound(os.path.join('audio','cherry.mp3'))
Zitrone = pygame.mixer.Sound(os.path.join('audio','lemon.mp3'))
Kiwi = pygame.mixer.Sound(os.path.join('audio','kiwi.mp3'))
Mango = pygame.mixer.Sound(os.path.join('audio','mango.mp3'))
Birne = pygame.mixer.Sound(os.path.join('audio','pear.mp3'))
Erdbeere = pygame.mixer.Sound(os.path.join('audio','strawberry.mp3'))
Melone = pygame.mixer.Sound(os.path.join('audio','melon.mp3'))
Guten_Tag = pygame.mixer.Sound(os.path.join('audio','hello.mp3'))
Danke = pygame.mixer.Sound(os.path.join('audio','thank you.mp3'))
Guten_Morgen = pygame.mixer.Sound(os.path.join('audio','good morning.mp3'))
Guten_Abend = pygame.mixer.Sound(os.path.join('audio','good evening.mp3'))
Tschues = pygame.mixer.Sound(os.path.join('audio','bye.mp3'))
Wie_gehts = pygame.mixer.Sound(os.path.join('audio','how are you.mp3'))
Wunderbar = pygame.mixer.Sound(os.path.join('audio','wonderful.mp3'))
Entschuldigung = pygame.mixer.Sound(os.path.join('audio','sorry.mp3'))

audio_animal = [Hund, Katze, Hase, Huhn, Affe, 
          Elefant, Fisch, Kuh, Vogel, Krokodil]
audio_animal_xx = random.sample(audio_animal, len(audio_animal))
audio_fruit = [Apfel, Banane, Ananas, Kirsche, Zitrone, 
               Kiwi, Mango, Birne, Erdbeere, Melone]
audio_fruit_xx = random.sample(audio_fruit, len(audio_fruit))

menu_font = pygame.font.Font("font.ttf", 40)
question_font = pygame.font.Font("font.ttf", 60)
menu_button = menu_font.render("離開遊戲", True, (0, 0, 0))
play_button = menu_font.render('開始遊戲', True, (0, 0, 0))
question1 = question_font.render('你聽到甚麼動物呢?', True, (0, 0, 0))
question2 = question_font.render('你聽到甚麼水果呢?', True, (0, 0, 0))
quiz_result1 = question_font.render('上課要專心喔?', True, (0, 0, 0))
quiz_result2 = question_font.render('很棒!你可以做得更好的!', True, (0, 0, 0))
quiz_result3 = question_font.render('你是德語小天才!!', True, (0, 0, 0))

def draw_menu(): #menu畫一堆東西跟 頁面轉換的計數器
    def draw_menu_item(): #畫反白跟兩顆箭頭
        if WIDTH/2 - menu_button.get_width()/2 <= MP[0] <= WIDTH/2 + menu_button.get_width()/2 and 380 <= MP[1] <= 380+60:
            pygame.draw.rect(WIN,color_gray,[WIDTH/2 - menu_button.get_width()/2,380,160,60])
            WIN.blit(arrow, (WIDTH/2 - menu_button.get_width()/2 - arrow.get_width() - 15, 380))
        if WIDTH/2 - play_button.get_width()/2 <= MP[0] <= WIDTH/2 + play_button.get_width()/2 and 300 <= MP[1] <= 300+60:
            pygame.draw.rect(WIN,color_gray,[WIDTH/2 - play_button.get_width()/2,300,160,60])
            WIN.blit(arrow, (WIDTH/2 - play_button.get_width()/2 - arrow.get_width() - 15, 300))
    if SWITCH == 1:
        WIN.blit(BG_menu, (0,0))
        WIN.blit(TRUCK, (700, 215))
        WIN.blit(TITLE1, (50, 50))
        WIN.blit(TITLE2, (375, 160))
        draw_menu_item()
        #畫兩顆按鈕
        WIN.blit(menu_button, (WIDTH/2 - menu_button.get_width()/2,380))
        WIN.blit(play_button, (WIDTH/2 - play_button.get_width()/2,300))
    elif SWITCH == 2: #select course
        play_window()
    elif SWITCH == 3: #動物
        animal_window()
    elif SWITCH == 4: #水果
        fruit_window()
    elif SWITCH == 5: #問候語
        GRT_window()
    elif SWITCH == 6: #小測驗
        quiz_window()
    elif SWITCH == 301:
        WIN.blit(ANIMAL_P1, (0,0))
        animal_inpage()
    elif SWITCH == 302:
        WIN.blit(ANIMAL_P2, (0,0))
        animal_inpage()
    elif SWITCH == 303:
        WIN.blit(ANIMAL_P3, (0,0))
        animal_inpage()
    elif SWITCH == 304:
        WIN.blit(ANIMAL_P4, (0,0))
        animal_inpage()
    elif SWITCH == 305:
        WIN.blit(ANIMAL_P5, (0,0))
        animal_inpage()
    elif SWITCH == 306:
        WIN.blit(ANIMAL_P6, (0,0))
        animal_inpage()
    elif SWITCH == 307:
        WIN.blit(ANIMAL_P7, (0,0))
        animal_inpage()
    elif SWITCH == 308:
        WIN.blit(ANIMAL_P8, (0,0))
        animal_inpage()
    elif SWITCH == 309:
        WIN.blit(ANIMAL_P9, (0,0))
        animal_inpage()
    elif SWITCH == 310:
         WIN.blit(ANIMAL_P10, (0,0))
         animal_inpage()
    elif SWITCH == 401:
        WIN.blit(FRUIT_P1, (0,0))
        fruit_inpage()
    elif SWITCH == 402:
        WIN.blit(FRUIT_P2, (0,0))
        fruit_inpage()
    elif SWITCH == 403:
        WIN.blit(FRUIT_P3, (0,0))
        fruit_inpage()
    elif SWITCH == 404:
        WIN.blit(FRUIT_P4, (0,0))
        fruit_inpage()
    elif SWITCH == 405:
        WIN.blit(FRUIT_P5, (0,0))
        fruit_inpage()
    elif SWITCH == 406:
        WIN.blit(FRUIT_P6, (0,0))
        fruit_inpage()
    elif SWITCH == 407:
        WIN.blit(FRUIT_P7, (0,0))
        fruit_inpage()
    elif SWITCH == 408:
        WIN.blit(FRUIT_P8, (0,0))
        fruit_inpage()
    elif SWITCH == 409:
        WIN.blit(FRUIT_P9, (0,0))
        fruit_inpage()
    elif SWITCH == 410:
         WIN.blit(FRUIT_P10, (0,0))
         fruit_inpage()
    elif SWITCH == 501:
        WIN.blit(GRT_P1, (0,0))
        GRT_inpage()
    elif SWITCH == 502:
        WIN.blit(GRT_P2, (0,0))
        GRT_inpage()
    elif SWITCH == 503:
        WIN.blit(GRT_P3, (0,0))
        GRT_inpage()
    elif SWITCH == 504:
        WIN.blit(GRT_P4, (0,0))
        GRT_inpage()
    elif SWITCH == 505:
        WIN.blit(GRT_P5, (0,0))
        GRT_inpage()
    elif SWITCH == 506:
        WIN.blit(GRT_P6, (0,0))
        GRT_inpage()
    elif SWITCH == 507:
        WIN.blit(GRT_P7, (0,0))
        GRT_inpage()
    elif SWITCH == 508:
        WIN.blit(GRT_P8, (0,0))
        GRT_inpage()
    elif SWITCH == 601:
        WIN.blit(QUIZ_P1, (0,0))
        WIN.blit(question1, (WIDTH/2 - question1.get_width()/2,10))
        matcher_animal()
        WIN.blit(animal_list[A], (Position_random_q1[0], 280))
        if animal_list[A] == animal_list_xx[0]:
            WIN.blit(animal_list_xx[1], (Position_random_q1[1], 280))
        else:
            WIN.blit(animal_list_xx[0], (Position_random_q1[1], 280))
        if animal_list[A] == animal_list_xx[2]:
            WIN.blit(animal_list_xx[3], (Position_random_q1[2], 280))
        else:
            WIN.blit(animal_list_xx[2], (Position_random_q1[2], 280))
        quiz_inpage()
    elif SWITCH == 602:
        WIN.blit(QUIZ_P1, (0,0))
        WIN.blit(question2, (WIDTH/2 - question1.get_width()/2,10))
        matcher_fruit()
        WIN.blit(fruit_list[D], (Position_random_q2[0], 280))
        if fruit_list[D] == fruit_list_xx[0]:
            WIN.blit(fruit_list_xx[1], (Position_random_q2[1], 280))
        else:
            WIN.blit(fruit_list_xx[0], (Position_random_q2[1], 280))
        if fruit_list[D] == fruit_list_xx[2]:
            WIN.blit(fruit_list_xx[3], (Position_random_q2[2], 280))
        else:
            WIN.blit(fruit_list_xx[2], (Position_random_q2[2], 280))
        quiz_inpage()
    elif SWITCH == 603:
        quiz_result0 = question_font.render('你答對了'+str(SCORE)+'題', True, (0, 0, 0))
        WIN.fill(color_brown)
        WIN.blit(TRUCK, (600, 275))
        WIN.blit(BUTTON, (WIDTH/2 - BUTTON.get_width()/2, 325))
        WIN.blit(quiz_result0, (WIDTH/2 - question1.get_width()/2,100))
        if SCORE == 0:
            WIN.blit(quiz_result1, (WIDTH/2 - question1.get_width()/2,180))
        elif SCORE == 1:
            WIN.blit(quiz_result2, (WIDTH/2 - question1.get_width()/2,180))
        elif SCORE == 2:
            WIN.blit(quiz_result3, (WIDTH/2 - question1.get_width()/2,180))
        if 295 <= MP[0] <= 295+300 and 325 <= MP[1] <= 325+80:
            WIN.blit(S9, (295, 325))
    elif SWITCH == 6011:
        WIN.blit(right, (WIN.blit(right, (WIDTH/2 - right.get_width()/2, HEIGHT/2 - right.get_height()/2))))
        if 330 <= MP[0] <= 330+240 and 290 <= MP[1] <= 290+75:
            WIN.blit(S8, (330,290))
    elif SWITCH == 6012:
        WIN.blit(wrong, (WIN.blit(right, (WIDTH/2 - right.get_width()/2, HEIGHT/2 - right.get_height()/2))))
        if 330 <= MP[0] <= 330+240 and 290 <= MP[1] <= 290+75:
            WIN.blit(S8, (330,290))
    elif SWITCH == 6013:
        WIN.blit(right, (WIN.blit(right, (WIDTH/2 - right.get_width()/2, HEIGHT/2 - right.get_height()/2))))
        if 330 <= MP[0] <= 330+240 and 290 <= MP[1] <= 290+75:
            WIN.blit(S8, (330,290))
    elif SWITCH == 6014:
        WIN.blit(wrong, (WIN.blit(right, (WIDTH/2 - right.get_width()/2, HEIGHT/2 - right.get_height()/2))))
        if 330 <= MP[0] <= 330+240 and 290 <= MP[1] <= 290+75:
            WIN.blit(S8, (330,290))



def click(): #menu用的點擊範圍
    if WIDTH/2 - menu_button.get_width()/2 <= MP[0] <= WIDTH/2 + menu_button.get_width()/2 and 380 <= MP[1] <= 380+60:
        pygame.quit()
    if WIDTH/2 - play_button.get_width()/2 <= MP[0] <= WIDTH/2 + play_button.get_width()/2 and 300 <= MP[1] <= 300+60:
        global SWITCH
        SWITCH = 2
        pygame.time.delay(200)
        draw_menu()

def click_course(): #Page2用的點擊範圍
    global SWITCH
    if 0 <= MP[0] <= 450 and 0 <= MP[1] <= 250:
        SWITCH = 3
        pygame.time.delay(200)
        draw_menu()
    if 450 <= MP[0] <= 900 and 0 <= MP[1] <= 250:
        SWITCH = 4
        pygame.time.delay(200)
        draw_menu()
    if 0 <= MP[0] <= 450 and 250 <= MP[1] <= 500:
        SWITCH = 5
        pygame.time.delay(200)
        draw_menu()
    if 450 <= MP[0] <= 900 and 250 <= MP[1] <= 500:
        SWITCH = 6
        pygame.time.delay(200)
        draw_menu()

def click_animal(): #全動物頁用的點擊範圍
    global SWITCH
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        SWITCH = 2
        pygame.time.delay(200)
        draw_menu()
    if 40 <= MP[0] <= 40+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 301
        pygame.time.delay(200)
        draw_menu()
    if 220 <= MP[0] <= 220+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 302
        pygame.time.delay(200)
        draw_menu()
    if 380 <= MP[0] <= 380+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 303
        pygame.time.delay(200)
        draw_menu()
    if 540 <= MP[0] <= 540+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 304
        pygame.time.delay(200)
        draw_menu()
    if 710 <= MP[0] <= 710+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 305
        pygame.time.delay(200)
        draw_menu()
    if 40 <= MP[0] <= 40+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 306
        pygame.time.delay(200)
        draw_menu()
    if 220 <= MP[0] <= 220+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 307
        pygame.time.delay(200)
        draw_menu()
    if 380 <= MP[0] <= 380+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 308
        pygame.time.delay(200)
        draw_menu()
    if 540 <= MP[0] <= 540+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 309
        pygame.time.delay(200)
        draw_menu()
    if 710 <= MP[0] <= 710+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 310
        pygame.time.delay(200)
        draw_menu()

def click_fruit(): #全水果頁用的點擊範圍
    global SWITCH
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        SWITCH = 2
        pygame.time.delay(200)
        draw_menu()
    if 40 <= MP[0] <= 40+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 401
        pygame.time.delay(200)
        draw_menu()
    if 220 <= MP[0] <= 220+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 402
        pygame.time.delay(200)
        draw_menu()
    if 380 <= MP[0] <= 380+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 403
        pygame.time.delay(200)
        draw_menu()
    if 540 <= MP[0] <= 540+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 404
        pygame.time.delay(200)
        draw_menu()
    if 710 <= MP[0] <= 710+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 405
        pygame.time.delay(200)
        draw_menu()
    if 40 <= MP[0] <= 40+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 406
        pygame.time.delay(200)
        draw_menu()
    if 220 <= MP[0] <= 220+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 407
        pygame.time.delay(200)
        draw_menu()
    if 380 <= MP[0] <= 380+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 408
        pygame.time.delay(200)
        draw_menu()
    if 540 <= MP[0] <= 540+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 409
        pygame.time.delay(200)
        draw_menu()
    if 710 <= MP[0] <= 710+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 410
        pygame.time.delay(200)
        draw_menu()

def click_GRT(): #全問候語頁用的點擊範圍
    global SWITCH
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        SWITCH = 2
        pygame.time.delay(200)
        draw_menu()
    if 40 <= MP[0] <= 40+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 501
        pygame.time.delay(200)
        draw_menu()
    if 260 <= MP[0] <= 260+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 502
        pygame.time.delay(200)
        draw_menu()
    if 480 <= MP[0] <= 480+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 503
        pygame.time.delay(200)
        draw_menu()
    if 710 <= MP[0] <= 710+150 and 125 <= MP[1] <= 125+135:
        SWITCH = 504
        pygame.time.delay(200)
        draw_menu()
    if 40 <= MP[0] <= 40+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 505
        pygame.time.delay(200)
        draw_menu()
    if 260 <= MP[0] <= 260+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 506
        pygame.time.delay(200)
        draw_menu()
    if 480 <= MP[0] <= 480+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 507
        pygame.time.delay(200)
        draw_menu()
    if 710 <= MP[0] <= 710+150 and 315 <= MP[1] <= 315+135:
        SWITCH = 508
        pygame.time.delay(200)
        draw_menu()

def click_quiz():
    global SWITCH
    if 195 <= MP[0] <= 395 and 295 <= MP[1] <= 395:
        SWITCH = 2
        pygame.time.delay(200)
        draw_menu()
    if 505 <= MP[0] <= 705 and 295 <= MP[1] <= 395:
        SWITCH = 601
        pygame.time.delay(200)
        draw_menu()


def click_animal_inpage(): #各動物頁用的點擊範圍
    global SWITCH
    if 500 <= MP[0] <= 500+125 and 360 <= MP[1] <= 360+75:
        if SWITCH == 301:
            Hund.play()
        elif SWITCH == 302:
            Katze.play()
        elif SWITCH == 303:
            Hase.play()
        elif SWITCH == 304:
            Huhn.play()
        elif SWITCH == 305:
            Affe.play()
        elif SWITCH == 306:
            Elefant.play()
        elif SWITCH == 307:
            Fisch.play()
        elif SWITCH == 308:
            Kuh.play()
        elif SWITCH == 309:
            Vogel.play()
        elif SWITCH == 310:
            Krokodil.play()
        pygame.time.delay(1000)
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        SWITCH = 3
        pygame.time.delay(200)
        draw_menu()

def click_fruit_inpage(): #各動物頁用的點擊範圍
    global SWITCH
    if 500 <= MP[0] <= 500+125 and 360 <= MP[1] <= 360+75:
        if SWITCH == 401:
            Apfel.play()
        elif SWITCH == 402:
            Banane.play()
        elif SWITCH == 403:
            Ananas.play()
        elif SWITCH == 404:
            Kirsche.play()
        elif SWITCH == 405:
            Zitrone.play()
        elif SWITCH == 406:
            Kiwi.play()
        elif SWITCH == 407:
            Mango.play()
        elif SWITCH == 408:
            Birne.play()
        elif SWITCH == 409:
            Erdbeere.play()
        elif SWITCH == 410:
            Melone.play()
        pygame.time.delay(1000)
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        SWITCH = 4
        pygame.time.delay(200)
        draw_menu()

def click_GRT_inpage(): #各動物頁用的點擊範圍
    global SWITCH
    if 500 <= MP[0] <= 500+125 and 360 <= MP[1] <= 360+75:
        if SWITCH == 501:
            Guten_Tag.play()
        elif SWITCH == 502:
            Danke.play()
        elif SWITCH == 503:
            Guten_Morgen.play()
        elif SWITCH == 504:
            Guten_Abend.play()
        elif SWITCH == 505:
            Tschues.play()
        elif SWITCH == 506:
            Wie_gehts.play()
        elif SWITCH == 507:
            Wunderbar.play()
        elif SWITCH == 508:
            Entschuldigung.play()
        pygame.time.delay(1000)
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        SWITCH = 5
        pygame.time.delay(200)
        draw_menu()

def matcher_animal():
    global A
    for i in audio_animal:
        if audio_animal_xx[0] == i:
            A = audio_animal.index(i)
        else:
            continue

def matcher_fruit():
    global D
    for i in audio_fruit:
        if audio_fruit_xx[0] == i:
            D = audio_fruit.index(i)
        else:
            continue

def click_quiz_animal():
    global SWITCH
    global SCORE
    if 350 <= MP[0] <= 350+150 and 110 <= MP[1] <= 110+100:
        audio_animal_xx[0].play()
        matcher_animal()
    if Position_random_q1[0] <= MP[0] <= Position_random_q1[0]+180 and 280 <= MP[1] <= 280+180:
        SCORE += 1
        SWITCH = 6011
        draw_menu()
    if Position_random_q1[1] <= MP[0] <= Position_random_q1[1]+180 and 280 <= MP[1] <= 280+180:
        SWITCH = 6012
        draw_menu()
    if Position_random_q1[2] <= MP[0] <= Position_random_q1[2]+180 and 280 <= MP[1] <= 280+180:
        SWITCH = 6012
        draw_menu()
    pygame.time.delay(400)

def click_quiz_fruit():
    global SWITCH
    global SCORE
    if 350 <= MP[0] <= 350+150 and 110 <= MP[1] <= 110+100:
        audio_fruit_xx[0].play()
        matcher_fruit()
    if Position_random_q2[0] <= MP[0] <= Position_random_q2[0]+180 and 280 <= MP[1] <= 280+180:
        SCORE += 1
        SWITCH = 6013
        draw_menu()
    if Position_random_q2[1] <= MP[0] <= Position_random_q2[1]+180 and 280 <= MP[1] <= 280+180:
        SWITCH = 6014
        draw_menu()
    if Position_random_q2[2] <= MP[0] <= Position_random_q2[2]+180 and 280 <= MP[1] <= 280+180:
        SWITCH = 6014
        draw_menu()
    pygame.time.delay(400)

def click_SCORE():
    global SWITCH
    if 295 <= MP[0] <= 295+300 and 325 <= MP[1] <= 325+80:
        SWITCH = 1

def play_window(): #畫page2的東西
    WIN.blit(BG_course, (0,0))
    def draw_course_item():
        if 0 <= MP[0] <= 450 and 0 <= MP[1] <= 250:
            WIN.blit(S1, (0,0))
        if 450 <= MP[0] <= 900 and 0 <= MP[1] <= 250:
            WIN.blit(S1, (450,0))
        if 0 <= MP[0] <= 450 and 250 <= MP[1] <= 500:
            WIN.blit(S1, (0,250))
        if 450 <= MP[0] <= 900 and 250 <= MP[1] <= 500:
            WIN.blit(S1, (450,250))
    draw_course_item()

def animal_window(): #畫全動物頁的東西
    WIN.blit(ANIMAL_P0, (0,0))
    def draw_animal_item(): #反白
        if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
            WIN.blit(S4, (35,15))#返回鍵
        if 40 <= MP[0] <= 40+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (40,125))
        if 220 <= MP[0] <= 220+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (220,125))
        if 380 <= MP[0] <= 380+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (380,125))
        if 540 <= MP[0] <= 540+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (540,125))
        if 710 <= MP[0] <= 710+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (710,125))
        if 40 <= MP[0] <= 40+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (40,315))
        if 220 <= MP[0] <= 220+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (220,315))
        if 380 <= MP[0] <= 380+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (380,315))
        if 540 <= MP[0] <= 540+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (540,315))
        if 710 <= MP[0] <= 710+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (710,315))
    draw_animal_item()

def fruit_window(): #畫全水果頁的東西
    WIN.blit(FRUIT_P0, (0,0))
    def draw_fruit_item(): #反白
        if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
            WIN.blit(S4, (35,15))#返回鍵
        if 40 <= MP[0] <= 40+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (40,125))
        if 220 <= MP[0] <= 220+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (220,125))
        if 380 <= MP[0] <= 380+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (380,125))
        if 540 <= MP[0] <= 540+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (540,125))
        if 710 <= MP[0] <= 710+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (710,125))
        if 40 <= MP[0] <= 40+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (40,315))
        if 220 <= MP[0] <= 220+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (220,315))
        if 380 <= MP[0] <= 380+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (380,315))
        if 540 <= MP[0] <= 540+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (540,315))
        if 710 <= MP[0] <= 710+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (710,315))
    draw_fruit_item()

def GRT_window(): #畫全問候語頁的東西
    WIN.blit(GRT_P0, (0,0))
    def draw_GRT_item(): #反白
        if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
            WIN.blit(S4, (35,15))#返回鍵
        if 40 <= MP[0] <= 40+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (40,125))
        if 260 <= MP[0] <= 260+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (260,125))
        if 480 <= MP[0] <= 480+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (480,125))
        if 710 <= MP[0] <= 710+150 and 125 <= MP[1] <= 125+135:
            WIN.blit(S2, (710,125))
        if 40 <= MP[0] <= 40+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (40,315))
        if 260 <= MP[0] <= 260+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (260,315))
        if 480 <= MP[0] <= 480+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (480,315))
        if 710 <= MP[0] <= 710+150 and 315 <= MP[1] <= 315+135:
            WIN.blit(S2, (710,315))
    draw_GRT_item()

def quiz_window(): #畫小測驗頁的入口
    WIN.blit(QUIZ_P0, (0,0))
    def draw_quiz_item():
        if 195 <= MP[0] <= 395 and 295 <= MP[1] <= 395:
            WIN.blit(S5, (195,295))#返回鍵
        if 505 <= MP[0] <= 705 and 295 <= MP[1] <= 395:
            WIN.blit(S5, (505,295))
    draw_quiz_item()

def animal_inpage(): #各動物頁的反白
    if 500 <= MP[0] <= 500+125 and 360 <= MP[1] <= 360+75:
        WIN.blit(S3, (500,360))
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        WIN.blit(S4, (35,15))

def fruit_inpage(): #各水果頁的反白
    if 500 <= MP[0] <= 500+125 and 360 <= MP[1] <= 360+75:
        WIN.blit(S3, (500,360))
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        WIN.blit(S4, (35,15))

def GRT_inpage(): #各水果頁的反白
    if 500 <= MP[0] <= 500+125 and 360 <= MP[1] <= 360+75:
        WIN.blit(S3, (500,360))
    if 35 <= MP[0] <= 35+75 and 15 <= MP[1] <= 15+60:
        WIN.blit(S4, (35,15))

def quiz_inpage(): #小測驗頁的反白
    if 350 <= MP[0] <= 350+150 and 110 <= MP[1] <= 110+100:
        WIN.blit(S6, (350,110))
    if 70 <= MP[0] <= 70+180 and 280 <= MP[1] <= 280+180:
        WIN.blit(S7, (70,280))
    if 345 <= MP[0] <= 345+180 and 280 <= MP[1] <= 280+180:
        WIN.blit(S7, (345,280))
    if 625 <= MP[0] <= 625+180 and 280 <= MP[1] <= 280+180:
        WIN.blit(S7, (625,280))


def Main():
    
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        #MUSIC.play()
        global MP
        MP = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_menu()
        #按下滑鼠 執行動作
        global SWITCH
        if SWITCH == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click()
        elif SWITCH == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_course()
        elif SWITCH == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_animal()
        elif SWITCH == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_fruit()
        elif SWITCH == 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_GRT()
        elif SWITCH == 6:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_quiz()
        elif 301<= SWITCH <= 310 : 
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_animal_inpage()
        elif 401 <= SWITCH <= 410: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_fruit_inpage()
        elif 501 <= SWITCH <= 508: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_GRT_inpage()
        elif SWITCH == 601:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_quiz_animal()
        elif SWITCH == 602:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_quiz_fruit()
        elif SWITCH == 603:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_SCORE()
                pygame.time.delay(400)
                pygame.quit()
        elif 6011 <= SWITCH <= 6012:
            if event.type == pygame.MOUSEBUTTONDOWN:
                SWITCH = 602
                pygame.time.delay(400)
                draw_menu()
        elif 6013 <= SWITCH <= 6014:
            if event.type == pygame.MOUSEBUTTONDOWN:
                SWITCH = 603
                pygame.time.delay(400)
                draw_menu()
        pygame.display.update()

if __name__ == '__main__':  #only if we run the file, this line will be called.
    Main()
