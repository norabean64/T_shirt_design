import requests

class UploadAgent:
    def __init__(self, pod_service, api_key):
        self.pod_service = pod_service
        self.api_key = api_key

    def upload_design(self, design_image, descriptions):
        try:
            if self.pod_service == "Teespring":
                response = requests.post(
                    "https://api.teespring.com/upload",
                    files={"file": design_image},
                    data={"title": descriptions["title"], "description": descriptions["description"], "tags": ",".join(descriptions["tags"])},
                    headers={"Authorization": f"Bearer {self.api_key}"}
                )
            elif self.pod_service == "Redbubble":
                response = requests.post(
                    "https://api.redbubble.com/upload",
                    files={"file": design_image},
                    data={"title": descriptions["title"], "description": descriptions["description"], "tags": ",".join(descriptions["tags"])},
                    headers={"Authorization": f"Bearer {self.api_key}"}
                )
            else:
                raise ValueError(f"Unsupported POD service: {self.pod_service}")

            response.raise_for_status()
            upload_result = response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to upload design: {e}")

        return upload_result
