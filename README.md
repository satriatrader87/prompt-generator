# Prompt Generator for Consistent Text-to-Image Prompts

This project provides a Python script to generate consistent text-to-image prompts for characters or objects with customizable descriptions. It supports saving and loading previous prompts to maintain consistency across multiple sessions.

## Features
- Generate prompts with specific details about a character or object.
- Automatically save the input for future use.
- Load and modify previous prompts easily.
- **GitHub Actions**: Automatically runs the script when you push changes to the repository.

## Installation
1. Clone this repository or download the files.
2. Ensure you have Python installed (version 3.6 or newer).

## Usage
Run the script in your terminal:
```
python prompt_generator.py
```
Follow the instructions to input your character's details and generate a prompt. The input data will be saved and can be reused in the next session.

## GitHub Actions
This repository includes a GitHub Actions workflow that automatically runs the `prompt_generator.py` script whenever changes are pushed to the `main` branch. You can find the workflow file in `.github/workflows/python-app.yml`.

## Example Prompt
```
Aria is a tall elf with silver hair and blue eyes. Keep the design consistent across all variations. Aria always wears a green robe with golden patterns. The current scene shows Aria casting a spell, with a background of a magical forest. Maintain the same color scheme and artistic style for consistency.
```

## License
This project is licensed under the MIT License.
