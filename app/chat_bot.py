import os
from fastapi import HTTPException
import google.generativeai as genai
from typing import List

# Load the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Configure GenAI
genai.configure(api_key=api_key)

def generate_idea_suggestions(user_query: str):
    """
    Generate 3 unique ideas from the user's query using Google's GenAI.
    
    Args:
        user_query (str): The user's input or query.

    Returns:
        List[str]: A list of 3 generated ideas.
    """
    prompt = f"""
    Based on the query: "{user_query}", generate 3 unique ideas. Keep them concise.
    """
    try:
        # Use GenAI to generate ideas
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        ideas = [line.strip() for line in response.text.split("\n") if line.strip()]
        if len(ideas) < 3:
            raise HTTPException(
                status_code=400,
                detail="Insufficient ideas generated. Please refine the query."
            )
        return ideas[:3]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating ideas: {str(e)}")

def expand_idea_details(selected_ideas: List[str]):
    """
    Expand on the selected ideas by providing detailed suggestions for each.
    
    Args:
        selected_ideas (List[str]): List of selected ideas.

    Returns:
        dict: A dictionary containing detailed suggestions for each idea.
    """
    try:
        detailed_suggestions = {}
        for idea in selected_ideas:
            prompt = f"""
            Provide a detailed suggestion for the idea: "{idea}". Focus on unique features, target audience, and a marketing strategy.
            """
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            detailed_suggestions[idea] = response.text.strip()
        return detailed_suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error expanding ideas: {str(e)}")


