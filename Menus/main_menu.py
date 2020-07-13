# displays main menu
def main_menu():
    # main menu audio
    pygame.mixer.music.load('assets/audio/menu/main_menu.wav')
    # lowering volume
    pygame.mixer.music.set_volume(0.3)
    # play forever
    pygame.mixer.music.play(-1)

    # loading main menu background
    main_menu_img = pygame.image.load("assets/sprites/main-menu.png").convert()

    # creating start button
    start_btn = Button(pygame.image.load("assets/sprites/start-game.png").convert(), (410, 380), (200, 80))

    while True:
        display_background(main_menu_img)
        display_text(win, "Soccer Match Simulator 2020", font_title, WHITE, (250, 300))
        start_btn.draw(win)
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            start_btn.event_handler(event, Teams().select_home)
                    
        pygame.display.update()
        clock.tick(FPS)