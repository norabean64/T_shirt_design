import tkinter as tk
from tkinter import ttk, messagebox
from agents.ceo_agent import CEOAgent
from agents.ideation_agent import IdeationAgent
from agents.prompt_engineer_agent import PromptEngineerAgent
from agents.product_manager_agent import ProductManagerAgent
from agents.design_image_generator_agent import DesignImageGeneratorAgent
from agents.descriptions_agent import DescriptionsAgent
from agents.legal_compliance_agent import LegalComplianceAgent
from agents.research_agent import ResearchAgent
from agents.api_key_manager_agent import APIKeyManagerAgent
from agents.upload_agent import UploadAgent
from agents.feedback_agent import FeedbackAgent
from agents.analytics_agent import AnalyticsAgent
from agents.localization_agent import LocalizationAgent
from agents.error_handling_agent import ErrorHandlingAgent
from agents.cache_agent import CacheAgent
from agents.security_agent import SecurityAgent
from agents.error_handling_agent import ErrorHandlingAgent
from agents.cache_agent import CacheAgent

class TShirtDesignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("T-Shirt Design Application")

        # Initialize agents
        self.ideation_agent = IdeationAgent()
        self.prompt_engineer_agent = PromptEngineerAgent()
        self.product_manager_agent = ProductManagerAgent()
        self.api_key_manager_agent = APIKeyManagerAgent()
        self.feedback_agent = FeedbackAgent()
        self.analytics_agent = AnalyticsAgent()
        self.localization_agent = LocalizationAgent()
        self.upload_agent = UploadAgent(pod_service="Teespring", api_key=self.api_key_manager_agent.get_api_key("Teespring"))

        self.design_image_generator_agent = DesignImageGeneratorAgent(
            image_service="Stable Diffusion",
            api_key_manager=self.api_key_manager_agent
        )
        self.descriptions_agent = DescriptionsAgent()
        self.legal_compliance_agent = LegalComplianceAgent()
        self.research_agent = ResearchAgent()
        self.error_handling_agent = ErrorHandlingAgent()
        self.cache_agent = CacheAgent()
        self.error_handling_agent = ErrorHandlingAgent()
        self.cache_agent = CacheAgent()
        self.security_agent = SecurityAgent()

        # Initialize CEOAgent
        self.ceo_agent = CEOAgent(
            self.ideation_agent,
            self.prompt_engineer_agent,
            self.product_manager_agent,
            self.design_image_generator_agent,
            self.descriptions_agent,
            self.legal_compliance_agent,
            self.research_agent,
            self.api_key_manager_agent,
            self.upload_agent,
            self.feedback_agent,
            self.analytics_agent,
            self.localization_agent,
            self.error_handling_agent,
            self.cache_agent,
            self.error_handling_agent,
            self.cache_agent,
            self.security_agent
        )

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Enter your design concept:")
        self.label.grid(column=0, row=0, padx=10, pady=10)

        self.user_input = ttk.Entry(self.root, width=50)
        self.user_input.grid(column=1, row=0, padx=10, pady=10)

        self.style_label = ttk.Label(self.root, text="Select Design Style:")
        self.style_label.grid(column=0, row=1, padx=10, pady=10)

        self.design_style = ttk.Combobox(self.root, values=[
            "Abstract Art", "Minimalist Design", "Vintage Style", "Modern Geometric",
            "Pop Art", "Surrealism", "Futuristic", "Retro", "Nature Inspired", "Urban Street Art"
        ])
        self.design_style.grid(column=1, row=1, padx=10, pady=10)

        self.image_service_label = ttk.Label(self.root, text="Select Image Generation Service:")
        self.image_service_label.grid(column=0, row=2, padx=10, pady=10)

        self.image_service = ttk.Combobox(self.root, values=[
            "Stable Diffusion", "DALLE", "LeonardoAI", "MidJourney"
        ])
        self.image_service.grid(column=1, row=2, padx=10, pady=10)

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
        self.submit_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def submit(self):
        user_input = self.user_input.get()
        design_style = self.design_style.get()
        if not user_input or not design_style:
            messagebox.showerror("Input Error", "Please enter a design concept and select a design style.")
            return

        try:
            image_service = self.image_service.get()
            result = self.ceo_agent.manage_workflow(user_input, image_service)
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_result(self, result):
        self.result_label.config(text=f"Generated Image URL: {result['image_url']}\n"
                                      f"Title: {result['descriptions']['title']}\n"
                                      f"Description: {result['descriptions']['description']}\n"
                                      f"Tags: {result['descriptions']['tags']}")
if __name__ == "__main__":
    root = tk.Tk()
    app = TShirtDesignApp(root)
    root.mainloop()
