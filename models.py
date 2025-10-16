# Not strictly necessary for SQLite + raw SQL, but included for standardization and future extensibility
class Campaign:
    def __init__(self, id, name, status, clicks, cost, impressions):
        self.id = id
        self.name = name
        self.status = status
        self.clicks = clicks
        self.cost = cost
        self.impressions = impressions
