from janito.llm.model import LLMModelInfo

MODEL_SPECS = {
    "glm-4.5": LLMModelInfo(
        name="glm-4.5",
        context=128000,
        max_input=128000,
        max_cot=4096,
        max_response=4096,
        thinking_supported=True,
        other={
            "description": "Z.AI's GLM-4.5 model for advanced reasoning and conversation",
            "supports_tools": True,
            "supports_images": True,
            "supports_audio": False,
            "supports_video": False,
            "input_cost_per_1k": 0.0005,
            "output_cost_per_1k": 0.0015,
        },
    ),
    "glm-4.5-air": LLMModelInfo(
        name="glm-4.5-air",
        context=128000,
        max_input=128000,
        max_cot=4096,
        max_response=4096,
        thinking_supported=True,
        other={
            "description": "Z.AI's GLM-4.5-Air model - compact and efficient version",
            "supports_tools": True,
            "supports_images": True,
            "supports_audio": False,
            "supports_video": False,
            "input_cost_per_1k": 0.0003,
            "output_cost_per_1k": 0.0009,
        },
    ),
}
