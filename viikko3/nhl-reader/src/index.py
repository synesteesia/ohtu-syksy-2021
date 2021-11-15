from playerreader import PlayerReader
from playerstats import Playerstats
from player import Player



def main():
    print("haloo")
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = Playerstats(reader)
    players = stats.top_scorers_by_nationality('FIN')

    for player in players:
        print(player)


main()