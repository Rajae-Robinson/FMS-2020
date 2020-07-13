import pygame, sys
import random
from time import sleep
from pygame.locals import *


"""
Modifications to be made:
- reconsider what should be a class variable and what should be an instance variable
- reconsider the use of class methods
- put all functions related to the game in one class called game; globals, main_menu, draw ect.
- separate this file into multiple modules and use imports

"""

# Initializing
pygame.init()
# Pre-initializing music
pygame.mixer.pre_init(44100, -16, 2, 512)

# Setting color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Setting the FPS
FPS = 30
# clock for game
clock = pygame.time.Clock()

# Setting height and width of screen
HEIGHT = 600
WIDTH = 1000

# Setting display surface
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(WHITE)
pygame.display.set_caption("SMS 2020")

# loading main background
background = pygame.image.load("assets/sprites/background.png").convert()

# loading background for when game begins
field_bkg = pygame.image.load("assets/sprites/play-screen.png").convert()

# goal image
goal_img = pygame.image.load("assets/sprites/goal.jpg").convert()

# Fonts
# title screen
font_title = pygame.font.SysFont('Lato', 45)
# others
font_large = pygame.font.SysFont('Lato', 35)
font_small = pygame.font.SysFont('Lato', 25)
font_extra_small = pygame.font.SysFont('Lato', 20)

# game vars and other vars
home = ""
away = ""
# player who recieved yellow
yellow = []
# Vars to position text
CENTER = (410, 300)
TO_LEFT = (100, 300)

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
        

