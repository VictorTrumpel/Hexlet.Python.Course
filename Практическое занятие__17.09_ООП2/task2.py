class Time:
    def __init__(self, hours, minutes, seconds):
        if not (0 <= hours <= 23):
            raise ValueError("Часы должны быть в диапазоне 0-23")
        if not (0 <= minutes <= 59):
            raise ValueError("Минуты должны быть в диапазоне 0-59")
        if not (0 <= seconds <= 59):
            raise ValueError("Секунды должны быть в диапазоне 0-59")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __del__(self):
        print(f"Объект Time({self}) удалён")

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def part_of_day(self):
        if 0 <= self.hours < 6:
            return "ночь"
        elif 6 <= self.hours < 12:
            return "утро"
        elif 12 <= self.hours < 18:
            return "день"
        else:
            return "вечер"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        total_seconds %= 24 * 3600 
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def __add__(self, other):
        total = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total)

    def __sub__(self, other):
        total = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total)

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

t1 = Time(10, 30, 15)
t2 = Time(5, 45, 50)
t3 = Time(2, 15, 30)
t4 = Time(18, 0, 0)

T1 = t1 + t3
T2 = t4 - t2

print("t1:", t1, t1.part_of_day())
print("t2:", t2, t2.part_of_day())
print("t3:", t3, t3.part_of_day())
print("t4:", t4, t4.part_of_day())
print("T1 = t1 + t3:", T1, T1.part_of_day())
print("T2 = t4 - t2:", T2, T2.part_of_day())
print("T1 < T2?", T1 < T2)
print("T1 > T2?", T1 > T2)
