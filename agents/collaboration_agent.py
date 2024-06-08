class CollaborationAgent:
    def __init__(self):
        self.collaborations = {}

    def start_collaboration(self, project_id, user_ids):
        self.collaborations[project_id] = {
            "user_ids": user_ids,
            "contributions": {user_id: [] for user_id in user_ids}
        }

    def add_contribution(self, project_id, user_id, contribution):
        if project_id in self.collaborations and user_id in self.collaborations[project_id]["user_ids"]:
            self.collaborations[project_id]["contributions"][user_id].append(contribution)

    def get_collaboration(self, project_id):
        return self.collaborations.get(project_id, None)

    def end_collaboration(self, project_id):
        if project_id in self.collaborations:
            del self.collaborations[project_id]

    def get_user_contributions(self, project_id, user_id):
        if project_id in self.collaborations and user_id in self.collaborations[project_id]["user_ids"]:
            return self.collaborations[project_id]["contributions"].get(user_id, [])
        return None
