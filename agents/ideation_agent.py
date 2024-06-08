import random

class IdeationAgent:
    def __init__(self):
        pass

    def brainstorm_ideas(self, user_input):
        # Simulate brainstorming with more creative techniques
        base_ideas = [
            "Abstract Art",
            "Minimalist Design",
            "Vintage Style",
            "Modern Geometric",
            "Pop Art",
            "Surrealism",
            "Futuristic",
            "Retro",
            "Nature Inspired",
            "Urban Street Art"
        ]
        
        # Add some randomness to simulate dynamic brainstorming
        random.shuffle(base_ideas)
        ideas = [f"{user_input} - {idea}" for idea in base_ideas[:5]]
        
        return ideas
