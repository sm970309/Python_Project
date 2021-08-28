import pygame

#원을 그려주는 함수
def display_start_screen():
    pygame.draw.circle(screen,WHITE,start_button.center,60,5)
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):      #start버튼의 좌표값
        start = True
def display_game_screen():
    print("game start")

# 초기화 하기
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")

#버튼 만들기
start_button = pygame.Rect(0,0,120,120,)        #사각형 만듦(0,0) 기준으로 120x120 크기로 만듦
start_button.center = (120,screen_height-120)   #해당 버튼에 중앙 설정

#색상 (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)

#게임 시작 여부
start = False

# 게임 루프 만들기(일정 조건 입력 전 까지 무한루프)
running = True
while running:
    click_pos = None
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는지 처리
        if event.type == pygame.QUIT:   #창 닫기 이벤트 발생
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 마우스 클릭 했을 때
            click_pos = pygame.mouse.get_pos()   #클릭한 현재 좌표 위치
            print(click_pos)

    #screen 색 채우기
    screen.fill((BLACK))

    if start:
        pass
        display_game_screen()  #게임화면
    else:
        display_start_screen()  #시작화면

    if click_pos:       # 사용자가 클릭을 하면
        check_buttons(click_pos)

    #화면 계속해서 업데이트
    pygame.display.update()

# 게임 종료 메소드
pygame.quit()