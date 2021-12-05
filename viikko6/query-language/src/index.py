from statistics import Statistics
from player_reader import PlayerReader
from matchers import And,Or, HasAtLeast, PlaysIn, Not
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = Or(
       HasAtLeast(30, "goals"),
       HasAtLeast(50, "assists")
    )


    query = QueryBuilder()
    # matcher = query.build()
    # matcher = query.playsIn("NYR").build()
    # matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()
    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .playsIn("EDM")
        .hasAtLeast(40, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
