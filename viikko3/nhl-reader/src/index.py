from player_reader import PlayerReader


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    players = PlayerReader(url)    
    #players.sort(key=lambda x: x.goals + x.assists, reverse=True)

    print("Oliot:")

    for player in players:
        if player.nationality == "FIN":
            print(player)


if __name__ == "__main__":
    main()
