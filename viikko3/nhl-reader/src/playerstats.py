def sort_by_points(player):
    return player.points

class Playerstats:
    def __init__(self, reader):
     self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top_scorers(self):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        return sorted_players

    def nationality(self, nationality):
        players_by_country = filter(
            lambda player: player.nationality == nationality,
            self._players
        )
        return list(players_by_country)

    def top_scorers_by_nationality(self, nationality):
        top_score_list = self.top_scorers()

        players_by_country = filter(
            lambda player: player.nationality == nationality,
            top_score_list
        )
        return list(players_by_country)