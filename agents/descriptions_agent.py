import random

class DescriptionsAgent:
    def __init__(self):
        pass

    def generate_descriptions(self, design):
        # Generate more detailed and varied descriptions
        base_keywords = ["nature", "abstract", "art", "modern", "geometric", "vibrant", "colorful", "unique", "creative", "contemporary"]
        base_tags = ["nature", "abstract", "art", "modern", "geometric", "vibrant", "colorful", "unique", "creative", "contemporary"]
        
        # Add some randomness to keywords and tags
        random.shuffle(base_keywords)
        random.shuffle(base_tags)
        
        descriptions = {
            "keywords": base_keywords[:7],
            "tags": base_tags[:7],
            "title": "Nature Abstract Art",
            "description": f"A beautiful abstract art design inspired by nature, featuring modern geometric shapes and vibrant colors. Perfect for those who appreciate contemporary art. This design is unique and {random.choice(['eye-catching', 'stunning', 'captivating'])}."
        }
        return descriptions
