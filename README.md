# Minecraft Agent Framework

This repository, **tapminecraft**, contains a Python framework for developing and running agents in **Minecraft Java Edition (version 1.12)**. The agents can interact with the Minecraft world by moving, building, destroying blocks, and sending/receiving chat messages. The framework leverages functional and reflective programming to create dynamic and customizable behaviors for bots.

## Features

- **Agent Framework**:
  - Move agents programmatically within the world.
  - Build and destroy blocks dynamically.
  - Send messages to the Minecraft chat.

- **Customizable Bots**:
  - Easily define behaviors using functional or reflective programming.
  - Example bots include:
    - **InsultBot**: Sends playful insults in the chat.
    - **TNTBot**: Places and explodes TNT blocks.

- **Integration with `mcpi` Library**:
  - Utilizes the `mcpi` library from the `AdventuresInMinecraft` repository for seamless interaction with Minecraft Java Edition.

## Prerequisites

1. **Minecraft Java Edition (1.12)**:
   - Install Minecraft Java Edition version 1.12 on your computer.
   - Ensure the game is running and the server connection is properly configured.

2. **AdventuresInMinecraft Repository**:
   - Clone or download the repository containing the `mcpi` folder.
   - Ensure the `mcpi` folder is in the same directory as the Python scripts or in your Python path.

3. **Python 3**:
   - Ensure Python 3 is installed.
   - Check your Python version:
     ```bash
     python3 --version
     ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tapminecraft.git
   cd tapminecraft
   ```

2. Ensure the `mcpi` folder is available in the project directory.

3. Install any additional dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running a Bot

1. **Start Minecraft Java Edition (1.12)**:
   - Open Minecraft Java Edition version 1.12 on your computer.
   - Create a new world in Creative Mode or connect to a server.

2. **Run a Bot Script**:
   - Execute a bot script from this repository. For example, to run `InsultBot`:
     ```bash
     python3 InsultBot.py
     ```

3. **Interact In-Game**:
   - Open the Minecraft chat to see messages from the bot.
   - Observe the bot's actions (e.g., block placement, movement).
