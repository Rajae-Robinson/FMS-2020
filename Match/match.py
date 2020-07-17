import pygame
import random
import time
from Display.display import Display
from Menus.select_team import SelectTeam
from Match.match_variables import MatchVariables

# player who recieved yellow
yellow = []

goal_img = pygame.image.load("assets/sprites/Match/goal.jpg").convert()

class Players:
    def __init__(self):
        """
            selects the team lineups for both home and way
            selects the attacking team, opposing team, player with ball, defender, and gk
        """
        self.select_team = SelectTeam()
        self.home_team = self.select_team.home_team
        self.away_team = self.select_team.away_team
        # selecting attacking team at random
        self.attacking_team = random.choice([self.home_team, self.away_team])

        # Figuring out which team is not in possession
        if self.attacking_team == self.select_team.home_team:
            self.opposing_team = self.select_team.away_team
        else:
            self.opposing_team = self.select_team.home_team

        # setting the first elevens for both attacking and opposing teams
        self.atkfirst_eleven = self.attacking_team[1:12]
        self.oppfirst_eleven = self.opposing_team[1:12]

        # players that will attack for the team in possession
        self.attackers = self.atkfirst_eleven[0:3]
        self.midfielders = self.atkfirst_eleven[3:6]

        # choosing between the forwards and midfielders
        self.position = random.choice([self.attackers, self.midfielders])
        self.player = random.choice(self.position) #player with the ball

        # if player was removed he cannot have the ball
        while self.player is None:
            self.player = random.choice(self.position)

        # Set-piece takers
        # Checking if the setpiece taker is on the field
        if self.player in self.atkfirst_eleven:
            self.fk_taker = self.attacking_team[15]
            self.ck_taker = self.attacking_team[16]
            self.pk_taker = self.attacking_team[17]
        else:
            self.fk_taker = random.choice(self.attackers)
            self.ck_taker = random.choice(self.midfielders)
            self.pk_taker = random.choice(self.attackers)

        # selecting a defender and the goalkeeper of the defending team
        self.defender = random.choice(self.oppfirst_eleven[6:10])

        # if defender is removed he cannot be selected
        while self.defender is None:
            self.defender = random.choice(self.oppfirst_eleven[6:10])

        # selecting gk
        self.gk = self.oppfirst_eleven[10]


