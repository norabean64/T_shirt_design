from flask import Flask, render_template, request
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

app = Flask(__name__)

# Initialize agents
ideation_agent = IdeationAgent()
prompt_engineer_agent = PromptEngineerAgent()
product_manager_agent = ProductManagerAgent()
api_key_manager_agent = APIKeyManagerAgent()
feedback_agent = FeedbackAgent()
analytics_agent = AnalyticsAgent()
localization_agent = LocalizationAgent()
upload_agent = UploadAgent(pod_service="Teespring", api_key=api_key_manager_agent.get_api_key("Teespring"))

design_image_generator_agent = DesignImageGeneratorAgent(
    image_service="Stable Diffusion",
    api_key_manager=api_key_manager_agent
)
descriptions_agent = DescriptionsAgent()
legal_compliance_agent = LegalComplianceAgent()
research_agent = ResearchAgent()
error_handling_agent = ErrorHandlingAgent()
cache_agent = CacheAgent()
security_agent = SecurityAgent()

# Initialize CEOAgent
ceo_agent = CEOAgent(
    ideation_agent,
    prompt_engineer_agent,
    product_manager_agent,
    design_image_generator_agent,
    descriptions_agent,
    legal_compliance_agent,
    research_agent,
    api_key_manager_agent,
    upload_agent,
    feedback_agent,
    analytics_agent,
    localization_agent,
    error_handling_agent,
    cache_agent,
    security_agent
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    image_service = request.form['image_service']
    try:
        result = ceo_agent.manage_workflow(user_input, image_service)
        return render_template('result.html', result=result)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
