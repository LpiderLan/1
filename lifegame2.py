import sys
import random
import copy
import pygame

chess_number = 20  # 设置棋盘大小
LIVEDENSITY = 1  # 生命密度
TICK = 0.5  # 帧数
BG = (255, 255, 255)
# BG = (20, 20, 20)  # 背景色
LINECOLOR = (52, 53, 46)  # 网格色
LIFECOLOR = (31, 97, 189)  # 活细胞的颜色
black = (0, 0, 0)
CELL_LENGTH = int(600 / chess_number)  # 每个格子的像素大小
LINE_WIDTH = 2  # 线的宽度
START_POSX = 50
START_POSY = 50
gameDisplay = pygame.display.set_mode((chess_number, chess_number))
# 设置背景框大小
size = width, \
       height = 2 * START_POSX + chess_number * CELL_LENGTH, \
                2 * START_POSY + chess_number * CELL_LENGTH
# 设置帧率，返回clock 类
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Accelerator made")


# 画
def draw(livcell):
    '''
    进行一次绘画操作，可以理解为进行一帧操作所更新的画面
    param:操作前活细胞图
    return:操作后活细胞图
    '''
    for i in range(chess_number + 1):
        pygame.draw.line(screen, LINECOLOR, (START_POSX, START_POSY + i * CELL_LENGTH),
                         (START_POSX + chess_number * CELL_LENGTH,
                          START_POSY + i * CELL_LENGTH), LINE_WIDTH)  # 横线
        pygame.draw.line(screen, LINECOLOR, (START_POSX + i * CELL_LENGTH, START_POSY),
                         (START_POSX + i * CELL_LENGTH,
                          START_POSY + chess_number * CELL_LENGTH), LINE_WIDTH)  # 竖线#
    # 画活细胞
    livcell = rule(livcell)
    print('drawnew', livcell)
    return livcell


def drawcell(i, j, cellkind):
    '''
    画出一个具体的方块
    param:行，列，方块颜色种类
    '''
    pygame.draw.rect(screen, cellkind,
                     [START_POSX + CELL_LENGTH * j + (LINE_WIDTH - 1),
                      START_POSY + CELL_LENGTH * i + (LINE_WIDTH - 1),
                      CELL_LENGTH - LINE_WIDTH, CELL_LENGTH - LINE_WIDTH], 0)
    # 终点.  Rect(left,top,width,height)


def creatlife(density):
    '''
    在初始状态下创造生命
    param:所要求生成生命细胞的密度
    return:初始生命细胞的位置图
    '''
    livcell = [[0] * chess_number for i in range(chess_number)]
    for i in range(chess_number):
        for j in range(chess_number):
            pwall = random.random()
            if pwall < density:
                livcell[i][j] = 1
    return livcell


def neighborcell(pos):
    '''
    获得一个细胞周围的细胞位置，并且存入数组
    param:细胞的位置
    return:这个细胞所有的邻居细胞
    '''
    neighborlist = []
    x_1 = pos[0]
    y_1 = pos[1]
    neighborlist = [[x_1 - 1], [x_1 - 1, y_1], [x_1 - 1, y_1 + 1], [x_1, y_1 - 1],
                    [x_1, y_1 + 1], [x_1 + 1, y_1 - 1], [x_1 + 1, y_1], [x_1 + 1, y_1 + 1]]

    realnList = copy.deepcopy(neighborlist)
    for i in neighborlist:
        if i[0] < 0 or i[0] > chess_number - 1 or i[1] < 0 or i[1] > chess_number - 1:
            realnList.remove(i)

    return realnList


def rule(livcell):
    '''
    制定生命游戏的游戏规则
    param:一次操作前所有活着细胞的位置
    return:一次操作后所有活着细胞的位置
    '''
    newlivcell = copy.deepcopy(livcell)
    print('livcell', livcell)
    for i in range(chess_number):
        for j in range(chess_number):
            if livcell[i][j] == 1:
                drawcell(i, j, LIFECOLOR)
                alive = 0
                for cell in neighborcell([i, j]):
                    if livcell[cell[0]][cell[1]] == 1:
                        alive += 1
                if alive == 0 or alive == 1:
                    newlivcell[i][j] = 0
                elif alive == 2 or alive == 3:
                    newlivcell[i][j] = 1
                else:
                    newlivcell[i][j] = 0
            else:
                alive = 0
                for cell in neighborcell([i, j]):
                    if livcell[cell[0]][cell[1]] == 1:
                        alive += 1
                if alive == 3:
                    newlivcell[i][j] = 1
    return newlivcell


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def main():
    pygame.init()
    livcell = creatlife(LIVEDENSITY)
    while True:
        for event in pygame.event.get():
            # 查找关闭窗口事件
            if event.type == pygame.QUIT:
                sys.exit()
        # 填充背景色

        screen.fill(BG)
        livcell = draw(livcell)
        # 刷新图s
        pygame.display.flip()
        clock.tick(TICK)


if __name__ == "__main__":
    main()
