class ConvertedDays:

    def __init__(self, **data):
        self.years = int(data.__getitem__("years"))
        self.weeks = int(data.__getitem__("weeks"))
        self.days = int(data.__getitem__("days"))

def convert(days: int) -> ConvertedDays:
    years = days // 365
    rest = days % 365
    weeks = rest // 7
    rest = rest % 7
    return ConvertedDays(years=years, weeks=weeks, days=rest)


converted = convert(365)
print(f"Jahre: {converted.years}")
print(f"Wochen: {converted.weeks}")
print(f"Tage: {converted.days}")
