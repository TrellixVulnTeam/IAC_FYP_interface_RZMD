# IAC_FYP_interface
This repo contains the "I'm a Celebrity" chatbot interface. This web app is made using the Flask python framework.
## Installation Requirements
After cloning the project be sure to install the packages needed from requirements.txt using pip.
```
python -m pip install -r requirements.txt
```
## Running the interface
This project was made and run with python 3.8.0 so there could be some dependency errors with the packages depending on the version used. Generally anything above python 3.6.0 should work.

To run the interface run this in the command line:
```
python flask_app.py
```
This should start the flask server and provide a local host address: http://127.0.0.1:5000/ where the interface should be running.
## Interacting with the Bot
Click 'Start Bot' to initialise the bot.
Click 'Get Personality' for the bot to randomly select a celebrity persona.
From here you can chat with the bot. 
If you want to guess who the celebrity is click 'Guess Who'.
If you need a hint click 'Need a hint?'.
If you want to talk to a different celebrity just click 'Get Personality' again.
## Open-Sourced Code
Some code used in developing this bot was sourced from the Hugging Face Project [Transfer-Learning-Conversational-AI](https://github.com/huggingface/transfer-learning-conv-ai)
