# Chatbot for Idea Suggestions

## Overview
This project is a chatbot that helps users brainstorm ideas based on their input, prioritize these ideas based on relevance, impact, and feasibility, and provide detailed suggestions for the selected ideas.

## Features
1. **Generate Ideas**: Using AI to generate three unique ideas based on a user-provided query.
2. **Rank Ideas**: Automatically rank the ideas based on relevance, potential impact, and feasibility.
3. **User Selection**: Allow users to select one or two ideas from the ranked list for further details.
4. **Detailed Suggestions**: Provide expanded details for the selected ideas.

## Technology Stack
- **Backend**: Flask
- **AI Integration**: Google Generative AI (Gemini API)
- **Text Processing**: SpaCy (used for scoring relevance, impact, and feasibility)
- **Environment Management**: Python `.env` for secure API key storage

## Setup and Installation

### Prerequisites
1. Python 3.10 or higher installed.
2. Google Generative AI (Gemini) API key.
3. Virtual environment setup (recommended).

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd chatbot_for_idea_suggestion
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the project root.
   - Add your Google Generative AI (Gemini) API key:
     ```env
     GEMINI_API_KEY=your_gemini_api_key
     ```

5. Run the Flask server:
   ```bash
   python app.py
   ```

### API Endpoints

#### 1. **Generate Ideas**
- **Endpoint**: `/generate_ideas/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "query": "What new app should I build?"
  }
  ```
- **Response**:
  ```json
  {
    "ideas": [
      "1. AI-powered recipe app: Suggests recipes based on fridge contents and dietary restrictions.",
      "2. Hyperlocal skill-sharing platform: Connects neighbors to learn and teach skills (e.g., baking, coding).",
      "3. Personalized micro-learning app: Delivers bite-sized lessons tailored to user's specific career goals."
    ]
  }
  ```

#### 2. **Expand Ideas**
- **Endpoint**: `/expand_ideas/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "selected_ideas": ["1", "3"]
  }
  ```
- **Response**:
  ```json
  {
    "detailed_suggestions": [
      "For the AI-powered recipe app: Incorporate AI algorithms to suggest recipes based on fridge inventory, dietary restrictions, and meal preferences. Add features like shopping list generation and nutritional analysis.",
      "For the personalized micro-learning app: Develop modules focused on career-specific skills, gamify the learning process with badges and rewards, and integrate AI to adapt lessons to the user's progress."
    ]
  }
  ```

### Ranking Logic
The ideas are ranked based on:
- **Relevance**: Calculated using cosine similarity between the user query and generated ideas.
- **Impact**: Estimated using keywords such as `AI`, `growth`, `global`, `education`, etc.
- **Feasibility**: Estimated using keywords such as `easy`, `local`, `automation`, etc.

Each idea is assigned a priority score, and the ideas are displayed in ascending order of their scores.


