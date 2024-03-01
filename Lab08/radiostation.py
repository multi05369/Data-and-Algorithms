'''function'''
import json
def findstation(station, city):
    '''find the station that covered most'''
    res = []
    while station:
        best_station = max(station, key=lambda x: len(station[x].intersection(city)))
        res.append(best_station)

        cover = station[best_station]
        station = {k: v - cover for k, v in station.items()}

        station = {k: v for k, v in station.items() if v}
    return sorted(res)

def radio_station():
    '''solution'''
    all_city = json.loads(input())
    station = {}
    for _ in range(int(input())):
        data = json.loads(input())
        station[data["Name"]] = set(data["Cities"])
    print(findstation(station, all_city))

radio_station()
