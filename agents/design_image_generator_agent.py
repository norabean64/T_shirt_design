import requests

class DesignImageGeneratorAgent:
    def __init__(self, image_service, api_key_manager):
        self.image_service = image_service
        self.api_key_manager = api_key_manager

    def generate_image(self, prompt):
        api_key = self.api_key_manager.get_api_key(self.image_service)
        if not api_key:
            raise ValueError(f"API key for {self.image_service} is not available.")

        try:
            if self.image_service == "Stable Diffusion":
                # Simulate a call to Stable Diffusion API
                response = requests.post(
                    "https://api.stablediffusion.com/generate",
                    json={"prompt": prompt},
                    headers={"Authorization": f"Bearer {api_key}"}
                )
            elif self.image_service == "DALLE":
                # Simulate a call to DALLE API
                response = requests.post(
                    "https://api.dalle.com/generate",
                    json={"prompt": prompt},
                    headers={"Authorization": f"Bearer {api_key}"}
                )
            elif self.image_service == "LeonardoAI":
                # Simulate a call to LeonardoAI API
                response = requests.post(
                    "https://api.leonardoai.com/generate",
                    json={"prompt": prompt},
                    headers={"Authorization": f"Bearer {api_key}"}
                )
            elif self.image_service == "MidJourney":
                # Simulate a call to MidJourney API
                response = requests.post(
                    "https://api.midjourney.com/generate",
                    json={"prompt": prompt},
                    headers={"Authorization": f"Bearer {api_key}"}
                )
            else:
                raise ValueError(f"Unsupported image service: {self.image_service}")

            response.raise_for_status()
            generated_image = response.json().get("image_url", "No image URL returned")
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to generate image: {e}")

        return generated_image
