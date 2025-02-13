import json
import os

PROMPT_HISTORY_FILE = "previous_prompt.json"

def save_prompt_to_file(prompt, filename="generated_prompt.txt"):
    """ Save the generated prompt to a text file. """
    with open(filename, "w") as file:
        file.write(prompt)

def load_previous_prompt():
    """ Load the previous prompt from the JSON file. """
    if os.path.exists(PROMPT_HISTORY_FILE):
        with open(PROMPT_HISTORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_prompt_history(prompt_data):
    """ Save the current prompt data to the JSON file. """
    with open(PROMPT_HISTORY_FILE, "w") as file:
        json.dump(prompt_data, file, indent=4)

def generate_prompt(name, core_description, outfit_description, situation, background):
    """ Generate a consistent prompt for a character or object. """
    prompt = f"{name} is {core_description}. Keep the design consistent across all variations. {name} always wears {outfit_description}. The current scene shows {situation}, with a background of {background}. Maintain the same color scheme and artistic style for consistency."
    return prompt

if __name__ == "__main__":
    print("Welcome to the Advanced Prompt Generator!")

    # Load previous prompt if available
    previous_prompt = load_previous_prompt()
    if previous_prompt:
        print("Previous prompt found. Do you want to reuse it? (y/n)")
        reuse = input().strip().lower()
        if reuse == 'y':
            print("
Reusing previous prompt...")
            print("Generated Prompt:
")
            print(previous_prompt["generated_prompt"])
            exit()

    # Get user input for the new prompt
    name = input("Enter the name of your character or object: ")
    core_description = input("Enter the core description (e.g., physical traits, personality, key features): ")
    outfit_description = input("Enter the outfit or design description (e.g., clothing, accessories, or key elements): ")
    situation = input("Enter the current situation or activity (e.g., fighting, relaxing, powered-up): ")
    background = input("Enter the background description (e.g., futuristic city, ancient temple): ")

    # Generate and display the new prompt
    generated_prompt = generate_prompt(name, core_description, outfit_description, situation, background)
    print("
Generated Prompt:
")
    print(generated_prompt)

    # Save the prompt to a text file and update the history
    save_prompt_to_file(generated_prompt)
    save_prompt_history({"generated_prompt": generated_prompt})

    print("
The prompt has been saved to 'generated_prompt.txt'.")
