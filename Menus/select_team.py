class Teams:
    # class variables for the team lists
    la_liga_team_names = ["REAL MADRID", "BARCELONA", "ATLETICO MADRID", "SEVILLA", "VALENCIA", "GETAFE"]
    bundesliga_team_names = ["BAYERN MUNICH", "DORTMUND", "RP LIEPZIG", "LEVERKUSEN", "WOLFSBURG", "FRANKFURT"]
    premier_team_names = ["MAN. CITY", "LIVERPOOL", "CHELSEA", "TOTTENHAM", "ARSENAL", "MAN. UNITED"]
    ligue1_team_names = ["PSG", "MARSEILLE", "LYON", "LILLE", "NICE", "MONACO"]
    serieA_team_names = ["JUVENTUS", "INTER MILAN", "AS MILAN", "ROMA", "NAPOLI", "LAZIO"]

    # is both a home and away team selected
    home_selected = False

    def la_liga(self):
        self.display_in_grid(self.la_liga_team_names)

    def bundesliga(self):
        self.display_in_grid(self.bundesliga_team_names)

    def premier(self):
        self.display_in_grid(self.premier_team_names)

    def ligue1(self):
        self.display_in_grid(self.ligue1_team_names)

    def serieA(self):
        self.display_in_grid(self.serieA_team_names)

    # show flags for each league
    def display_leagues(self):
        # load the flag images
        la_liga = Button(pygame.image.load("assets/sprites/spain.png").convert(), (100, 200), (120, 100))
        premier = Button(pygame.image.load("assets/sprites/england.png").convert(), (240, 200), (120, 100))
        bundesliga = Button(pygame.image.load("assets/sprites/germany.png").convert(), (380, 200), (120, 100))
        ligue1 = Button(pygame.image.load("assets/sprites/france.png").convert(), (520, 200), (120, 100))
        serieA = Button(pygame.image.load("assets/sprites/italy.png").convert(), (660, 200), (120, 100))

        # drawing the flags
        la_liga.draw(win)
        premier.draw(win)
        bundesliga.draw(win)
        ligue1.draw(win)
        serieA.draw(win)

        # when flag clicked
        for event in pygame.event.get():
            la_liga.event_handler(event, self.la_liga)
            bundesliga.event_handler(event, self.bundesliga)
            premier.event_handler(event, self.premier)
            ligue1.event_handler(event, self.ligue1)
            serieA.event_handler(event, self.serieA)

    # game_com list of teams in a league
    def display_in_grid(self, team_list):
        global home, away
        text = []

        while True:
            win.fill(BLACK)
            display_background(background)
            COLUMN_WIDTH = 200
            ROW_WIDTH = 50
            x = 100
            y = 200
            # number of teams in row
            row = 0
            # index of team
            i = 0

            # displaying teams in 3 x 2 grid
            for team in team_list:
                # when 3 teams in row move to new column
                if row == 3:
                    x = 100
                    y += ROW_WIDTH

                display_text(win, team, font_small, WHITE, (x, y))
                text.append(display_text(win, team, font_small, WHITE, (x, y)))
                x += COLUMN_WIDTH
                row += 1
                i += 1
            
            # checking if they were clicked
            for event in pygame.event.get():
                for tup in text:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                # tuple(text, text_rect)
                                if tup[1].collidepoint(event.pos):
                                    if self.home_selected:
                                        # setting away team
                                        away = tup[0]
                                        # run select_random to set class vars for home and away team
                                        Players().select_random()
                                        Lineups().display_lineups()
                                        #Engine().game()
                                    else:
                                        # setting home team
                                        self.home_selected = True
                                        home = tup[0]
                                        self.select_away()
            
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            clock.tick(FPS)

    # select home team
    def select_home(self):
        while True:
            win.fill(BLACK)
            display_background(background)
            display_text(win, "Select home team league: ", font_large, WHITE, (100, 100))
            self.display_leagues()
            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(FPS)

    # select away team
    def select_away(self):
        while True:
            win.fill(BLACK)
            display_background(background)
            display_text(win, "Select away team league: ", font_large, WHITE, (100, 100))
            self.display_leagues()
            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(FPS)
