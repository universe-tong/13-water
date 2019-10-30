# -*- coding=utf-8 -*-
import pygame
import json
from widget import *
from sys import exit
from funcs import *
from api import *
WHITE = (255, 255, 255)
GREEN = (200, 221, 139)
BLUE = (65, 193, 227)
BLACK = (0, 0, 0)
def draw_card(screen, x, y, card_list = None, card_dirt = None):
    i = 0
    n1 = x
    n2 = y
    if(card_list != None):
        for c in card_list:
            i = i + 1
            screen.blit(card_dirt[c], (n1, n2))
            n1 = n1 + 35
            if i == 3 or i == 8:
                n2 = n2 + 42
                n1 = x
    else:
        for c in range(13):
            i = i + 1
            pygame.draw.rect(screen, BLUE, [n1, n2, 71, 96])
            pygame.draw.rect(screen, BLACK, [n1, n2, 71, 96], 2)
            n1 = n1 + 35
            if i == 3 or i == 8:
                n2 = n2 + 42
                n1 = x
rank_data = [
    {"player_id": 1, "score": 1233, "name": "user1"},
    {"player_id": 2, "score": 145, "name": "user2"},
    {"player_id": 3, "score": 135, "name": "user3"},
    {"player_id": 4, "score": 98, "name": "user4"}
]
# 使用字典 key:value($) 黑桃 spade, (&)红桃 heart,(*/@) 梅花 club, (#) 方块
suites = {'$': 'spade', '&': 'heart', '*': 'club', '#': 'diamond'}
faces = {'A': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10', 'J': '11', 'Q': '12', 'K': '13'}
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 600), 0, 32)  # 创建了一个窗口
    screen.fill(GREEN)
    pygame.display.set_caption("福建十三水")  # 设置窗口标题
    tb_username = TextBox(340, 50, 283, 272)
    tb_password = TextBox(340, 50, 283, 352)
    card_dirt = {}
    for suite in suites:
        for face in faces:
            key = suite + face
            res = 'img/puke/' + suites[suite] + '_' + faces[face] + '.png'
            img = pygame.image.load(res).convert()
            card_dirt[key] = img
    rank_data = []
    history_data = []
    text_list_rank = TextList(rank_data, 167, 395, 5, 3, [304, 304, 256], 49, 1)
    text_list_history = TextList(history_data, 69, 187, 5, 3, [304, 304, 256], 49, 1)
    # 1
    background_screen_main = pygame.image.load('img/background_main.png').convert()
    # 2\3
    background_screen_lore = pygame.image.load('img/background_login&register.png').convert()
    # 4
    background_screen_catalogue = pygame.image.load('img/backgroud_catalogue.png').convert()
    # 5
    background_screen_game = pygame.image.load('img/background_game.png').convert()
    # 6
    background_screen_history = pygame.image.load('img/background_history.png').convert_alpha()
    # 7
    background_screen_ranking = pygame.image.load('img/background_ranking.png').convert_alpha()

# 1
    buttonto_login = Button('img/button_login.png', 167, 456)
    buttonto_register = Button('img/button_register.png', 624, 456)
# 2
    buttonto_screen_login = Button('img/button_login.png', 278, 442)
    buttonto_loginback = Button('img/button_back.png', 479, 442) # 2
# 3
    buttonto_screen_register = Button('img/button_register.png', 278, 442)
    buttonto_registerback = Button('img/button_back.png', 479, 442)
# 4
    buttonto_logout = Button('img/button_exit.png', 740, 10)
    buttonto_begingame = Button('img/button_begingame.png', 27, 212)
    buttonto_history = Button('img/button_history.png', 323, 219)
    buttonto_ranking = Button('img/button_ranking.png', 619, 218)
# 5
    buttonto_exitback = Button('img/button_exitgame.png', 20, 14)
# 6history\7rank
    button_back = Button('img/button_backy.png', 367, 540)

    page = [[] for _ in range(8)]
# enter
    page[1].append(buttonto_login)
    page[1].append(buttonto_register)
# login
    page[2].append(buttonto_screen_login)
    page[2].append(buttonto_loginback)
    page[2].append(tb_username)
    page[2].append(tb_password)
