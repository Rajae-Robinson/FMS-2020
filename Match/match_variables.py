class MatchVariables:
    home_goals = 0
    away_goals = 0
    mins = 1
    home_scorers = []
    away_scorers = []

    # takes team who scored and player who scored
    def increase_score(self, team, player):
        from Menus.select_team import SelectTeam
        # stores the player who scored and at what time
        scorer = (player, MatchVariables.mins)
        # if player is on home team
        if team[0] in SelectTeam.home_team:
            if player in SelectTeam.home_team:
                MatchVariables.home_goals += 1
                MatchVariables.home_scorers.append(scorer)

        # if player is on away team
        if team[0] in SelectTeam.away_team:
            if player in SelectTeam.away_team:
                MatchVariables.away_goals += 1
                MatchVariables.away_scorers.append(scorer)

    def update_mins(self):
        MatchVariables.mins += 4