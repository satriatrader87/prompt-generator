# Prompt Generator

![Python Application](https://github.com/satriatrader87/prompt-generator/workflows/Python%20Application/badge.svg)

An advanced prompt generator for consistent text-to-image generation. This tool allows you to create prompts with history support and batch processing, ensuring design consistency across variations.

## Features
- **Prompt History:** Save and reuse previously generated prompts.
- **Export to Text:** Prompts are automatically saved as `.txt` files.
- **Batch Mode:** Generate multiple prompts in one go.
- **GitHub Actions:** Automated testing and execution.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/prompt-generator.git
   cd prompt-generator
   ```
2. Run the script:
   ```bash
   python prompt_generator.py
   ```

## Usage
1. Enter character or object details when prompted.
2. The script generates a consistent prompt based on your input.
3. Prompts are saved in `generated_prompt.txt` and stored in `previous_prompt.json` for future use.

## GitHub Actions
The project includes a GitHub Actions workflow for automation. It runs the script and verifies its execution on each push to the main branch.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for details on updates and changes.
