import pygame
import time
from random import *

def display_start_screen():
    global level
    # 첫 화면 표시
    start_font = pygame.font.Font(None,60)
    title_font = pygame.font.Font(None,120)
    # 원 그리기
    pygame.draw.circle(screen,WHITE,start_button.center,60,5)

    # 원 위에 텍스트 쓰기
    cell_text = start_font.render("Start", True, WHITE)
    text_circle = cell_text.get_rect(center=start_button.center)
    screen.blit(cell_text, text_circle)

    # 레벨 쓰기
    title = pygame.Rect(0, 0, 600, 200)
    title.center = (640, 240)
    pygame.draw.rect(screen, BLACK, title)

    title_text = title_font.render("LEVEL "+str(level), True, WHITE)
    text_title = title_text.get_rect(center=title.center)
    screen.blit(title_text, text_title)

def display_finished_screen():
    global level,game_over
    title_font1 = pygame.font.Font(None,120)
    title_font2 = pygame.font.Font(None, 60)

    # Game Over 쓰기
    title1 = pygame.Rect(0, 0, 600, 200)
    title1.center = (640, 240)
    pygame.draw.rect(screen, BLACK, title1)

    title_text = title_font1.render("Game Over", True, WHITE)
    text_title = title_text.get_rect(center=title1.center)
    screen.blit(title_text, text_title)
    # 점수 쓰기
    title2 = pygame.Rect(0, 0, 600, 200)
    title2.center = (640, 480)
    pygame.draw.rect(screen, BLACK, title2)

    title2_text = title_font2.render("SCORE: "+str(level), True, WHITE)
    text_title2 = title2_text.get_rect(center=title2.center)
    screen.blit(title2_text, text_title2)
    game_over = True

def check_buttons(pos):
    global start,start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):      #start버튼의 좌표값
        start = True
        start_ticks = pygame.time.get_ticks()  #타이머 시작(현재 시간 저장)
def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
        if elapsed_time > display_time:
            hidden=True

    for idx,rect in enumerate(number_buttons,1):
        if hidden:
            pygame.draw.rect(screen,WHITE,rect)
        else:
            # 숫자 텍스트
            cell_text = game_font.render(str(idx),True,WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            # 스크린에 숫자 그리기
            screen.blit(cell_text,text_rect)

def setup(level):
    global display_time,hidden
    hidden = False
    # 몇 초 동안 보여줄지
    display_time = max(1,5-(level//3))
    # 몇 개의 숫자를 보여줄지
    number_count = min((level//3)+5,20)

    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20

    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    number = 1

    while number<=number_count:
        x = randrange(0,rows)
        y = randrange(0,columns)

        if grid[x][y] == 0:
            grid[x][y] = number
            number += 1

            # grid cell 위치 기준으로 x,y 위치를 구함
            center_x = screen_left_margin+y*cell_size+cell_size/2
            center_y = screen_top_margin + x*cell_size + cell_size/2

            # 숫자 버튼이 들어갈 틀 만들기
            button = pygame.Rect(0,0,button_size,button_size)
            button.center = (center_x,center_y)
            number_buttons.append(button)

    print(grid)
def check_number_buttons(pos):
    global hidden,running
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                display_finished_screen()
            break

# 초기화 하기
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None,120)
# 버튼 만들기
start_button = pygame.Rect(0,0,120,120,)        # 사각형 만듦(0,0) 기준으로 120x120 크기로 만듦
start_button.center = (120,screen_height-120)   # 해당 버튼에 중앙 설정

# 색상 (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)

# 누르는 버튼 리스트
number_buttons = []
display_time = None   # 숫자를 보여주는 시간
start_ticks = None    # 시간 계산

# 게임 시작 여부
start = False
game_over = False
# 숨김 변수
hidden = False
# 레벨 화면 보여주기 위한 변수
first = True
#게임 시작 전 설정
level = 1
setup(level)

# 게임 루프 만들기(일정 조건 입력 전 까지 무한루프)
running = True
while running:
    click_pos = None
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는지 처리
        if event.type == pygame.QUIT:   #창 닫기 이벤트 발생
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 마우스 클릭 했을 때
            click_pos = pygame.mouse.get_pos()   #클릭한 현재 좌표 위치

    #screen 색 채우기
    screen.fill((BLACK))

    if start and not game_over:
        display_game_screen()  #게임화면
    elif not start and not game_over:
        display_start_screen()  #시작화면
    elif game_over:
        display_finished_screen()

    if len(number_buttons) == 0:
        level += 1
        setup(level)
        start = False
    if click_pos:       # 사용자가 클릭을 하면
        check_buttons(click_pos)

    #화면 계속해서 업데이트
    pygame.display.update()

# 게임 종료 메소드
pygame.quit()