from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    '''
    matcher = (query
        .plays_in("NYR").has_at_least(1, "goals")
        .has_fewer_than(5, "goals")
        .build()
    )
    '''
    
    matcher = (
    query
        .oneOf(
        query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
        query.playsIn("EDM")
            .hasAtLeast(40, "points")
            .build()
        )
        .build()
)

    [print(player) for player in stats.matches(matcher)]


if __name__ == "__main__":
    main()
