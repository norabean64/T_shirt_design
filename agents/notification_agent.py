class NotificationAgent:
    def __init__(self):
        self.notifications = []

    def send_notification(self, user_id, message):
        self.notifications.append({"user_id": user_id, "message": message})

    def get_notifications(self, user_id):
        return [n for n in self.notifications if n["user_id"] == user_id]
