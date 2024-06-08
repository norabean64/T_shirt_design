class APIKeyManagerAgent:
    def __init__(self):
        self.api_keys = {
            "Stable Diffusion": "your_stable_diffusion_api_key",
            "DALLE": "your_dalle_api_key",
            "LeonardoAI": "your_leonardoai_api_key",
            "MidJourney": "your_midjourney_api_key"
        }

    def get_api_key(self, service):
        return self.api_keys.get(service, None)

    def set_api_key(self, service, api_key):
        self.api_keys[service] = api_key

    def rotate_api_key(self, service):
        # Placeholder for API key rotation logic
        # In a real scenario, this would involve generating a new key and updating the service
        new_api_key = f"new_{service.lower()}_api_key"
        self.api_keys[service] = new_api_key
        return new_api_key
