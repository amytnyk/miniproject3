#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
"""
Module for visualization of filler game
"""
import argparse
import subprocess
import os
import csv
import operator
from os import listdir
from os.path import isfile, join
from multiprocessing import Pool


def get_name(player: str) -> str:
    return os.path.basename(player).split('.')[-2]


def play(player1: str, player2: str, board: str):
    process = subprocess.Popen(f"./filler_vm -f {board} -p1 {player1} -p2 {player2} > dump.txt", shell=True, stdout=subprocess.PIPE)
    process.wait()
    process = subprocess.Popen(f"python visualizer/visualizer.py -file dump.txt -image results/{get_name(player1)}_vs_{get_name(player2)}.gif", shell=True, stdout=subprocess.PIPE)
    process.wait()


def get_winner() -> str:
    with open("filler.trace", 'r', encoding="utf-8") as file:
        return file.read().split('\n')[1].split()[0]


def play_all(players: str, board: str):
    players = [join(players, f) for f in listdir(players) if isfile(join(players, f))]
    names = list(map(get_name, players))

    with open('results.csv', 'w', encoding='UTF8') as csv_file:
        wins = {}

        for name in names:
            wins[name] = 0

        writer = csv.writer(csv_file)
        writer.writerow([' '] + names)
        for idx1 in range(len(players)):
            row = [ names[idx1] ]
            for idx2 in range(len(players)):
                if idx1 == idx2:
                    row.append(' ')
                    continue
                try:
                    print(f"Playing {names[idx1]} vs {names[idx2]}")
                    play(players[idx1], players[idx2], board)
                except:
                    pass
                winner = get_name(get_winner())
                row.append(winner)
                wins[winner] += 1
            writer.writerow(row)
        writer.writerow([])
        writer.writerow(['Total wins'])
        for winner, wins in sorted(wins.items(), key=operator.itemgetter(1)):
            writer.writerow([ winner, str(wins) ])


def main():
    """
    Filler 42 leaberboard
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-map", help="map")
    parser.add_argument("-players", help="path to players folder")
    args = parser.parse_args()
    play_all(args.players, args.map)


if __name__ == "__main__":
    main()
