import random

class ResearchAgent:
    def __init__(self):
        pass

    def research_niche(self, user_input):
        # Simulate niche research
        niches = [
            "Eco-friendly fashion",
            "Streetwear",
            "Athleisure",
            "Vintage",
            "Graphic Tees",
            "Minimalist",
            "Bohemian",
            "Techwear",
            "Anime/Manga",
            "Music Bands"
        ]
        random.shuffle(niches)
        return niches[:3]

    def research_trends(self):
        # Simulate trend research
        trends = [
            "Sustainable materials",
            "Bold colors",
            "Retro designs",
            "Customizable clothing",
            "Tech-integrated fashion",
            "Gender-neutral fashion",
            "Art-inspired designs",
            "Statement pieces",
            "Handmade aesthetics",
            "Digital prints"
        ]
        random.shuffle(trends)
        return trends[:3]

    def research_platform_promotions(self):
        # Simulate platform promotion research
        platforms = [
            "Instagram",
            "Pinterest",
            "Etsy",
            "Redbubble",
            "Amazon",
            "eBay",
            "Facebook",
            "TikTok",
            "Shopify",
            "Teespring"
        ]
        random.shuffle(platforms)
        return platforms[:3]
