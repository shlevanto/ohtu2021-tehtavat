class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        players_f = [p for p in players if p.nationality == nationality]
        players_f.sort(key=lambda x: x.goals + x.assists, reverse=True)

        return players_f
