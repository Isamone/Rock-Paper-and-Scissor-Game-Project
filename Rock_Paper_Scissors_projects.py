import streamlit as st
import random
import time

st.title("✊ Rock, 🖐 Paper, ✌️ Scissors Game")

# Show welcome toast once
if "toast_shown" not in st.session_state:
    st.session_state.toast_shown = False
if not st.session_state.toast_shown:
    placeholder = st.empty()
    placeholder.success("Let's see how well you shoot in the dark... 😎")
    time.sleep(2)
    placeholder.empty()
    st.session_state.toast_shown = True

# Store game settings
options = ["Rock", "Paper", "Scissors"]

# Store player name in session state
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

# If name not set, show editable input
if st.session_state.player_name == "":
    player_name_input = st.text_input("Enter your name")
    if player_name_input:
        st.session_state.player_name = player_name_input.strip()
        

else:
    st.text_input("Enter your name", value=st.session_state.player_name, disabled=True)

# Assign variable
player_name = st.session_state.player_name

# Initialize game state variables
for key, default in {
    "player_score": 0,
    "cpu_score": 0,
    "rounds_played": 0,
    "game_over": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Only show the game UI if name is set
if player_name:
    st.write(f"Welcome {player_name}! Best of 5 rounds wins the game.")

    # Show scoreboard
    st.markdown("### 🧮 Scoreboard")
    st.markdown(f"**🧍 {player_name}: {st.session_state.player_score}**")
    st.markdown(f"**🤖 CPU: {st.session_state.cpu_score}**")
    st.markdown(f"**🔁 Rounds Played: {st.session_state.rounds_played + 1}/5**")

    if not st.session_state.game_over:
        player_choice = st.selectbox(f"{player_name}, choose your move:", options)

        if st.button("Play"):
            cpu_choice = random.choice(options)

            st.write(f"🧍 {player_name} played: **{player_choice}**")
            st.write(f"🤖 CPU played: **{cpu_choice}**")

            st.progress((st.session_state.rounds_played + 1) / 5)

            # Determine round winner
            if player_choice == cpu_choice:
                st.info("It's a tie this round!")
            elif (
                (player_choice == "Rock" and cpu_choice == "Scissors") or
                (player_choice == "Scissors" and cpu_choice == "Paper") or
                (player_choice == "Paper" and cpu_choice == "Rock")
            ):
                st.session_state.player_score += 1
                st.success(f"{player_name} wins this round! 🎉")
            else:
                st.session_state.cpu_score += 1
                st.error("CPU wins this round! 😢")

            # Increment round count
            st.session_state.rounds_played += 1

            # End of game
            if st.session_state.rounds_played == 5:
                st.session_state.game_over = True
                st.subheader("🏁 Game Over!")
                st.write(f"Final Score - {player_name}: {st.session_state.player_score}, CPU: {st.session_state.cpu_score}")

                if st.session_state.player_score > st.session_state.cpu_score:
                    st.success(f"🎉 {player_name} wins the game!")
                elif st.session_state.player_score < st.session_state.cpu_score:
                    st.error("😢 CPU wins the game!")
                else:
                    st.info("🤝 It's a draw!")

                # Reset button
                if st.button("🔁 Reset Game"):
                    st.toast("Let's see how well you shoot in the dark... 😎")
                    st.session_state.player_score = 0
                    st.session_state.cpu_score = 0
                    st.session_state.rounds_played = 0
                    st.session_state.game_over = False
                    st.session_state.player_name = ""
                    
            else:
                st.subheader("📢 Next Round")

