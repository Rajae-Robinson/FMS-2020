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