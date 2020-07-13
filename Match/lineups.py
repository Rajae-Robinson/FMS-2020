class Lineups(Players):
    def display_players(self):
        # lineup boxs image
        lineup_box = pygame.image.load("assets/sprites/lineup.png").convert()

        # Box for home team
        win.blit(lineup_box, (20, 20))
        # Box for away team 
        win.blit(lineup_box, (600, 20))

        home_team = self.home_team
        away_team = self.away_team

        # vars to postion text
        # home and away team
        hy = 24
        ay = 24

        # Space between names
        SPACE = 40

        # Displaying home team name
        display_text(win, home_team[0], font_small, WHITE, (22, 22))
        # Display names of players on home team
        for i in range(1, 12):
            hy += SPACE
            display_text(win, home_team[i], font_extra_small, WHITE, (22, hy))
            
        # Displaying away team name
        display_text(win, away_team[0], font_small, WHITE, (602, 22))
        # Display names of players on away team
        for i in range(1, 12):
            ay += SPACE
            display_text(win, away_team[i], font_extra_small, WHITE, (602, ay))
            

    def display_lineups(self):
        # menu audio
        pygame.mixer.music.load("assets/audio/match/lineup.wav")
        pygame.mixer.music.play(-1)

        while True:
            win.fill(BLACK)
            display_background(field_bkg)
            self.display_players()
            display_text(win, "Press Spacebar to continue", font_small, WHITE, (400, -5))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # if users presses spacebar start simulator
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Engine().game()

            pygame.display.update()
            clock.tick(FPS)