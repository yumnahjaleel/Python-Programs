import json
import os

class Question:
    def __init__(self, text, trait, weight=1):
        self.text = text
        self.trait = trait  # e.g., 'Extraversion', 'Logic', 'Creativity'
        self.weight = weight

class PersonalityTest:
    def __init__(self, user_name):
        self.user_name = user_name
        self.results = {
            "Social": 0,
            "Analytical": 0,
            "Creative": 0,
            "Resilience": 0
        }
        self.questions = [
            Question("Do you feel energized after spending time with large groups?", "Social"),
            Question("Do you prefer solving problems using data rather than intuition?", "Analytical"),
            Question("Do you often find yourself daydreaming about new possibilities?", "Creative"),
            Question("Do you stay calm and focused under high-pressure situations?", "Resilience"),
            Question("Are you the first to start a conversation with a stranger?", "Social", weight=2),
            Question("Do you enjoy breaking down complex systems to see how they work?", "Analytical", weight=2)
        ]

    def run_test(self):
        print(f"\n--- Welcome, {self.user_name}! Please answer (1-5) ---")
        print("1: Strongly Disagree | 5: Strongly Agree\n")
        
        for q in self.questions:
            while True:
                try:
                    score = int(input(f"{q.text}: "))
                    if 1 <= score <= 5:
                        # Logic: Normalize score (3 is neutral) and apply weight
                        normalized_score = (score - 3) * q.weight
                        self.results[q.trait] += normalized_score
                        break
                    print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def calculate_archetype(self):
        # Determine the dominant trait
        dominant = max(self.results, key=self.results.get)
        
        archetypes = {
            "Social": "The Connector (Thrives on human interaction)",
            "Analytical": "The Architect (Driven by logic and structure)",
            "Creative": "The Visionary (Sees patterns others miss)",
            "Resilience": "The Anchor (Steady in the middle of a storm)"
        }
        return archetypes.get(dominant, "The Enigma")

    def save_results(self):
        data = {
            "user": self.user_name,
            "scores": self.results,
            "archetype": self.calculate_archetype()
        }
        filename = f"{self.user_name}_results.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\nResults saved to {filename}")

# --- Main Execution ---
if __name__ == "__main__":
    name = input("Enter your name: ")
    test = PersonalityTest(name)
    test.run_test()
    
    print("\n--- Final Profile ---")
    print(f"Dominant Trait: {test.calculate_archetype()}")
    for trait, score in test.results.items():
        print(f"{trait}: {score}")
    
    test.save_results()