# register
    page[3].append(buttonto_screen_register)
    page[3].append(buttonto_registerback)
    page[3].append(tb_username)
    page[3].append(tb_password)
# main
    page[4].append(buttonto_logout)
    page[4].append(buttonto_begingame)
    page[4].append(buttonto_history)
    page[4].append(buttonto_ranking)
# game
    page[5].append(buttonto_exitback)
# history
    page[6].append(button_back)
    page[6].append(text_list_history)
# ranking
    page[7].append(button_back)
    page[7].append(text_list_rank)
    current_page = 1
    pygame.display.flip()
    p1 = Player('lsyqlelel', '925471206')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                p1.logout()
                exit()
            # keyboard
            if event.type == pygame.KEYDOWN:
                if current_page == 2 or 3:
                    mouse = pygame.mouse.get_pos()
                    if (tb_username.pressed(mouse)):
                        tb_username.key_down(event)
                    if (tb_password.pressed(mouse)):
                        tb_password.key_down(event)
            # mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # 1 主界面
                if current_page == 1:
                    if buttonto_login.pressed(mouse):
                        current_page = 2
                    if buttonto_register.pressed(mouse):
                        current_page = 3
                # 2 登入
                elif current_page == 2:
                    if buttonto_loginback.pressed(mouse):
                        current_page = 1
                    if buttonto_screen_login.pressed(mouse):
                        p1 = Player(tb_username.get_text(), tb_password.get_text())
                        p1.login()
                        if p1.check_login_status():
                            current_page = 4
                # 3 注册
                elif current_page == 3:
                    if buttonto_registerback.pressed(mouse):
                        current_page = 1
                    if buttonto_screen_register.pressed(mouse):
                        p1.registerbang(tb_username.get_text(), tb_password.get_text())
                        if p1.check_register_status():
                            current_page = 2
                # 4 游戏主界面
                elif current_page == 4:
                    if buttonto_logout.pressed(mouse):
                        current_page = 1
                    if buttonto_begingame.pressed(mouse):
                        forcard = p1.getCard()  #getcard函数就是游戏开局标志
                        ans = findAns(forcard)
                        card = ""
                        card = ans[0] + " " + ans[1] + " " + ans[2]
                        card_list = card.split(" ")
                        p1.push = False  # 不要提交手牌
                        current_page = 5
                    if buttonto_ranking.pressed(mouse):
                        current_page = 7
                        rank_data = p1.get_rank()
                        text_list_rank.update(0, rank_data)
                    if buttonto_history.pressed(mouse):
                        current_page = 6
                        history_data = p1.get_history(0, 20, p1.user_id)
                        text_list_history.update(0, history_data)
                # 5 进入游戏
                elif current_page == 5:
                    if buttonto_exitback.pressed(mouse):
                        current_page = 4
                # 6 历史记录
                elif current_page == 6:
                    if button_back.pressed(mouse):
                        current_page = 4
                # 7 游戏排行榜
                elif current_page == 7:
                    if button_back.pressed(mouse):
                        current_page = 4
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        # display update
        if current_page == 1:
            screen.blit(background_screen_main, (0, 0))
            for w in page[1]:
                w.draw(screen)

        elif current_page == 2:
            screen.blit(background_screen_lore, (0, 0))
            for w in page[2]:
                w.draw(screen)

        elif current_page == 3:
            screen.blit(background_screen_lore, (0, 0))
            for w in page[3]:
                w.draw(screen)

        elif current_page == 4:
            screen.blit(background_screen_catalogue, (0, 0))
            for w in page[4]:
                w.draw(screen)

        elif current_page == 5:
            screen.blit(background_screen_game, (0, 0))
            for w in page[5]:
                w.draw(screen)
            draw_card(screen, 344, 348, card_list, card_dirt)


        elif current_page == 6:
            screen.blit(background_screen_history, (0, 0))
            for w in page[6]:
                w.draw(screen)

        elif current_page == 7:
            screen.blit(background_screen_ranking, (0, 0))
            for w in page[7]:
                w.draw(screen)

        pygame.display.update()
        if (current_page == 5 and p1.push == False):
            p1.push = True

        pygame.time.delay(33)
        pygame.display.flip()
        clock.tick(20)
if __name__ == '__main__':
    main()