import requests

# Step 1: Generate ideas
response = requests.post("http://127.0.0.1:5000/generate_ideas/", json={"query": "What new app should I build?"})
ideas = response.json()["ideas"]

print("Generated Ideas:")
for i, idea in enumerate(ideas, start=1):
    print(f"{i}. {idea}")

# Step 2: Let the user select two options
selected_indices = input("Choose two ideas by typing their numbers (e.g., 1,3): ")
selected_indices = [int(idx.strip()) - 1 for idx in selected_indices.split(",")]

# Validate user input
if len(selected_indices) != 2 or any(idx < 0 or idx >= len(ideas) for idx in selected_indices):
    print("Invalid selection. Please choose exactly two valid numbers.")
else:
    # Step 3: Send selected ideas to expand_ideas endpoint
    selected_ideas = [ideas[idx] for idx in selected_indices]
    expand_response = requests.post("http://127.0.0.1:5000/expand_ideas/", json={"selected_ideas": selected_ideas})
    expanded_ideas = expand_response.json()["detailed_suggestions"]

    print("\nDetailed Suggestions:")
    # breakpoint()
    for idea, suggestion in expanded_ideas.items():
        idea = idea.replace("**", "")
        suggestion = suggestion.replace("**", "")
        print(f"- {idea}: {suggestion}")
