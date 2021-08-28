import pygame

#원을 그려주는 함수
def display_start_screen():
    pygame.draw.circle(screen,WHITE,start_button.center,60,5)

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

# 게임 루프 만들기(일정 조건 입력 전 까지 무한루프)
running = True
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는지 처리
        if event.type == pygame.QUIT:   #창 닫기 이벤트 발생
            running = False

    #screen 색 채우기
    screen.fill((BLACK))
    display_start_screen()

    #화면 계속해서 업데이트
    pygame.display.update()

# 게임 종료 메소드
pygame.quit()