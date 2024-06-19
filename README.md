# Pokedex
Pokedex CLI is a simple command-line application that allows users to search for Pokémon by name or ID using the PokeAPI. The application retrieves and displays information about the Pokémon, including its sprite, height, weight, types, and type damage relations. The sprite is displayed in the terminal using ANSI color codes. Additionally, users can continue searching for more Pokémon within the same session.

## Features

- Search for a Pokémon by name or ID.
- Display the Pokémon's sprite in the terminal using ANSI colour codes.
- Show detailed information about the Pokémon, including height, weight, and types.
- Display type damage relations for the Pokémon's types.

## Requirements

- Python 3.6 or higher
- Requests library
- Pillow library
- Pydub library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/pokedex-cli.git
    ```
2. Navigate to the project directory:
    ```bash
    cd pokedex-cli
    ```
3. Install the required libraries:
    ```bash
    pip install requests pillow pydub
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```
2. Enter the name or ID of the Pokémon you would like to search for.
3. View the Pokémon's information and sprite in the terminal.
4. Optionally, search for another Pokémon by following the prompts.


