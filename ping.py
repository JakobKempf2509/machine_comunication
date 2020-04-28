#!/usr/bin/env python

#this code is used to realize a repeat ping
#J.Kempf 2020-04-28

import os 

abbruch = True
my_counter = 0
my_ip = "192.168.178.180" #ip adress from the KD4-Simulation

while abbruch:
    try:
        my_ping = os.system("ping " + my_ip) #one time ping

        if (my_ping == 0):
            print("\nThe desired ip is reachable\n")
            abbruch = False

        elif (my_ping != 0):
            my_counter = my_counter + 1

            if (my_counter < 3):
                print("\nThe ping was failed, the program will try it again")
                abbruch = True
            else:
                print("\nThe desired ip is not reachable, please start the program again\n")
                abbruch = False

    except ValueError:
        print("\nThere was an error during runtime\nthe program was restarted\n")
