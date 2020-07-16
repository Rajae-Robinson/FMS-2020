import pygame, sys
from pygame.locals import *

from Display.display import Display
from Menus.button import Button
from Match.lineups import Lineups

class SelectTeam:
    # class variables for the team lists
    la_liga_team_names = ["REAL MADRID", "BARCELONA", "ATLETICO MADRID", "SEVILLA", "VALENCIA", "GETAFE"]
    bundesliga_team_names = ["BAYERN MUNICH", "DORTMUND", "RP LIEPZIG", "LEVERKUSEN", "WOLFSBURG", "FRANKFURT"]
    premier_team_names = ["MAN. CITY", "LIVERPOOL", "CHELSEA", "TOTTENHAM", "ARSENAL", "MAN. UNITED"]
    ligue1_team_names = ["PSG", "MARSEILLE", "LYON", "LILLE", "NICE", "MONACO"]
    serieA_team_names = ["JUVENTUS", "INTER MILAN", "AS MILAN", "ROMA", "NAPOLI", "LAZIO"]

    # is both a home and away team selected
    home_selected = False

    all_teams = la_liga_team_names + bundesliga_team_names + premier_team_names + ligue1_team_names + serieA_team_names
     
    """
    list format by index
    0 = team name
    1-3 = attackers
    4-6 = midfielders
    7-10 = defenders
    11 = goalkeeper
    12-14 = substitutes (3 substitutes)
    15 = freekick taker
    16 = cornerkick taker
    17 = penalty taker
    """
    la_liga_teams = [["REAL MADRID", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                     ["BARCELONA", "L. Messi", "L. Suarez", "A. Griezmann", "P. Coutinho", "S. Busquets", "Vidal", "N. Semedo",
                    "Umtiti", "Pique", "J. Alba", "M. ter Stegen", "Pjanic", "O. Dembele", "Sergio Roberto", "L. Messi",
                    "L. Messi", "L. Suarez"],

                     ["ATLETICO MADRID", "J. Felix", "Morata", "Saul", "T. Lemar", "Correa", "Koke", "Lodi",
                    "Hermoso", "Savic", "Trippier", "Jan Oblak", "T. Partey", "N. Llorente", "Diego Costa",
                    "A. Griezmann", "Koke", "A. Griezmann"],

                     ["VALENCIA", "M. Gomez", "Gameiro", "Mina", "Goncalo Guedes", "Kondogbia", "Parejo", "Gaya",
                    "Gabriel", "Garay", "D. Wass", "J. Cillessen", "Soler", "D. Cheryshev", "Rodrigo", "Parejo", "Parejo", "Parejo"],

                     ["GETAFE", "J. Mata", "J. Molina", "Angel Rodriguez", "M. Cucurella", "N. Maksimovic", "Jason", "Olivera",
                   "Timor", "Djene", "Cabaco", "D. Soria", "Duro", "F. Portillo", "A. Ndiaye", "N/A",
                   "N/A", "N/A"],

                     ["SEVILLA", "L. de Jong", "El Haddadi", "Torres", "Jordan", "Fernando R.", "Banega", "Marcelo",
                   "Kounde", "Diego Carlos", "S. Reguilon", "T. Vaclik", "Y. En-Nesyri", "Suso", "Sergi Gomez", "N/A",
                   "N/A", "N/A"]
                   ]

    serieA_teams = [["AS MILAN", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["INTER MILAN", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["JUVENTUS", "Cristiano Ronaldo", "M. Mandzukic", "P. Dybala", "B. Matuidi", "Arthur", "S. Khedira",
                   "A. Sandro", "Chiellini", "Bonucci", "De Sciglio", "W. Szczesny", "Barzagli", "Cancelo", "R. Bentacur",
                   "Cristiano Ronaldo", "P. Dybala", "Cristiano Ronaldo"], 

                    ["NAPOLI", "D. Mertens", "Insigne", "Callejon", "F. Ruiz", "Hamsik", "Allan", "Mario Rui", "K. Koulibaly",
                   "Albiol", "Maksimovic", "D. Ospina", "A. Milik", "Hysaj", "A. Diawara", "Hamsik", "Allan", "D. Mertens"],

                    ["AS ROMA", "J. Kluivert", "Dzeko", "Schick", "Under", "S. N'Zonzi", "Florenzi", "A. Kolarov", "F. Fazio",
                   "Manolas", "Santon", "R. Olsen", "Pastore", "Perotti", "B. Cristante", "A. Kolarov", "A. Kolarov",
                   "A. Kolarov"],

                    ["LAZIO", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"]]

    bundesliga_teams = [["BAYERN MUNICH", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["DORTMUND", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["LEVERKUSEN", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["RP LIEPZIG", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["WOLFSBURG", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["FRANKFURT", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"]]

    ligue1_teams = [["PSG", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["MARSEILLE", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["LILLE", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["NICE", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["LYON", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["MONACO", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"]]

    premier_teams = [["MAN. CITY", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["MAN. UNITED", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["LIVERPOOL", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["ARSENAL", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["CHELSEA", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                    ["TOTTENHAM", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"]]

    teams_dict = {}

    # matching team name to list with lineup in key-value relationship
    # key - team name, value - lineup list
    for team in all_teams:
        for i in range(6):  
            if la_liga_teams[i][0] == team:
                teams_dict[team] = la_liga_teams[i]

            if bundesliga_teams[i][0] == team:
                teams_dict[team] = bundesliga_teams[i]

            if serieA_teams[i][0] == team:
                teams_dict[team] = serieA_teams[i]

            if ligue1_teams[i][0] == team:
                teams_dict[team] = ligue1_teams[i]

            if premier_teams[i][0] == team:
                teams_dict[team] = premier_teams[i]

    # home and away team vars
    home = " "
    away = " "
    # home team and away team list with name of players
    home_team = []
    away_team = []

    def __init__(self):
        self.display = Display()
        self.background = pygame.image.load("assets/sprites/Backgrounds/background.png").convert()

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

    def display_leagues(self, team):
        """
            Show flag buttons for each league
        """

        # load the flag images
        la_liga = Button(pygame.image.load("assets/sprites/Buttons/Flags/spain.png").convert(), (100, 200), (120, 100))
        premier = Button(pygame.image.load("assets/sprites/Buttons/Flags/england.png").convert(), (240, 200), (120, 100))
        bundesliga = Button(pygame.image.load("assets/sprites/Buttons/Flags/germany.png").convert(), (380, 200), (120, 100))
        ligue1 = Button(pygame.image.load("assets/sprites/Buttons/Flags/france.png").convert(), (520, 200), (120, 100))
        serieA = Button(pygame.image.load("assets/sprites/Buttons/Flags/italy.png").convert(), (660, 200), (120, 100))

        while True:
            # displaying the background
            self.display.display_background(self.background)
            self.display.display_text(f"Select {team} team league: ", self.display.font_large, (100, 100))

            # drawing the flags
            la_liga.draw()
            premier.draw()
            bundesliga.draw()
            ligue1.draw()
            serieA.draw()

            # when flag clicked
            for event in pygame.event.get():
                la_liga.event_handler(event, self.la_liga)
                bundesliga.event_handler(event, self.bundesliga)
                premier.event_handler(event, self.premier)
                ligue1.event_handler(event, self.ligue1)
                serieA.event_handler(event, self.serieA)

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


    def display_in_grid(self, team_list):
        """
            List all of the teams in a given league

        """
        text = []

        while True:
            self.display.display_background(self.background)
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

                self.display.display_text(team, self.display.font_small, (x, y))
                text.append(self.display.display_text(team, self.display.font_small, (x, y)))
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
                                        self.away = tup[0]
                                        self.away_team = self.teams_dict[self.away]
                                        Lineups(self.home_team, self.away_team).display_lineups()
                                    else:
                                        # setting home team
                                        self.home_selected = True
                                        self.home = tup[0]
                                        self.home_team = self.teams_dict[self.home]
                                        self.select_away()
            
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    # select home team
    def select_home(self):
        self.display_leagues("home")
            

    # select away team
    def select_away(self):
        self.display_leagues("away")