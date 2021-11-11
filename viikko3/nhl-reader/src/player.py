import requests


class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

        print("JSON-muotoinen vastaus:")
        print(self.response)

        self.players = []

        for player_dict in self.response:
            player = Player(
                player_dict
            )

        self.players.append(player)

        return self.players


class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.penalties = player_dict['penalties']
        self.team = player_dict['team']
        self.games = player_dict['games']

    def __str__(self):
        return (f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(self.goals + self.assists):4}")
