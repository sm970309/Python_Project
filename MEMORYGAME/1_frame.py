import pygame

# 초기화 하기
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프 만들기(일정 조건 입력 전 까지 무한루프)
running = True
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는지 처리
        if event.type == pygame.QUIT:   #창 닫기 이벤트 발생
            running = False

# 게임 종료 메소드
pygame.quit()