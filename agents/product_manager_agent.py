import logging

class ProductManagerAgent:
    def __init__(self):
        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def approve_design(self, design):
        # Simulate a more complex approval process
        approval_criteria = {
            "error": "Design contains errors.",
            "low quality": "Design is of low quality.",
            "inappropriate content": "Design contains inappropriate content.",
            "blurry": "Design is blurry.",
            "pixelated": "Design is pixelated.",
            "low resolution": "Design resolution is too low.",
            "poor color scheme": "Design has a poor color scheme."
        }

        for criterion, message in approval_criteria.items():
            if criterion in design.lower():
                self.logger.info(f"Design rejected: {message}")
                return False

        # Additional checks can be added here
        if len(design) < 10:
            self.logger.info("Design rejected: Design description is too short.")
            return False

        # Simulate resolution check
        if "low resolution" in design.lower():
            self.logger.info("Design rejected: Design resolution is too low.")
            return False

        # Simulate color scheme check
        if "poor color scheme" in design.lower():
            self.logger.info("Design rejected: Design has a poor color scheme.")
            return False

        self.logger.info("Design approved.")
        return True

    def provide_feedback(self, design):
        # Provide feedback on why a design was rejected
        feedback = []
        approval_criteria = {
            "error": "Design contains errors.",
            "low quality": "Design is of low quality.",
            "inappropriate content": "Design contains inappropriate content.",
            "blurry": "Design is blurry.",
            "pixelated": "Design is pixelated.",
            "low resolution": "Design resolution is too low.",
            "poor color scheme": "Design has a poor color scheme."
        }

        for criterion, message in approval_criteria.items():
            if criterion in design.lower():
                feedback.append(message)

        if len(design) < 10:
            feedback.append("Design description is too short.")

        return feedback
