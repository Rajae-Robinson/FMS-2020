class MatchVariables:
    home_goals = 0
    away_goals = 0
    mins = 1

    # takes team who scored and player who scored
    def increase_score(self, team, player):
        from Menus.select_team import SelectTeam
        # if player is on home team
        if team[0] in SelectTeam.home_team:
            if player in SelectTeam.home_team:
                MatchVariables.home_goals += 1

        # if player is on away team
        if team[0] in SelectTeam.away_team:
            if player in SelectTeam.away_team:
                MatchVariables.away_goals += 1

    def update_mins(self):
        MatchVariables.mins += 1