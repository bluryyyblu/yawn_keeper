class Dashboard:
    def __init__(self, userName, sleepDuration, sleepDebt, suggestedBedtime):
        self.userName = userName
        self.sleepDuration = sleepDuration
        self.sleepDebt = sleepDebt
        self.suggestedBedtime = suggestedBedtime
    
    def display(self):
        print("\n" + "=" * 40)
        print(f"SLEEP DASHBOARD: {self.userName}")
        print("=" * 40)
        print(f"Hours Slept:    {self.sleepDuration:.1f}h")
        print(f"Sleep Debt:     {self.sleepDebt.total_seconds() / 3600:.1f}h")
        print(f"Suggested Bedtime: {self.suggestedBedtime}")
        print("=" * 40)