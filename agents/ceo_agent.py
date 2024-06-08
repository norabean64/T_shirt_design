class CEOAgent:
    def __init__(self, ideation_agent, prompt_engineer_agent, product_manager_agent, design_image_generator_agent, descriptions_agent, legal_compliance_agent, research_agent, api_key_manager_agent, upload_agent, feedback_agent, analytics_agent, localization_agent, error_handling_agent, cache_agent, security_agent):
        self.ideation_agent = ideation_agent
        self.prompt_engineer_agent = prompt_engineer_agent
        self.product_manager_agent = product_manager_agent
        self.design_image_generator_agent = design_image_generator_agent
        self.descriptions_agent = descriptions_agent
        self.legal_compliance_agent = legal_compliance_agent
        self.research_agent = research_agent
        self.api_key_manager_agent = api_key_manager_agent
        self.upload_agent = upload_agent
        self.feedback_agent = feedback_agent
        self.analytics_agent = analytics_agent
        self.localization_agent = localization_agent

        self.error_handling_agent = error_handling_agent
        self.cache_agent = cache_agent
        self.security_agent = security_agent

    def manage_workflow(self, user_input, image_service="Stable Diffusion"):
        try:
            # Research phase
            niches = self.research_agent.research_niche(user_input)
            trends = self.research_agent.research_trends()
            platforms = self.research_agent.research_platform_promotions()
            print(f"Niches: {niches}")
            print(f"Trends: {trends}")
            print(f"Platforms: {platforms}")

            # Ideation phase
            ideas = self.ideation_agent.brainstorm_ideas(user_input)
            print(f"Ideas: {ideas}")

            # Prompt creation phase
            prompt = self.prompt_engineer_agent.create_prompt(ideas[0], service=image_service)
            print(f"Prompt: {prompt}")

            # Image generation phase
            image = self.design_image_generator_agent.generate_image(prompt)
            print(f"Generated Image: {image}")

            # Design approval phase
            if self.product_manager_agent.approve_design(image):
                print("Design approved")

                # Legal compliance check
                if self.legal_compliance_agent.check_compliance(image):
                    print("Design is legally compliant")

                    # Description generation phase
                    descriptions = self.descriptions_agent.generate_descriptions(image)
                    print(f"Descriptions: {descriptions}")

                    # Localize descriptions
                    localized_descriptions = self.localization_agent.localize(descriptions, "es")
                    print(f"Localized Descriptions: {localized_descriptions}")

                    # Upload design to POD service
                    upload_result = self.upload_agent.upload_design(image, descriptions)
                    print(f"Upload Result: {upload_result}")

                    # Collect feedback
                    self.feedback_agent.collect_feedback("design_id_123", "Good design!")
                    feedback = self.feedback_agent.analyze_feedback()
                    print(f"Feedback: {feedback}")

                    # Track performance
                    self.analytics_agent.track_performance("design_id_123", "Teespring", {"sales": 150, "likes": 200})
                    performance = self.analytics_agent.analyze_performance()
                    print(f"Performance: {performance}")
                else:
                    print("Design is not legally compliant")
            else:
                print("Design not approved")
            return {
                "image_url": image,
                "descriptions": descriptions
            }
        except Exception as e:
            error_info = self.error_handling_agent.handle_exception(e)
            print(f"Error: {error_info['message']}")
            raise e
