from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import math
import Game

colors = ["#0282c7", "#b602c7", "#500000"]

def plotTimeline(dates, drinks, id, width=0.2):
    global taxes

    taxes = plots.add_subplot(1, 2, 1)
    x = np.arange(len(dates))
    offset = (width*(1-(id%2)*2)*math.floor((1+id)/2))
    taxes.bar(x+offset, drinks, width, color=colors[id])
    taxes.set_xticklabels([""]+dates, rotation=65)
    taxes.set_xlim(-1, 5)
    taxes.add_callback(scrollx)
    taxes.set_ylabel("drinks")

def plotPie(drinks, players):
    global paxes
    paxes = plots.add_subplot(1, 2, 2)
    labels = []
    for player, drink in zip(players, drinks):
        labels.append(player + "\n" + str(round(drink,2)) + " drinks")
    paxes.pie(drinks, colors=colors, labels=labels, autopct="%1.2f%%")

    # plt.subplot(1, 2, 2)
    # plt.pie(drinks, colors=colors, labels=players)

def createFigures(players, date1, date2):
    global plots
    global startdate
    global enddate

    startdate = date1
    enddate = date2

    plots = plt.figure(figsize=[16,9],dpi=80)
    plots.canvas.mpl_connect("scroll_event", scrollx)
    # plots = plt.subplots(figsize=(16, 9), dpi=80)
    Game.createTimeline(players, date1, date2)
    Game.createPie(players, date1, date2)
    plots.show()

def scrollx(event):
    dates = [""] + Game.getDateRange(enddate, startdate) + [""]
    for i in range(len(dates)):
        if (dates[i] == datetime.today().strftime("%#m/%#d/%y")):
            dates[i] = "Today"

    xmin, xmax = taxes.get_xlim()
    if(event.step > 0):
        if (xmin > -1):
            # print(int(xmin)-1,"   ",int(xmax)-1)
            # print(dates[int(xmin)-1:int(xmax)-1])
            taxes.set_xticklabels(dates[int(xmin):int(xmax)], rotation=65)
            taxes.set_xlim(xmin-1, xmax-1)
    elif(event.step < 0):
        if (xmax < len(dates)-2):
            taxes.set_xticklabels(dates[int(xmin)+2:int(xmax)+2], rotation=65)
            taxes.set_xlim(xmin+1, xmax+1)
    plots.canvas.draw()
