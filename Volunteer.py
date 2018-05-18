#!/usr/local/bin/python3
class Volunteer:
    move_count  = 0
    drive_count = 0

    def __init__(self, cwid, name, email, phone_num, driver,year):
        self.cwid = cwid
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.driver = driver
        self.year = year

    def drove():
        self.drive_count += 1

    def drove(count):
        self.drive_count += count

    def moved():
        self.move_count += 1

    def moved(count):
        self.move_count += count

    def get_cwid(self):
        return self.cwid

    def get_volunteer(self):
        return(self.cwid, self.name, self.email, self.phone_num, self.driver,self.year)

    def display_count():
        print ("Total FRN Volunteers: %d" % Volunteer.total_count())
