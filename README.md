# PyGame_GenAI

First - Experimental Version!
Produces a final_pygame.py file - missing few final code composing steps and cleanups still

Welcome to the PyGame_GenAI project! This repository provides a framework to automatically generate code for Pygame projects using the dspygen library with Groq AI. The goal is to streamline the creation of Pygame environments and games by leveraging AI-driven code generation.

## Installation

To get started, you'll need to install the required dependencies and set up your environment:

1. **Install Ollama locally:**
   Ensure that you have Ollama installed locally to support AI code generation.

2. **Obtain AI Keys:**
   Get your API keys for OpenAI or Groq AI.

3. **Install dspygen:**
   ```bash
   pip install dspygen
   ```

## Usage

Once you have installed the dependencies, you can run the provided script to generate a Pygame project. The script guides you through various steps, each focusing on a specific part of the game development process.

### Steps

1. **Set up the Pygame environment.**
2. **Create the game window and main loop.**
3. **Implement the game grid.**
4. **Create Tetris shapes and movement.**
5. **Add collision detection.**
6. **Implement the scoring system.**
7. **Add game over conditions.**
8. **Refine UI/UX and optimize the code.**

### Running the Script

To run the script, execute the following command:

```bash
python src/dspygen/rm/dspy_dev_steps.py
```

The script will prompt you to provide task descriptions and any required RFCs (Request for Change) for error handling and refining the code generation process.

### Example Classes

Below are the key classes defined in the script, which represent different stages of the game development process:

- **SetupPygameEnv:** Sets up the Pygame environment.
- **CreateGameWindow:** Creates the game window and main loop.
- **ImplementGameGrid:** Implements the game grid.
- **CreateTetrisShapes:** Creates Tetris shapes and movement.
- **AddCollisionDetection:** Adds collision detection.
- **ImplementScoringSystem:** Implements the scoring system.
- **AddGameOverConditions:** Adds game over conditions.
- **Refine:** Refines UI/UX and makes the code pretty and tested.

Each class uses input and output fields to define the task and the generated code snippet.

### Code Snippet Execution

The script extracts and executes code snippets generated by the AI model. If an error occurs during execution, it prompts you to provide suggestions or use the default error message to refine the process.

### Building the Final Game

Once all steps are successfully processed, the script compiles the generated code snippets into a final game script, `final_game.py`.

### Main Function

The `main` function initializes the environment, defines the steps, and processes each step to generate the final game code.

## New Feature and Plannings

Add a pyGame Wizard guiding through the workflow
Add the DSPyGEn code_master_retriever and Code - RAG - Open up to select what DBs also store code / hot code composables to remote offer (SaaS) maybe by hot wallets for micro payments TBD / composable smart contracts. 
Add terms and conditions for each code_snippet - Ricardian Contracts - Hoare Logics?
Tokenize code_snippets of value and allow value chains / virtual supply chains / PoC for enterprise code value co-creation ...

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please contact me via my github user chat here.

---

Enjoy building your Pygame projects with PyGame_GenAI!