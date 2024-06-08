class LocalizationAgent:
    def __init__(self):
        self.translations = {
            "en": {"title": "Nature Abstract Art", "description": "A beautiful abstract art design inspired by nature."},
            "es": {"title": "Arte Abstracto de la Naturaleza", "description": "Un hermoso diseño de arte abstracto inspirado en la naturaleza."},
            "fr": {"title": "Art Abstrait de la Nature", "description": "Un beau design d'art abstrait inspiré par la nature."}
        }

    def localize(self, descriptions, language):
        if language in self.translations:
            localized_descriptions = self.translations[language]
            descriptions["title"] = localized_descriptions["title"]
            descriptions["description"] = localized_descriptions["description"]
        return descriptions
