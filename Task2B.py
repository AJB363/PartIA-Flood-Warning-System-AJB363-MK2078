# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Station names with the current relative level of 0.8
    for s in stations_level_over_threshold(stations, 0.9):
        print("{} {}".format(s[0].name, s[1]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
