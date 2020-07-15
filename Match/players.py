class Players():
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

    def __init__(self, home, away):
      self.home = home
      self.away = away

    @classmethod
    def select_random(cls):
        """
        selects the team lineups for both home and way
        selects the attacking team, opposing team, player with ball, defender, and gk
        """
        cls.home_team = cls.teams_dict[self.home]
        cls.away_team = cls.teams_dict[self.away]
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
