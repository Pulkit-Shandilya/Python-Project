class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

    def add_time(self, other_time):
        total_hours = self.hours + other_time.hours
        total_minutes = self.minutes + other_time.minutes
        total_seconds = self.seconds + other_time.seconds
        return Time(total_hours, total_minutes, total_seconds)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


# Example usage
time1 = Time(2, 45, 50)
time2 = Time(1, 20, 30)
result = time1.add_time(time2)
print("Resultant Time:", result)