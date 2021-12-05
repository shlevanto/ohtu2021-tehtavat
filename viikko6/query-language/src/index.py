from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, HasAtLeast, HasFewerThan, PlaysIn, Not, All
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )
    
    #for player in stats.matches(matcher):
    #    print(player)
        
    query = QueryBuilder()
    matcher = query.plays_in("NYR").build()
    
    for player in stats.matches(matcher):
        print(player)
    
if __name__ == "__main__":
    main()
