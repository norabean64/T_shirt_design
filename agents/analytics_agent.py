class AnalyticsAgent:
    def __init__(self):
        self.analytics_data = []

    def track_performance(self, design_id, platform, metrics):
        self.analytics_data.append({"design_id": design_id, "platform": platform, "metrics": metrics})

    def analyze_performance(self):
        # Placeholder for performance analysis logic
        high_performance = [a for a in self.analytics_data if a["metrics"]["sales"] > 100]
        low_performance = [a for a in self.analytics_data if a["metrics"]["sales"] <= 100]
        return {
            "high_performance": high_performance,
            "low_performance": low_performance
        }
