from datetime import datetime, timedelta

class SleepSuggestor:
    def __init__(self, sleepDebtHours, wakeUpTimeStr):
        self.sleepDebtHours = sleepDebtHours
        self.wakeUpTimeStr = wakeUpTimeStr
        self.wakeUpTime = self.parseTime(wakeUpTimeStr)
    
    def parseTime(self, timeStr):
        try:
            return datetime.strptime(timeStr, "%H:%M")
        except ValueError:
            return datetime.strptime("07:00", "%H:%M") 
    
    def suggestBedTime(self):
        totalSleepNeeded = 8 + self.sleepDebtHours
        sleepDuration = timedelta(hours=totalSleepNeeded)
        suggestedBedTime = self.wakeUpTime - sleepDuration
        
        if suggestedBedTime.day != self.wakeUpTime.day:
            suggestedBedTime = suggestedBedTime.replace(day=self.wakeUpTime.day)
        
        return suggestedBedTime.strftime("%H:%M")
