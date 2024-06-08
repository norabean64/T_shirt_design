class FeedbackAgent:
    def __init__(self):
        self.feedback_data = []

    def collect_feedback(self, design_id, feedback):
        self.feedback_data.append({"design_id": design_id, "feedback": feedback})

    def analyze_feedback(self):
        # Placeholder for feedback analysis logic
        positive_feedback = [f for f in self.feedback_data if "good" in f["feedback"].lower()]
        negative_feedback = [f for f in self.feedback_data if "bad" in f["feedback"].lower()]
        return {
            "positive_feedback": positive_feedback,
            "negative_feedback": negative_feedback
        }
