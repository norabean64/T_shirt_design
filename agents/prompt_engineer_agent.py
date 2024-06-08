class PromptEngineerAgent:
    def __init__(self):
        pass

    def create_prompt(self, design_concept, service="Stable Diffusion"):
        # Enhanced prompt creation logic for different services
        style_adjectives = ["vibrant", "eye-catching", "unique", "modern", "artistic", "detailed"]
        additional_instructions = [
            "Ensure the design is scalable and maintains quality at different sizes.",
            "Use a color palette that complements the theme.",
            "Incorporate elements that enhance the overall aesthetic.",
            "Make sure the design is suitable for various T-shirt colors."
        ]
        
        if service == "Stable Diffusion":
            prompt = (
                f"Create a high-resolution image with a {design_concept} theme, suitable for printing on a T-shirt. "
                f"The design should be {', '.join(style_adjectives)}. "
                f"{' '.join(additional_instructions)}"
            )
        elif service == "DALLE":
            prompt = (
                f"Generate an artistic image with a {design_concept} theme, perfect for T-shirt printing. "
                f"The design should be {', '.join(style_adjectives)} and follow these guidelines: "
                f"{' '.join(additional_instructions)}"
            )
        elif service == "LeonardoAI":
            prompt = (
                f"Produce a detailed and high-quality image with a {design_concept} theme for T-shirt printing. "
                f"The design should be {', '.join(style_adjectives)}. "
                f"{' '.join(additional_instructions)}"
            )
        elif service == "MidJourney":
            prompt = (
                f"Craft a visually stunning image with a {design_concept} theme, ideal for T-shirt printing. "
                f"The design should be {', '.join(style_adjectives)}. "
                f"{' '.join(additional_instructions)}"
            )
        else:
            prompt = (
                f"Create a high-resolution image with a {design_concept} theme, suitable for printing on a T-shirt. "
                f"The design should be {', '.join(style_adjectives)}. "
                f"{' '.join(additional_instructions)}"
            )
        
        return prompt
