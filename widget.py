import pygame

GREEN = (0, 128, 128)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)


# 类：列表
class TextList():
    def __init__(self, data, x, y, limit, Column, w, h, flag, font=None):
        self.data = data
        self.x = x
        self.y = y
        self.limit = limit
        self.Column = Column
        self.w = w
        self.h = h
        self.p = 0
        self.surf = []
        self.rect = []
        self.flag = flag
        self.push = None
        if font is None:
            # self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
            self.font = pygame.font.SysFont('arial', 22)
        else:
            self.font = font

        for item in range(self.Column):
            self.surf.append(pygame.Surface((w[item], self.h)))
            self.surf[item].fill((255, 255, 255))
            self.surf[item].set_alpha(0)

    def update(self, p, data=None):
        self.p = p
        if data != None:
            self.data = data

    def draw(self, screen):
        if (self.flag == 1):
            Laber_draw(str(self.p + 1), screen, 398, 482)

        else:
            Laber_draw(str(self.p + 1), screen, 390, 527)
        y = self.y
        x = self.x
        index = self.p * self.limit
        for _row in range(self.limit):
            x = self.x
            text = ""
            if (index > len(self.data) - 1):
                return
            dirt = self.data[index]
            for item in range(self.Column):
                if self.flag == 1:
                    if item == 0:
                        text = str(dirt["player_id"])
                    elif item == 1:
                        text = str(dirt["name"])
                    else:
                        text = str(dirt["score"])
                else:
                    if item == 0:
                        text = str(dirt["id"])
                    elif item == 1:
                        _list = dirt["card"]
                        text = _list[0] + '  ' + _list[1] + '  ' + _list[2]
                    else:
                        text = str(dirt["score"])
                if self.flag == 2 and item == 1:
                    font = pygame.font.SysFont('arial', 18)
                    text_surf = font.render(text, True, (0, 0, 0))
                else:
                    text_surf = self.font.render(text, True, (0, 0, 0))
                screen.blit(self.surf[item], (x, y))
                # if self.flag == 2 and item == 1:
                #   screen.blit(text_surf, (x , y + (self.h - text_surf.get_height())/2 ),
                #     (0, 0, self.w[item], self.h))
                # else:
                screen.blit(text_surf, (x + (self.w[item] - text_surf.get_width()) / 2,
                                        y + (self.h - text_surf.get_height()) / 2),
                            (0, 0, self.w[item], self.h))
                x += self.w[item]
            y += self.h
            index += 1


# 类：按钮
class Button():
    def __init__(self, img, x, y):
        self.surf = pygame.image.load(img).convert()
        self.rect = self.surf.get_rect()
        self.rect.topleft = x, y

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def draw(self, dest_surf):
        dest_surf.blit(self.surf, self.rect)


# 类：文本框
class TextBox():
    def __init__(self, w, h, x, y, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        :param callback:在文本框按下回车键之后的回调函数
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        self.callback = callback
        # 创建
        self.__surface = pygame.Surface((w, h))
        self.__surface.fill((255, 255, 255))
        self.__surface.set_alpha(200)
        self.rect = self.__surface.get_rect()
        self.rect.topleft = x, y
        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font

    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height()) / 2),
                       (0, 0, self.width, self.height))

    def key_down(self, event):
        unicode = event.unicode
        key = event.key

        # 退位键
        if key == 8:
            self.text = self.text[:-1]
            return
        # 切换大小写键
        if key == 301:
            return
        # 回车键
        if key == 13:
            if self.callback is not None:
                self.callback()
            return
        if unicode != "":
            char = unicode
        else:
            char = chr(key)

        self.text += char

    def get_text(self):
        return self.text

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False





def Laber(self, ttf, size, text, color):
    fontObj = pygame.font.Font(ttf, size)
    textSurfaceObj = fontObj.render(text, True, GREEN, BLUE)
    return textSurfaceObj





def Laber_draw(text, screen, x, y):
    font = pygame.font.SysFont('arial', 12)
    textSurfaceObj = font.render(text, True, (0, 0, 0))
    rect = textSurfaceObj.get_rect()
    rect.center = x, y
    screen.blit(textSurfaceObj, rect)


# 出牌


def draw_card(screen, x, y, card_list=None, card_dirt=None):
    i = 0
    n1 = x
    n2 = y
    if (card_list != None):
        for c in card_list:
            i += 1
            screen.blit(card_dirt[c], (n1, n2))
            n1 += 105
            if i == 3 or i == 8:
                n2 += 40
                n1 = x
    else:
        for c in range(13):
            i += 1
            pygame.draw.rect(screen, GREEN, [n1, n2, 71, 96])
            pygame.draw.rect(screen, BLACK, [n1, n2, 71, 96], 2)
            n1 += 20
            if i == 3 or i == 8:
                n2 += 30
                n1 = x


def callback():
    print("回车测试")
