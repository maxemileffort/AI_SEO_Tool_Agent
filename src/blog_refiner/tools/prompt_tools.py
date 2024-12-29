from crewai_tools import tool

@tool
def generate_image_prompt(content_snippet: str) -> str:
    """
    Generates a detailed prompt for DALL-E 3 based on provided content.
    """
    prompt = f"Create an artistic illustration based on this content: {content_snippet}. Use vibrant and realistic elements to match a casual and humorous tone."
    return prompt
