#!/usr/local/bin/python3
from Volunteer import Volunteer
import _pickle as pickle
import csv
import os

class Roster:
    roster = []
    count = 0

    def __init__(self,name):
        self.name = name

    def add_members(self, filename):
        row = 0
        with open(filename) as frn_data:
            data_reader = csv.reader(frn_data)
            iter_data = iter(data_reader)
            next(iter_data)
            for row in iter_data:
                Roster.roster.append(Volunteer(row[1],row[2],row[3],row[4],row[5],row[6]))
                Roster.count += 1

    def remove_member(cwid):
        Roster.roster = [volunteer for volunteer in Roster.roster if volunteer.cwid == cwid]

    def total_count():
        return Roster.count

    def get_roster(self):
        return Roster.roster

    def update_member_runs(self, filename):
        row = 0
        with open(filename) as frn_data:
            data_reader = csv.reader(frn_data)
            iter_data = iter(data_reader)
            next(iter_data)
            for row in iter_data:
                Roster.roster.append(Volunteer(row[1],row[2],row[3],row[4],row[5],row[6]))
                Roster.count += 1
