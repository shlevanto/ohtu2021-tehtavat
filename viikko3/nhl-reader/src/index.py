from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    [print(player) for player in players]


if __name__ == "__main__":
    main()
