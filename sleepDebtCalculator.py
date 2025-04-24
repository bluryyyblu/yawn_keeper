from datetime import timedelta

class SleepDebtCalculator:
    def __init__(self, actualSleepDuration, idealSleepHours):
        self.actualSleepDuration = actualSleepDuration
        self.idealSleepDuration = timedelta(hours=idealSleepHours)
        self.sleep_debt = self.idealSleepDuration - self.actualSleepDuration

    
    def calculateSleepDebt(self):
        recommendedDuration = timedelta(hours=self.recommendedSleepHours)
        debt = recommendedDuration - self.actualSleepDuration
        
        if debt.total_seconds() < 0:
            return timedelta(0)
        return debt
    
    def formatSleepDebt(self):
        debt = self.calculateSleepDebt()
        totalMinutes = int(debt.total_seconds() // 60)
        hours = totalMinutes // 60
        minutes = totalMinutes % 60
        return f"{hours}h {minutes}m"
