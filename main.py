from sleepLog import createDb, logSleep, getLastSleep
from datetime import datetime, timedelta

class Dashboard:
    def __init__(self, userName, sleepDuration, sleepDebt, suggestedBedtime):
        self.userName = userName
        self.sleepDuration = sleepDuration
        self.sleepDebt = sleepDebt
        self.suggestedBedtime = suggestedBedtime

    def display(self):
        print(f"\n Sleep Dashboard for {self.userName}")
        print(f" Last Night's Sleep: {self.sleepDuration} hours")
        print(f" Sleep Debt: {self.sleepDebt:+.1f} hours")
        print(f" Suggested Bedtime Tonight: {self.suggestedBedtime}\n")

def calculateBedtime(wakeUpTime, hoursNeeded):
    wakeHour, wakeMin = map(int, wakeUpTime.split(":"))
    wakeTime = datetime.combine(datetime.today(), datetime.min.time()) + timedelta(hours=wakeHour, minutes=wakeMin)
    bedTime = wakeTime - timedelta(hours=hoursNeeded)
    return bedTime.strftime("%H:%M")

def main():
    createDb()

    userName = input()
    idealSleep = float(input())
    wakeUpTime = input()

    print(f"\n Setup complete. Welcome, {userName}!")

    sleepDuration = float(input())
    logSleep(userName, sleepDuration)

    lastSleep = getLastSleep(userName)
    sleepDebt = lastSleep - idealSleep
    suggestedBedtime = calculateBedtime(wakeUpTime, idealSleep)

    dashboard = Dashboard(userName, sleepDuration, sleepDebt, suggestedBedtime)
    dashboard.display()

if __name__ == "__main__":
    main()