class Chances(Players):
    """
        Deals with a chance on goalnand setpieces
        for e.g
        a shot
        a pass to teammate
        a cross
    """

    def __init__(self):
        super().__init__()
        self.match_vars = MatchVariables()
        self.display = Display()

    # SHOTS
    # play goal audio, crowd should be louder after goal and show image
    def goal(self, team, player):
        self.match_vars.increase_score(team, player)
        goal_scored = True

        pygame.mixer.Sound("assets/audio/match/goal.wav").play()

        self.display.draw_image(goal_img, (410, 280))
        pygame.display.update()
        time.sleep(4)

    # play audio when miss
    def miss(self):
        pygame.mixer.Sound("assets/audio/match/miss.wav").play()

    def shot_on_target(self, player):
        goal = random.randint(1, 2)
        corner = random.randint(1, 2)
        if goal == 1:
            self.goal(self.attacking_team, player)
        else:
            self.display.game_com(f"{self.gk} saves!", self.display.font_small)
            if corner == 1:
                self.display.game_com(f"{self.gk} did not save the ball cleanly and it goes behind for a corner.", 
                        self.display.font_small)
                self.corner_kick()
                

    # if miss play audio
    def shot_off_target(self):
        r = random.randint(1, 10)
        msg = random.choice(["The ball goes slightly over the bar! Great effort!",
                            "That was nowhere near the goal!",
                            "He hit the crossbar! Unlucky!"])
        self.miss()
        self.display.game_com(msg, self.display.font_small)
        
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
            self.display.game_com(f"Great vision from {self.player} to find {teammate} with a pin-point through ball", 
                    self.display.font_small)
            self.display.game_com(f"{teammate} steadies himself and shoots!...", 
                    self.display.font_small)
            self.shoot(teammate)
        elif type_of_pass > 3 and type_of_pass < 7:
            self.display.game_com(f"{self.player} finds {teammate} with a low cross", self.display.font_small)
            self.display.game_com(f"{teammate} shoots!...", self.display.font_small)
            self.shoot(teammate)
        else:
            self.display.game_com(f"{self.player} finds {teammate} with a high cross", self.display.font_small)
            if volley_or_header == 1:
                self.display.game_com(f"{teammate} goes for the volley!", 
                        self.display.font_small)
                self.shoot(teammate)
            else:
                self.display.game_com(f"{teammate} heads it!", self.display.font_small)
                self.shoot(teammate)


    # DRIBBLE
    def dribble(self):
        event = random.randint(1, 10)
        is_pass = random.randint(1, 2)

        self.display.game_com(f"{self.player} dribbles with the ball...", self.display.font_small)

        if event >= 1 and event <= 5:
            self.display.game_com("Then, he attempts to pass to his teammate.", self.display.font_small)
            if is_pass:
                self.pass_ball()
            else:
                self.display.game_com(f"{self.defender} intercepts the ball", self.display.font_small)
        elif event >= 6 or event <= 8:
            #solo-goal
            self.display.game_com(f"{self.player} takes it pass the defender. He's in the box!", self.display.font_small)
            self.shoot(self.player)
        else:
            Foul().play()

    # SETPIECES
    def freekick(self):
        pass_or_shoot = random.randint(1, 2)
        self.display.game_com(f"{self.attacking_team[0]} gets a freekick. {self.fk_taker} stands over it.", 
                self.display.font_small)

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
            self.display.game_com(f"{self.fk_taker} tries to find the head of his teammate in the box", 
                    self.display.font_small)

            # ball lands on head
            if head == 1:
                self.display.game_com(f"{teammate} heads it!", 
                        self.display.font_small)
                # scores
                if headed_goal == 1:
                    self.goal(self.attacking_team, teammate)
                else:
                    self.display.game_com("He heads it over the bar.", 
                            self.display.font_small)

            # ball does not find teammmate
            else:
                self.display.game_com("The ball flies over the heads of everyone in the box and goes out of play.", 
                        self.display.font_small)

        # Player shoots from freekick
        else:
            shoot = random.randint(1, 3)
            self.display.game_com(f"{self.fk_taker} goes for goal!...", self.display.font_small)

            # 33.33% chance he scores directly from freekick
            if shoot == 1:
                self.goal(self.attacking_team, self.fk_taker)
            else:
                self.miss()
                self.display.game_com("It goes over the bar! Great Effort.",
                         self.display.font_small)

    def penalty(self):
        score = random.randint(1, 2)
        miss = random.choice(["{} misses!".format(self.pk_taker), 
                "{} saves!{}".format(self.gk, self.pk_taker)])

        self.display.game_com("The referee points to the spot!", 
                self.display.font_small)
        self.display.game_com(f"{self.pk_taker} places the ball and steps back...", 
                self.display.font_small)
        self.display.game_com(f"{self.gk} gets ready to defend his goal", 
                self.display.font_small)
        self.display.game_com(f"{self.pk_taker} runs up!...", 
                self.display.font_small)
        self.display.game_com("He shoots!", self.display.font_small)

        if score:
            self.goal(self.attacking_team, self.pk_taker)
        else:
            self.miss()
            self.display.game_com(miss, self.display.font_small)
        

    def corner_kick(self):
        success = random.randint(1, 2)
        event = random.randint(1, 10)
        goal = random.randint(1, 2)

        box = self.attacking_team[1:11] # excludes gk

        # remove corner kick taker if he is in the box
        if self.ck_taker in box:
            box.remove(self.ck_taker)

        teammate = random.choice(box)

        self.display.game_com(f"{self.attacking_team[0]} receives a corner. {self.ck_taker} is going to take it.", 
                self.display.font_small)
        self.display.game_com(f"{self.ck_taker} whips it into the box!...", 
                self.display.font_small)

        # successful corner attempt
        if success == 1:
            if event >= 1 and event <= 6:
                self.display.game_com(f"{teammate} jumps and head the ball!", 
                        self.display.font_small)
                if goal == 1:
                    self.goal(self.attacking_team, teammate)
                else:
                    self.miss()
                    self.display.game_com("It's over the bar!", 
                            self.display.font_small)
            elif event > 6 and event <= 9:
                self.display.game_com(f"{teammate} tries a bicycle kick!...", 
                        self.display.font_small)
                if goal == 1:
                    self.goal(self.attacking_team, teammate)
                else:
                    self.miss()
                    self.display.game_com("Great effort but it goes slightly over the crossbar! ", 
                            self.display.font_small)
            else:
                if goal == 1:
                    self.display.game_com(f"{self.ck_taker} goes for goal from the corner flag.", 
                            self.display.font_small)
                    self.goal(self.attacking_team, self.ck_taker)
                else:
                    self.display.game_com("The ball fly over the heads of everyone in the box.", 
                            self.display.font_small)
        else:
            self.display.game_com("The defender heads it clear. Good defending.", 
                    self.display.font_small)


    # when the two teams are struggling for possession/no chance for goal
    def idle(self):
        msg = random.choice(["Both teams are struggling for possession...", 
            f"{self.home_team[0]} and {self.away_team[0]} are battling it out together...", 
            "We wait for a chance on goal as both teams are currently at a stalemate..."])
        self.display.game_com(msg, self.display.font_small)

    def play(self):
        # 50% chance player pass 30% chance player shoots 20% he dribbles
        dist = random.randint(20, 30)
        r = random.randint(1, 10)
        self.display.game_com(f"{self.attacking_team[0]} attacks...", 
                self.display.font_small)

        if r >= 1 and r < 6:
            self.pass_ball()
        elif r >= 6 and r < 9:
            self.display.game_com(f"{self.player} goes for goal from {dist} yards out!", 
                    self.display.font_small)
            self.shoot(self.player)
        else:
            self.dribble()

