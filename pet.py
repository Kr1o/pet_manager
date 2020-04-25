from datetime import date


class Pet:
    def __init__(self, name,
                 birth_date,
                 feed_weight=0,
                 feed_in_day=0,
                 vaccination=False,
                 tick_protect=False):
        self.name = name
        self.birth_date = birth_date
        self.feed_weight = feed_weight
        self.feed_in_day = feed_in_day
        self.vaccination = vaccination
        self.tick_protect = tick_protect

    def buy_feed(self, weight):
        self.feed_weight += weight

    def calculate_feed(self):
        calculate_feed = self.feed_weight // self.feed_in_day
        return calculate_feed

    def age(self):
        today = date.today()
        birth_date = self.birth_date.split('.')
        birth_date = date(int(birth_date[2]), int(birth_date[1]), int(birth_date[0]))
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
