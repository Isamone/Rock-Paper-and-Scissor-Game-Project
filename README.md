✊🖐✌️ Rock, Paper, Scissors Game (Streamlit App)
This is a simple web-based implementation of the classic Rock, Paper, Scissors game built using Streamlit. The player competes against the computer in a best-of-five challenge.

🎮 Features
Clean UI with emojis and progress bar.

Name input for a personalized experience.

Game logic that follows traditional rules:

Rock beats Scissors

Scissors beats Paper

Paper beats Rock

Round-based scoreboard display.

Toast-style greeting for first-time users.

Game state preserved using st.session_state.

Option to reset the game after 5 rounds.

🚀 How to Run
Make sure you have Python and Streamlit installed:

pip install streamlit
Save the code in a Python file, for example:
rock_paper_scissors.py

Run the app with:

streamlit run rock_paper_scissors.py
🧠 How It Works
On first load, the user is greeted with a temporary success toast.

The player enters their name to start the game.

The game proceeds for 5 rounds, updating and displaying the score after each round.

After the final round, the app displays the winner and offers a Reset Game button to restart.

📁 Project Structure

rock_paper_scissors.py    # Main application script
README.md                 # Project overview (this file)
✅ Requirements
Python 3.7+

Streamlit

Version created by Ismail Damcida
