import spacy
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Define keywords for scoring
IMPACT_KEYWORDS = [
    "AI", "growth", "global", "market", "revenue", "education",
    "career", "personalized", "community", "network", "collaboration"
]
FEASIBILITY_KEYWORDS = [
    "easy", "simple", "quick", "feasible", "low cost", "local",
    "peer-to-peer", "technology", "automation", "accessible", "incremental"
]

def calculate_relevance(query: str, ideas: List[str]) -> List[float]:
    """
    Calculate relevance scores between the query and each idea using cosine similarity.
    """
    vectorizer = TfidfVectorizer()
    all_texts = [query] + ideas
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    query_vector = tfidf_matrix[0]
    idea_vectors = tfidf_matrix[1:]
    relevance_scores = cosine_similarity(query_vector, idea_vectors).flatten()
    return relevance_scores

def score_text_based_on_keywords(text: str, keywords: List[str]) -> int:
    """
    Score a text based on the presence of specific keywords.
    """
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]
    score = sum(1 for keyword in keywords if keyword in tokens)
    return score

def calculate_impact_and_feasibility(ideas: List[str]):
    """
    Calculate impact and feasibility scores based on predefined keywords.
    """
    impact_scores = [score_text_based_on_keywords(idea, IMPACT_KEYWORDS) for idea in ideas]
    feasibility_scores = [score_text_based_on_keywords(idea, FEASIBILITY_KEYWORDS) for idea in ideas]
    return impact_scores, feasibility_scores

def rank_ideas(query: str, ideas: List[str]):
    """
    Rank ideas based on relevance, potential impact, and feasibility.
    """
    # Calculate relevance
    relevance_scores = calculate_relevance(query, ideas)

    # Calculate impact and feasibility
    impact_scores, feasibility_scores = calculate_impact_and_feasibility(ideas)

    max_impact = max(impact_scores) if max(impact_scores) else 1
    max_feasibility = max(feasibility_scores) if max(feasibility_scores) else 1

    normalized_impact_scores = [(max_impact - score) / max_impact for score in impact_scores]
    normalized_feasibility_scores = [(max_feasibility - score) / max_feasibility for score in feasibility_scores]

    ranked_ideas = []
    for i, idea in enumerate(ideas):
        priority_score = (
            relevance_scores[i] * 0.5 +  # Weight relevance
            normalized_impact_scores[i] * 0.3 +  # Weight impact
            normalized_feasibility_scores[i] * 0.2  # Weight feasibility
        )
        ranked_ideas.append({
            "idea": idea,
            "relevance": round(relevance_scores[i], 2),
            "impact": impact_scores[i],
            "feasibility": feasibility_scores[i],
            "priority_score": round(priority_score, 2),
        })

    ranked_ideas.sort(key=lambda x: x["priority_score"])
    return ranked_ideas