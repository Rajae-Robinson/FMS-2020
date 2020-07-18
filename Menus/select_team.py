import pygame, sys
from pygame.locals import *

from Display.display import Display
from Menus.button import Button
from Match.lineups import Lineups

# whether home or away screen is displaying
home_screen = False
away_screen = False

class SelectTeam:
    # class variables for the team lists
    la_liga_team_names = ["REAL MADRID", "BARCELONA", "ATLETICO MADRID", "SEVILLA", "VALENCIA", "GETAFE"]
    bundesliga_team_names = ["BAYERN MUNICH", "DORTMUND", "RB LIEPZIG", "LEVERKUSEN", "WOLFSBURG", "FRANKFURT"]
    premier_team_names = ["MAN. CITY", "LIVERPOOL", "CHELSEA", "TOTTENHAM", "ARSENAL", "MAN. UNITED"]
    ligue1_team_names = ["PSG"]
    serieA_team_names = ["JUVENTUS", "INTER MILAN", "AC MILAN", "AS ROMA", "NAPOLI", "LAZIO"]

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

                     ["SEVILLA", "L. de Jong", "El Haddadi", "Torres", "Jordan", "Fernando R.", "Banega", "Navas",
                   "Kounde", "Diego Carlos", "S. Reguilon", "T. Vaclik", "Y. En-Nesyri", "Suso", "Sergi Gomez", "N/A",
                   "N/A", "N/A"]
                   ]

    serieA_teams = [["AC MILAN", "H. Calhanoglu", "Z. Ibrahimovic", "A. Rebic", "F. Kessie", "L. Biglia", "G. Bonaventura", "T. Hernandez",
                   "M. Musacchio", "A. Romagnoli", "A. Conti", "G. Donnarumma", "S. Castillejo", "R. Krunic", "L. Duarte", "M/A",
                   "N/A", "Z. Ibrahimovic"],

                    ["INTER MILAN", "L. Martinez", "R. Lukaku", "A. Sanchez", "A. Candreva", "C. Eriksen", "M. Vecino", "D. Godin",
                   "M. Skriniar", "S. de Vrij", "D. D'Ambrosio", "S. Handovic", "M. Brozovic", "N. Barella", "A. Bastoni", "N/A",
                   "N/A", "R. Lukaku"],

                    ["JUVENTUS", "Cristiano Ronaldo", "Higuain", "P. Dybala", "B. Matuidi", "R. Bentacur", "A. Ramsey",
                   "A. Sandro", "Chiellini", "Bonucci", "Danilo", "W. Szczesny", "Douglas Costa", "M. De Ligt", "Arthur",
                   "Cristiano Ronaldo", "P. Dybala", "Cristiano Ronaldo"], 

                    ["NAPOLI", "D. Mertens", "K. Insigne", "H. Lozano", "F. Ruiz", "P. Zielinski", "Allan", "Mario Rui", "K. Koulibaly",
                   "Albiol", "Manolas", "D. Ospina", "A. Milik", "Hysaj", "Callejon", "N/A", "Allan", "D. Mertens"],

                    ["AS ROMA", "J. Kluivert", "Dzeko", "Schick", "Under", "N. Zaniolo", "Florenzi", "A. Kolarov", "F. Fazio",
                   "C. Smalling", "Santon", "R. Olsen", "Pastore", "Perotti", "N. Kalinic", "A. Kolarov", "A. Kolarov",
                   "A. Kolarov"],

                    ["LAZIO", "F. Caicedo", "C. Immobile", "J. Correa", "Luis Alberto", "S. Milinkovic-Savic", "Jony", "J. Lukaku",
                   "L. Felipe", "F. Acerbi", "Radu", "T. Strakosha", "L. Leiva", "M. Parolo", "M. Lazzari", "N/A",
                   "N/A", "C. Immobile"]]

    bundesliga_teams = [["BAYERN MUNICH", "L. Sane", "R. Lewandowski", "S. Gnabry", "P. Coutinho", "J. Martinez", "J. Kimmich", "D. Alaba",
                   "L. Hernandez", "N. Sule", "B. Pavard", "M. Neuer", "C. Tolisso", "I. Perisic", "Thiago", "D. Alaba",
                   "D. Alaba", "R. Lewandowski"],

                    ["DORTMUND", "T. Hazard", "E. Haaland", "J. Sancho", "M. Reus", "E. Can", "J. Brandt", "N. Schulz",
                   "M. Hummels", "M. Akanji", "T. Meunier", "R. Burki", "A. Witsel", "T. Delaney", "R. Guerreiro", "J. Sancho",
                   "M. Reus", "E. Haaland"],

                    ["LEVERKUSEN", "L. Bailey", "K. Volland", "M. Diaby", "K. Havertz", "K. Demirbay", "E. Palacios", "Wendell",
                   "S. Bender", "J. Tah", "M. Weiser", "L. Hradecky", "L. Alario", "Paulinho", "N. Amiri", "L. Bailey",
                   "N/A", "K. Volland"],

                    ["RB LIEPZIG", "Y. Poulsen", "J. Augustin", "H. Hwang", "D. Olmo", "K. Kampl", "M. Sabitzer", "M. Halstenberg",
                   "W. Orban", "D. Upamecano", "B. Henrichs", "P. Gulacsi", "O. Bias", "A. Lookman", "F. Hartmann", "N/A",
                   "N/A", "N/A"],

                    ["WOLFSBURG", "J. Brekalo", "W. Weghorst", "R. Steffen", "Y. Gerhardt", "J. Guilavogui", "M. Arnold", "J. Roussillon",
                   "M. Pongracic", "J. Brooks", "William", "K. Casteels", "X. Schlager", "F. Claus", "D. Ginczek", "N/A",
                   "N/A", "W. Weghorst"],

                    ["FRANKFURT", "B. Dost", "A. Silva", "G. Paciencia", "F. Kostic", "D. Kamada", "D. Sow", "T. Chandler",
                   "D. Abraham", "M. Hinteregger", "E. Durm", "K. Trapp", "D. Joveljic", "M. Gacinovic", "S. Rode", "N/A",
                   "N/A", "N/A"]]

    ligue1_teams = [["PSG", "Neymar", "M. Icardi", "K. Mbappe", "A. Di Maria", "I. Gueye", "M. Veratti", "L. Kurzawa",
                   "T. Silva", "P. Kimpembe", "T. Kehrer", "K. Navas", "E. Cavani", "J. Draxler", "P. Sarabia", "Neymar",
                   "Neymar", "M. Icardi"]]

    premier_teams = [["MAN. CITY", "R. Sterling", "S. Aguero", "R. Mahrez", "B. Silva", "Fernandinho", "K. De Bruyne", "B. Mendy",
                   "N. Otamendi", "A. Laporte", "K. Walker", "Ederson", "D. Silva", "O. Zinchenko", "Rodri", "K. De Bruyne",
                   "K. De Bruyne", "S. Aguero"],

                    ["MAN. UNITED", "A. Martial", "M. Rashford", "D. James", "B. Fernandes", "P. Pogba", "S. McTominay", "L. Shaw",
                   "E. Bailly", "V. Lindelof", "A. Wan-Bissaka", "D. De Gea", "Fred", "J. Mata", "M. Rojo", "M. Rashford",
                   "P. Pogba", "M. Rashford"],

                    ["LIVERPOOL", "S. Mane", "R. Firmino", "M. Salah", "J. Milner", "Fabinho", "J. Henderson", "Robertson",
                   "J. Matip", "V. Van Dijk", "T. Alexander-Arnold", "Alisson", "J. Gomez", "G. Wijnaldum", "D. Origi", "R. Firminho",
                   "J. Milner", "J. Milner"],

                    ["ARSENAL", "N. Pepe", "P. Aubameyang", "A. Lacazette", "M. Ozil", "D. Ceballos", "M. Guendouzi", "S. Kolasinac",
                   "D. Luiz", "Sokratis", "H. Bellerin", "B. Leno", "L. Torreira", "E. Nketiah", "S. Mustafi", "P. Aubamenyang",
                   "M. Ozil", "P. Aubameyang"],

                    ["CHELSEA", "C. Pulisic", "T. Werner", "H. Ziyech", "M. Kovacic", "N. Kante", "Jorginho", "Emerson",
                   "K. Zouma", "A. Rudiger", "C. Azpilicueta", "Kepa", "Willian", "Pedro", "T. Abraham", "N/A",
                   "N. Kante", "Jorginho"],

                    ["TOTTENHAM", "H. Son", "H. Kane", "L. Moura", "D. Alli", "G. Lo Ceslo", "M. Sissoko", "B. Davis",
                   "T. Alderweireld", "J. Vertonghen", "S. Aurier", "H. LLoris", "E. Lamela", "H. Winks", "T. Ndombele", "N/A",
                   "N/A", "H. Kane"]]

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

            # only one team P.S.G
            if ligue1_teams[0][0] == team:
                teams_dict[team] = ligue1_teams[0]

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

        # The screen that is now showing
        team_screen = "home" if home_screen else "away" 

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

            self.display.display_text(f"Press Spacebar to return to select {team_screen} team league screen", 
                                      self.display.font_small, (200, 500))

            for event in pygame.event.get():
                for tup in text:
                    # checking if they were clicked
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                # tuple(text, text_rect)
                                if tup[1].collidepoint(event.pos):
                                    if self.home_selected:
                                        # setting away team
                                        SelectTeam.away = tup[0]
                                        SelectTeam.away_team = self.teams_dict[SelectTeam.away]
                                        Lineups(SelectTeam.home_team, SelectTeam.away_team).display_lineups()
                                    else:
                                        # setting home team
                                        self.home_selected = True
                                        SelectTeam.home = tup[0]
                                        SelectTeam.home_team = self.teams_dict[SelectTeam.home]
                                        self.select_away()

                # if spacebar is clicked return to previous menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if home_screen:
                            self.select_home()
                        else:
                            self.select_away()

                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    # select home team
    def select_home(self):
        global home_screen
        home_screen = True
        self.display_leagues("home")
            

    # select away team
    def select_away(self):
        global home_screen, away_screen
        away_screen = True
        home_screen = False
        self.display_leagues("away")