# --------------------------------------------------------------------------------------------------

class Foul(Players):
    """
        Deals with fouls events

    """
    def __init__(self):
        super().__init__()
        self.display = Display()
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


        self.display.game_com(f"{self.player} is writhing on the pitch in pain!", 
                self.display.font_small)
        self.display.game_com(f"{substitute} replaces {self.player}", 
                self.display.font_small)

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

        self.display.game_com(f"Red Card! {self.defender} receives a red card for his nasty tackle on {self.player}", 
                self.display.font_small)

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
            self.display.game_com(f"{self.defender} trips {self.player} in the box!", 
                    self.display.font_small)
            # 50% chance a yellow is given
            if event <= 5:
                self.display.game_com(f"{self.defender} receives a yellow card!", 
                        self.display.font_small)
                yellow.append(self.defender)
            # 50% chance red is given
            else:
                self.red_card()
            Chances().penalty()

        # 90% chance player is fouled outside of the box
        else:
            self.display.game_com(f"{self.defender} tackles {self.player} roughly.", 
                    self.display.font_small)
            self.display.game_com(f"The referee approaches the players...", 
                    self.display.font_small)

            # 40% chance player only gets a warning
            if event < 5:
                self.display.game_com(f"The referee gives {self.defender} a warning.", 
                        self.display.font_small)
                Chances().freekick()
                
            # 50% chance player recieves a yellow card
            elif event >= 5 and event < 10:
                self.display.game_com("Yellow card!", self.display.font_small)
                yellow.append(self.player)

                # if player already recieved yellow he should recieve a yellow card
                if self.defender in yellow:
                    self.display.game_com("It's his second yellow!", self.display.font_small)
                    self.red_card()
                    Chances().freekick()
                else:
                    self.display.game_com(f"{self.defender} will have to be careful now.", self.display.font_small)
                    Chances().freekick()
            # 10% chance player recieves a red
            else:
                self.red_card()
                Chances().freekick()