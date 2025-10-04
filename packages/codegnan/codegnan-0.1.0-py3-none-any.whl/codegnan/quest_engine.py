class QuestTracker:
    def __init__(self):
        self.badges = set()

    def award_badge(self, badge_name: str):
        print(f"🎖️ Badge earned: {badge_name}!")
        self.badges.add(badge_name)

    def get_badges(self):
        return list(self.badges)