class Players(Teams):
    all_teams = ["REAL MADRID", "BARCELONA", "ATLETICO MADRID", "SEVILLA", "VALENCIA", "GETAFE",
                "BAYERN MUNICH", "DORTMUND", "RP LIEPZIG", "LEVERKUSEN", "WOLFSBURG", "FRANKFURT",
                 "MAN. CITY", "LIVERPOOL", "CHELSEA", "TOTTENHAM", "ARSENAL", "MAN. UNITED",
                 "PSG", "MARSEILLE", "LYON", "LILLE", "NICE", "MONACO",
                 "JUVENTUS", "INTER MILAN", "AS MILAN", "ROMA", "NAPOLI", "LAZIO"]
     
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

                     ["ATLETICO MADRID", "J. Felix", "Diego Costa", "Saul", "T. Lemar", "Correa", "Koke", "Filipe Luis",
                    "L. Hernandez", "Savic", "S. Arias", "Jan Oblak", "T. Partey", "N. Kalinic", "R. Hernandez",
                    "A. Griezmann", "Koke", "A. Griezmann"],

                     ["VALENCIA", "M. Batshuayi", "Gameiro", "Mina", "Goncalo Guedes", "Kondogbia", "Parejo", "Gaya",
                    "Gabriel", "Garay", "D. Wass", "Neto", "Soler", "T. Lato", "Rodrigo", "Parejo", "Parejo", "Parejo"],

                     ["GETAFE", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"],

                     ["SEVILLA", "E. Hazard", "K. Benzema", "Vinicius Jr.", "T. Kroos", "Casemiro", "L. Modric", "Marcelo",
                   "Varane", "S. Ramos", "D. Carvajal", "T. Courtois", "M. Asensio", "L. Vazquez", "G. Bale", "S. Ramos",
                   "L. Modric", "S. Ramos"]
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


    home_goals = 0
    away_goals = 0

    """
        selects the team lineups for both home and way
        selects the attacking team, opposing team, player with ball, defender, and gk
    """
    @classmethod
    def select_random(cls):
        cls.home_team = cls.teams_dict[home]
        cls.away_team = cls.teams_dict[away]
        teams = [cls.home_team, cls.away_team]

        # selecting attacking team at random
        cls.attacking_team = random.choice(teams)

        # Figuring out which team is not in possession
        if cls.attacking_team == cls.home_team:
            cls.opposing_team = cls.away_team
        else:
            cls.opposing_team = cls.home_team

        # setting the first elevens for both attacking and opposing teams
        cls.atkfirst_eleven = cls.attacking_team[1:12]
        cls.oppfirst_eleven = cls.opposing_team[1:12]

        # players that will attack for the team in possession
        cls.attackers = cls.atkfirst_eleven[0:3]
        cls.midfielders = cls.atkfirst_eleven[3:6]

        player_in_possession = [cls.attackers, cls.midfielders]

        # choosing between the forwards and midfielders
        cls.position = random.choice(player_in_possession)
        cls.player = random.choice(cls.position) #player with the ball

        # if player was removed he cannot have the ball
        while cls.player is None:
            cls.player = random.choice(cls.position)

        # Set-piece takers
        # Checking if the setpiece taker is on the field
        if cls.player in cls.atkfirst_eleven:
            cls.fk_taker = cls.attacking_team[15]
            cls.ck_taker = cls.attacking_team[16]
            cls.pk_taker = cls.attacking_team[17]
        else:
            cls.fk_taker = random.choice(cls.attackers)
            cls.ck_taker = random.choice(cls.midfielders)
            cls.pk_taker = random.choice(cls.attackers)

        # selecting a defender and the goalkeeper of the defending team
        cls.defender = random.choice(cls.oppfirst_eleven[6:10])

        # if defender is removed he cannot be selected
        while cls.defender is None:
            cls.defender = random.choice(cls.oppfirst_eleven[6:10])

        cls.gk = cls.oppfirst_eleven[10]

    # takes team who scroed and player who scored
    @classmethod
    def increase_score(cls, team, player):
        # if player is on home team
        if team[0] in cls.home_team:
            if player in cls.home_team:
                cls.home_goals += 1

        # if player is on away team
        if team[0] in cls.away_team:
            if player in cls.away_team:
                cls.away_goals += 1


class Chances(Players):
    # SHOTS
    # play goal audio, crowd should be louder after goal and show image
    def goal(self, team, player):
        global goal_scored

        Players().increase_score(team, player)
        goal_scored = True

        pygame.mixer.Sound("assets/audio/match/goal.wav").play()

        win.blit(goal_img, (410, 280))
        pygame.display.update()
        sleep(4)

    # play audio when miss
    def miss(self):
        pygame.mixer.Sound("assets/audio/match/miss.wav").play()

    def shot_on_target(self, player):
        goal = random.randint(1, 2)
        corner = random.randint(1, 2)
        if goal == 1:
            self.goal(self.attacking_team, player)
        else:
            game_com(win, f"{self.gk} saves!", font_small, WHITE, TO_LEFT)
            if corner == 1:
                game_com(win, f"{self.gk} did not save the ball cleanly and it goes behind for a corner.", 
                        font_small, WHITE, TO_LEFT)
                self.corner_kick()
                

    # if miss play audio
    def shot_off_target(self):
        r = random.randint(1, 10)
        msg = random.choice(["The ball goes slightly over the bar! Great effort!",
                            "That was nowhere near the goal!",
                            "He hit the crossbar! Unlucky!"])
        self.miss()
        game_com(win, msg, font_small, WHITE, TO_LEFT)
        
    def shoot(self, player):
        r = random.randint(1, 2)
        if r == 1:
            self.shot_on_target(player)
        else:
            self.shot_off_target()

    # PASS/CROSS
    def pass_ball(self):
        # through ball, low cross, high cross
        type_of_pass = random.randint(1, 10)
        volley_or_header = random.randint(1, 2)
        field = self.attacking_team[1:8]

        if self.player in field:
            field.remove(self.player)
        teammate = random.choice(field)

        if type_of_pass >= 1 and type_of_pass < 4:
            game_com(win, f"Great vision from {self.player} to find {teammate} with a pin-point through ball", 
                    font_small, WHITE, TO_LEFT)
            game_com(win, f"{teammate} steadies himself and shoots!...", 
                    font_small, WHITE, TO_LEFT)
            self.shoot(teammate)
        elif type_of_pass > 3 and type_of_pass < 7:
            game_com(win, f"{self.player} finds {teammate} with a low cross", font_small, 
                    WHITE, TO_LEFT)
            game_com(win, f"{teammate} shoots!...", font_small,
                    WHITE, TO_LEFT)
            self.shoot(teammate)
        else:
            game_com(win, f"{self.player} finds {teammate} with a high cross", font_small,
                     WHITE, TO_LEFT)
            if volley_or_header == 1:
                game_com(win, f"{teammate} goes for the volley!", 
                        font_small, WHITE, TO_LEFT)
                self.shoot(teammate)
            else:
                game_com(win, f"{teammate} heads it!", font_small, WHITE, TO_LEFT)
                self.shoot(teammate)


    # DRIBBLE
    def dribble(self):
        event = random.randint(1, 10)
        is_pass = random.randint(1, 2)

        game_com(win, f"{self.player} dribbles with the ball...", font_small, WHITE, TO_LEFT)

        if event >= 1 and event <= 5:
            game_com(win, "Then, he attempts to pass to his teammate.", font_small, WHITE, TO_LEFT)
            if is_pass:
                self.pass_ball()
            else:
                game_com(win, f"{self.defender} intercepts the ball", font_small, WHITE, TO_LEFT)
        elif event >= 6 or event <= 8:
            #solo-goal
            game_com(win, f"{self.player} takes it pass the defender. He's in the box!", font_small, WHITE, TO_LEFT)
            self.shoot(self.player)
        else:
            Foul().play()

    # SETPIECES
    def freekick(self):
        pass_or_shoot = random.randint(1, 2)
        game_com(win, f"{self.attacking_team[0]} gets a freekick. {self.fk_taker} stands over it.", 
                font_small, WHITE, TO_LEFT)

        # pass
        if pass_or_shoot == 1:
            head = random.randint(1, 2)
            headed_goal = random.randint(1, 2)
            # any player except the goalkeeper is in the box
            box = self.atkfirst_eleven[:10]

            # freekick taker is in box remove him
            if self.fk_taker in box:
                box.remove(self.fk_taker)

            teammate = random.choice(box)
            game_com(win, f"{self.fk_taker} tries to find the head of his teammate in the box", 
                    font_small, WHITE, TO_LEFT)

            # ball lands on head
            if head == 1:
                game_com(win, f"{teammate} heads it!", 
                        font_small, WHITE, TO_LEFT)
                # scores
                if headed_goal == 1:
                    self.goal(self.attacking_team, teammate)
                else:
                    game_com(win, "He heads it over the bar.", 
                            font_small, WHITE, TO_LEFT)

            # ball does not find teammmate
            else:
                game_com(win, "The ball flies over the heads of everyone in the box and goes out of play.", 
                        font_small, WHITE, TO_LEFT)

        # Player shoots from freekick
        else:
            shoot = random.randint(1, 3)
            game_com(win, f"{self.fk_taker} goes for goal!...", font_small, WHITE, TO_LEFT)

            # 33.33% chance he scores directly from freekick
            if shoot == 1:
                self.goal(self.attacking_team, self.fk_taker)
            else:
                self.miss()
                game_com(win, "It goes over the bar! Great Effort.",
                         font_small, WHITE, TO_LEFT)

    def penalty(self):
        score = random.randint(1, 2)
        miss = random.choice(["{} misses!".format(self.pk_taker), 
                "{} saves!{}".format(self.gk, self.pk_taker)])

        game_com(win, "The referee points to the spot!", 
                font_small, WHITE, TO_LEFT)
        game_com(win, f"{self.pk_taker} places the ball and steps back...", 
                font_small, WHITE, TO_LEFT)
        game_com(win, f"{self.gk} gets ready to defend his goal", 
                font_small, WHITE, TO_LEFT)
        game_com(win, f"{self.pk_taker} runs up!...", 
                font_small, WHITE, TO_LEFT)
        game_com(win, "He shoots!", font_small, WHITE, TO_LEFT)

        if score:
            self.goal(self.attacking_team, self.pk_taker)
        else:
            self.miss()
            game_com(win, miss, font_small, WHITE, TO_LEFT)
        

    def corner_kick(self):
        success = random.randint(1, 2)
        event = random.randint(1, 10)
        goal = random.randint(1, 2)

        box = self.attacking_team[1:11] # excludes gk

        # remove corner kick taker if he is in the box
        if self.ck_taker in box:
            box.remove(self.ck_taker)

        teammate = random.choice(box)

        game_com(win, f"{self.attacking_team[0]} receives a corner. {self.ck_taker} is going to take it.", 
                font_small, WHITE, TO_LEFT)
        game_com(win, f"{self.ck_taker} whips it into the box!...", 
                font_small, WHITE, TO_LEFT)

        # successful corner attempt
        if success == 1:
            if event >= 1 and event <= 6:
                game_com(win, f"{teammate} jumps and head the ball!", 
                        font_small, WHITE, TO_LEFT)
                if goal == 1:
                    self.goal(self.attacking_team, teammate)
                else:
                    self.miss()
                    game_com(win, "It's over the bar!", 
                            font_small, WHITE, TO_LEFT)
            elif event > 6 and event <= 9:
                game_com(win, f"{teammate} tries a bicycle kick!...", 
                        font_small, WHITE, TO_LEFT)
                if goal == 1:
                    self.goal(self.attacking_team, teammate)
                else:
                    self.miss()
                    game_com(win, "Great effort but it goes slightly over the crossbar! ", 
                            font_small, WHITE, TO_LEFT)
            else:
                if goal == 1:
                    game_com(win, f"{self.ck_taker} goes for goal from the corner flag.", 
                            font_small, WHITE, TO_LEFT)
                    self.goal(self.attacking_team, self.ck_taker)
                else:
                    game_com(win, "The ball fly over the heads of everyone in the box.", 
                            font_small, WHITE, TO_LEFT)
        else:
            game_com(win, "The defender heads it clear. Good defending.", 
                    font_small, WHITE, TO_LEFT)


    # when the two teams are struggling for possession/no chance for goal
    def idle(self):
        msg = random.choice(["Both teams are struggling for possession...", 
            f"{self.home_team[0]} and {self.away_team[0]} are battling it out together...", 
            "We wait for a chance on goal as both teams are currently at a stalemate..."])
        game_com(win, msg, font_small, WHITE, TO_LEFT)

    def play(self):
        # 50% chance player pass 30% chance player shoots 20% he dribbles
        dist = random.randint(20, 30)
        r = random.randint(1, 10)
        game_com(win, f"{self.attacking_team[0]} attacks...", 
                font_small, WHITE, TO_LEFT)

        if r >= 1 and r < 6:
            self.pass_ball()
        elif r >= 6 and r < 9:
            game_com(win, f"{self.player} goes for goal from {dist} yards out!", 
                    font_small, WHITE, TO_LEFT)
            self.shoot(self.player)
        else:
            self.dribble()

class Foul(Players):
    # substitute player if injured
    def injury(self):
        player_index = 0

        # selecting index of substitute
        sub_index = random.randint(12, 14)
        substitute = self.attacking_team[sub_index]

        # checking if substitute has already been used
        while substitute is None:
            sub_index = random.randint(12, 14)
            substitute = self.attacking_team[sub_index]


        game_com(win, f"{self.player} is writhing on the pitch in pain!", 
                font_small, WHITE, TO_LEFT)
        game_com(win, f"{substitute} replaces {self.player}", 
                font_small, WHITE, TO_LEFT)

        # getting the injuired player's index in the first eleven
        for i in range(1, 11):
            if self.attacking_team[i] == self.player:
                player_index = i

        # swapping injuired player for subsitute    
        self.attacking_team[player_index] = substitute
        # removing substitute's name from bench as he is now on the field
        self.attacking_team[sub_index] = None

    def red_card(self):
        player_index = 0

        injury = random.randint(1, 2)

        game_com(win, f"Red Card! {self.defender} receives a red card for his nasty tackle on {self.player}", 
                font_small, WHITE, TO_LEFT)

        # getting the defender's index
        for i in range(1, 11):
            if self.opposing_team[i] == self.defender:
                player_index = i
    
        # removing defender from team
        self.opposing_team[player_index] = None

        if injury == 1:
            self.injury()

    def play(self):
        event = random.randint(1, 10)
        in_box = random.randint(1, 10)

        # 10% chance player is tripped in box
        if in_box == 1:
            game_com(win, f"{self.defender} trips {self.player} in the box!", 
                    font_small, WHITE, TO_LEFT)
            # 50% chance a yellow is given
            if event <= 5:
                game_com(win, f"{self.defender} receives a yellow card!", 
                        font_small, WHITE, TO_LEFT)
                yellow.append(self.defender)
            # 50% chance red is given
            else:
                self.red_card()
            Chances().penalty()

        # 90% chance player is fouled outside of the box
        else:
            game_com(win, f"{self.defender} tackles {self.player} roughly.", 
                    font_small, WHITE, TO_LEFT)
            game_com(win, f"The referee approaches the players...", 
                    font_small, WHITE, TO_LEFT)

            # 40% chance player only gets a warning
            if event < 5:
                game_com(win, f"The referee gives {self.defender} a warning.", 
                        font_small, WHITE, TO_LEFT)
                Chances().freekick()
                
            # 50% chance player recieves a yellow card
            elif event >= 5 and event < 10:
                game_com(win, "Yellow card!", font_small, WHITE, TO_LEFT)
                yellow.append(self.player)

                # if player already recieved yellow he should recieve a yellow card
                if self.defender in yellow:
                    game_com(win, "It's his second yellow!", font_small, WHITE, TO_LEFT)
                    self.red_card()
                    Chances().freekick()
                else:
                    game_com(win, f"{self.defender} will have to be careful now.", font_small, WHITE, TO_LEFT)
                    Chances().freekick()
            # 10% chance player recieves a red
            else:
                self.red_card()
                Chances().freekick()

# displays lineups
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

class Engine(Chances, Foul):
    mins = 1

    @classmethod
    def update_mins(cls):
        cls.mins += 1

    def game(self):
        # crowd audio
        pygame.mixer.music.load('assets/audio/match/atm-normal.wav')
        # play forever
        pygame.mixer.music.play(-1)

        win.fill(BLACK)
        display_background(field_bkg)

        while self.mins <= 90:    
            #rand_events = random.randint(1, 10)
            rand_events = 5

            self.select_random()

            # playing crowd with louder audio
            if self.mins > 25 or self.mins > 75:
                pygame.mixer.Sound("assets/audio/match/atm-loud.wav").play()
            
            if self.mins == 1:
                game_com(win, "Kick Off", font_large, WHITE, CENTER)
                pygame.mixer.Sound('assets/audio/match/whistle.wav').play()
                sleep(3)

            if self.mins == 45:
                game_com(win, "Half Time", font_large, WHITE, CENTER)
                pygame.mixer.Sound('assets/audio/match/whistle.wav').play()
                sleep(3)

            if self.mins == 90:
                game_com(win, "Full Time", font_large, WHITE, CENTER)
                pygame.mixer.Sound('assets/audio/match/whistle.wav').play()
                sleep(3)
                main_menu()
            
            if rand_events == 1:
                Chances().play()
                self.update_mins()
            elif rand_events == 5:
                Foul().play()
                self.update_mins()
            else:
                Chances().idle()
                self.update_mins()
            
            self.update_mins()

            for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()


# handles creation of button images and selecting them
class Button():
    def __init__(self, image, position, size):
        # create surface
        self.image = image

        # get image size and position
        self.rect = pygame.Rect(position, size)

    def draw(self, win):
        # draw image on rect
        win.blit(self.image, self.rect)

    def event_handler(self, event, function):
        # listening for event for start button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if left mouse clicked
            if event.button == 1:
                # if you hover over button
                if self.rect.collidepoint(event.pos):
                    function()

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

def display_background(image):
    # Displaying background to fit screen
    win.blit(pygame.transform.scale(image, (WIDTH, HEIGHT)), (0, 0))

# display text to screen
def display_text(surface, text, font, color, position):
    msg = font.render(text, 1, color)
    text_rect = msg.get_rect()
    text_rect.topleft = position
    surface.blit(msg, text_rect)
    return (text, text_rect)

# game commentary function displays text then sleeps
def game_com(surface, text, font, color, position):
    playersobj = Players()
    engineobj = Engine()
    score = "{} {}-{} {}".format(playersobj.home_team[0], playersobj.home_goals, playersobj.away_goals, playersobj.away_team[0])

    win.fill(BLACK)
    display_background(field_bkg)

    # display scores
    display_text(win, score, font_large, WHITE, (280, 220))

    # display commentary
    display_text(surface, text, font, color, position)

    # display minutes
    display_text(win, f"{engineobj.mins} minutes", font_large, WHITE, (410, 350))
    pygame.display.update()
    # time given to read commentary
    sleep(2)

# draw images to screen
def draw_image(surface, image, position):
    surface.blit(image, position)

def main():
    main_menu()

if __name__ == "__main__":
    main()
