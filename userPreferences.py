class UserPreferences:
    def __init__(self):
        self.idealSleepHours = 8.0
        self.defaultWakeTime = "07:00"
        self.userName = ""

    def updatePreferences(self, idealSleepHours=None, defaultWakeTime=None, userName=None):
        if idealSleepHours is not None:
            self.idealSleepHours = idealSleepHours
        if defaultWakeTime is not None:
            self.defaultWakeTime = defaultWakeTime
        if userName is not None:
            self.userName = userName

    def getPreferences(self):
        return {
            "idealSleepHours": self.idealSleepHours,
            "defaultWakeTime": self.defaultWakeTime,
            "userName": self.userName
        }
