class UserProfileAgent:
    def __init__(self):
        self.user_profiles = {}

    def create_profile(self, user_id, preferences):
        self.user_profiles[user_id] = {
            "preferences": preferences,
            "history": []
        }

    def update_preferences(self, user_id, preferences):
        if user_id in self.user_profiles:
            self.user_profiles[user_id]["preferences"] = preferences

    def add_to_history(self, user_id, design_id):
        if user_id in self.user_profiles:
            self.user_profiles[user_id]["history"].append(design_id)

    def get_profile(self, user_id):
        return self.user_profiles.get(user_id, None)
