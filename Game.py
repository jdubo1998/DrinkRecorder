from datetime import datetime
from datetime import timedelta
import json
import Graphs

with open("scores.json", "r") as file:
    data = json.load(file)

# True if date1 is before date2, false otherwise.
def compareDates(date1, date2):
    if (date1.count("+") > 0 or date2.count("+") > 0):
        return False

    if (date1=="" or date2==""):
        return True

    d1 = datetime.strptime(date1, "%m/%d/%y")
    d2 = datetime.strptime(date2, "%m/%d/%y")
    return d2 > d1

def getEndDate():
    date = ""
    for player in data["Players"]:
        for score in player["Scores"]:
            if (compareDates(date, score["date"])):
                date = score["date"]
    return date

def getEndDateISO():
    return datetime.strptime(getEndDate(), "%m/%d/%y")

def printPlayer(name=""):
    for player in data["Players"]:
        if (name=="" or player["name"]==name):
            print(player["name"], ":")
            for score in player["Scores"]:
                print(score["date"], ": ", score["pct"], " @ ", score["oz"])
            print("total: ", player["total"], "\n")

def insertScore(name, date, pct, oz):
    # Creates a new dictionary object for the score.
    new_score = {"date": date, "pct": pct, "oz": oz}
    for player in data["Players"]:
        if (player["name"] == name):
            index = -1
            for score in player["Scores"]:
                if (compareDates(date, score["date"])):
                    index = player["Scores"].index(score)
                elif (date == score["date"]):
                    new_score["date"] = "+" + date
            if (index == -1):
                player["Scores"].append(new_score)
            else:
                player["Scores"].insert(index, new_score)
            print(player["Scores"])
    with open("scores.json", "w") as ofile:
        json.dump(data, ofile, indent=4)

def findUniqueDates(scores, date1="", date2=""):
    uniqueDates = []
    for score in scores:
        # Makes sure that the date falls in the correct range, marked by date1 and date2
        if (inDateRange(score["date"], date1, date2)):
            uniqueDates.append(score["date"])
    return uniqueDates

def calculateAvg(scores, date1="", date2=""):
    print("Under Construction")
    totals = calculateTotals(date1, date2, name)

    for score in scores:
        date = score["date"].replace("+", "")
        # if ((compareDates(date1, date) or date1 == date) and (compareDates(date, date2) or date2 == date)):
    # for player in data["Players"]:
        # uniqueDates = 0
    #     for score in player["Scores"]:
    #         dCount = (score["pct"]*score["oz"])/60
    #         player["total"] = player["total"] + dCount
    #
    #         if (score["date"].count("+") == 0):
    #             uniqueDates = uniqueDates + 1
    #     player["Avgs"]["session"] = player["total"]/

def calculateDrinks(scores, date1="", date2=""):
    if (not compareDates(date1, date2)):
        date1, date2 = date2, date1
    dCount = 0

    for score in scores:
        date = score["date"].replace("+", "")
        # Makes sure that the date falls in the correct range, marked by date1 and date2
        if (inDateRange(date, date1, date2)):
            dCount = dCount + (score["pct"]*score["oz"])/60
    return dCount

def inDateRange(date, date1, date2):
    return (compareDates(date1, date) or date1 == date) and (compareDates(date, date2) or date2 == date)

def getDateRange(date2, date1="4/20/20"):
    dates = []
    startdate = datetime.strptime(date1, "%m/%d/%y")
    enddate = datetime.strptime(date2, "%m/%d/%y")

    for i in range((enddate-startdate).days+1):
        date = (startdate + timedelta(days=i)).strftime("%#m/%#d/%y")
        dates.append(date)

    return dates

# TODO: use getDateRange instead
def createTimeline(players, date1, date2):
    drinks = []
    dates = []
    startdate = datetime.strptime(date1, "%m/%d/%y")
    enddate = datetime.strptime(date2, "%m/%d/%y")

    for player in data["Players"]:
        # Checks if the current player is an active player.
        if (player["name"] in players):
            for i in range((enddate-startdate).days+1):
                date = (startdate + timedelta(days=i)).strftime("%#m/%#d/%y")
                dates.append(date)
                drinks.append(calculateDrinks(player["Scores"], dates[i], dates[i]))
            Graphs.plotTimeline(dates, drinks, player["id"])
            dates.clear()
            drinks.clear()

def createPie(players, date1, date2):
    drinks = []
    for player in data["Players"]:
        if (player["name"] in players):
            drinks.append(calculateDrinks(player["Scores"], date1, date2))
    Graphs.plotPie(drinks, players)

def getPlayers():
    players = []
    for player in data["Players"]:
        players.append(player["name"])
    return players

# print(calculateDrinks(data["Players"][2]["Scores"], "5/1/20", "5/1/20"))

# enddate = getEndDateISO()
# startdate = datetime.strptime("4/20/20", "%m/%d/%y")

# def __init__():

# def __main__():
#     startdate = datetime.strptime("4/20/20", "%m/%d/%y")
#     enddate = startdate
#
#     pCount = 0
#     pCount = len(data["Players"])
#     enddate = getEndDateISO()
#
#     for player in data["Players"]:
#         createDailyGraph(player["Scores"], player["id"])
#
#     Graphs.showWeek()
