import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.header("🏟️ Match Details", divider='gray')
    bat_team = st.text_input("Batting Team", key="bat_team_input")
    bowl_team = st.text_input("Bowling Team", key="bowl_team_input")
    innings = st.radio("Innings", ["1", "2"], horizontal=True, key="innings_radio")
    bat_players = st.text_area(f"Enter {bat_team}'s Players (comma-separated)", key="bat_players_area")
    bowl_players = st.text_area(f"Enter {bowl_team}'s Players (comma-separated)", key="bowl_players_area")
    start = st.checkbox("Start App 🚀", key="start_checkbox")

st.header(":cricket_bat_and_ball: BallTrack Analyzer: Every Ball, Every Insight :bar_chart:", divider='gray')

# Initialize session state for ball data
if 'ball_data' not in st.session_state:
    st.session_state.ball_data = pd.DataFrame(columns=[
        "Over", "Ball", "Batting Team", "Bowling Team", "Innings", "Batter",
        "Batting Hand", "Bowler", "Bowling Style", "Bowling Side", "Runs",
        "Outcome", "False Shot", "Pitching Line", "Pitching Length",
        "Arrival Line", "Shot Type", "Shot Connection", "Shot Intent",
        "Wagon Zone", "Feet Movement", "Extras", "Extra Runs", "Wicket",
        "Player Dismissed", "Dismissed Type", "Description"
    ])

if start:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ball Details")
        over_no = st.number_input("Over No.", min_value=1, step=1, key="over_no_input")
        ball_no = st.number_input("Ball No.", min_value=1, max_value=6, step=1, key="ball_no_input")
        batter = st.selectbox("Batter", [name.strip() for name in bat_players.split(",") if name.strip()], key="batter_selectbox")
        bowler = st.selectbox("Bowler", [name.strip() for name in bowl_players.split(",") if name.strip()], key="bowler_selectbox")
        bat_hand = st.radio("Batting Hand", ["RHB", "LHB"], horizontal=True, key="bat_hand_radio")
        bowling_style = st.selectbox("Bowling Style", [
            "Right-arm Fast", "Right-arm Medium", "Left-arm Fast", "Left-arm Medium",
            "Right-arm Legspin", "Right-arm Offspin", "Left-arm Chinaman", "Left-arm Orthodox"
        ], key="bowling_style_selectbox")
        bowl_side = st.radio("Bowling Side", ["Around", "Over"], horizontal=True, key="bowl_side_radio")
        runs = st.number_input("Runs Off Bat", min_value=0, step=1, key="runs_input")
        extras = st.selectbox("Extras", ["None", "Wide", "Legbyes", "Byes", "No ball", "Penalty"], key="extras_selectbox")
        extra_runs = st.number_input("Extra Runs", min_value=0, step=1, key="extra_runs_input")
        outcome = st.selectbox("Outcome", ["Dot", "Single", "Double", "Triple", "Four", "Six", "Extras"], key="outcome_selectbox")
        false_shot = st.radio("False Shot", ["No", "Yes"], horizontal=True, key="false_shot_radio")
        wicket = st.radio("Wicket", ["No", "Yes"], horizontal=True, key="wicket_radio")
        player_dismissed = st.selectbox("Player Dismissed", ["None"] + [name.strip() for name in bat_players.split(",") if name.strip()], key="player_dismissed_selectbox")
        dismissal_type = st.selectbox("Dismissed Type", [
            "None", "Bowled", "Caught", "LBW", "Run Out", "Stumped",
            "Hit Wicket", "Retire Out", "Timed Out", "Handled Ball", "Obstructed Field"
        ], key="dismissal_type_selectbox")
        description = st.text_area("Description", key="description_area")

    with col2:
        st.subheader("Zone Details")
        pitching_line = st.selectbox("Pitching Line", ["Wide Off Stump", "Outside Off Stump", "On Stumps", "Down Leg", "Wide Leg"], key="pitching_line_selectbox")
        pitching_length = st.selectbox("Pitching Length", ["Full Toss", "Yorker", "Full", "Good", "Back of Length", "Short"], key="pitching_length_selectbox")
        arrival_line = st.selectbox("Arrival Line", ["Wide Off Stump", "Outside Off Stump", "On Stumps", "Down Leg", "Wide Leg"], key="arrival_line_selectbox")
        shot_type = st.selectbox("Shot Type", [
            "None", "FF def", "BF def", "Steer", "Cover Drive", "Straight Drive",
            "Pull Shot", "Square Cut", "Flick", "Push", "Worked", "Leg Glance",
            "On Drive", "Off Drive", "Square Drive", "Late Cut", "Upper Cut",
            "Hook Shot", "Sweep Shot", "Reverse Sweep", "Switch Hit", "Paddle Sweep",
            "Paddle Scoop", "Slog Sweep", "Slog", "Inside Out", "Glance"
        ], key="shot_type_selectbox")
        shot_connection = st.selectbox("Shot Connection", [
            "None", "Middle", "Mistime", "Leading Edge", "Inside Edge",
            "Outside Edge", "Top Edge", "Bottom Edge", "Beaten", "Glove"
        ], key="shot_connection_selectbox")
        shot_intent = st.selectbox("Shot Intent", ["None", "Attack", "Defense", "Rotate", "Leave"], key="shot_intent_selectbox")
        wagon_zone = st.selectbox("Wagon Zone", [
            "None", "Fine Leg", "Square Leg", "Mid Wicket", "Long On",
            "Long Off", "Covers", "Point", "Third Man"
        ], key="wagon_zone_selectbox")
        feet_movement = st.selectbox("Feet Movement", [
            "None", "Front Foot", "Back Foot", "Charged Down", "Walked Across", "Created Room"
        ], key="feet_movement_selectbox")

    if st.button("Add Ball Data 📝", key="add_ball_data_button"):
        new_entry = {
            "Over": over_no,
            "Ball": ball_no,
            "Batting Team": bat_team,
            "Bowling Team": bowl_team,
            "Innings": innings,
            "Batter": batter,
            "Batting Hand": bat_hand,
            "Bowler": bowler,
            "Bowling Style": bowling_style,
            "Bowling Side": bowl_side,
            "Runs": runs,
            "Outcome": outcome,
            "False Shot": false_shot,
            "Pitching Line": pitching_line,
            "Pitching Length": pitching_length,
            "Arrival Line": arrival_line,
            "Shot Type": shot_type,
            "Shot Connection": shot_connection,
            "Shot Intent": shot_intent,
            "Wagon Zone": wagon_zone,
            "Feet Movement": feet_movement,
            "Extras": extras,
            "Extra Runs": extra_runs,
            "Wicket": wicket,
            "Player Dismissed": player_dismissed,
            "Dismissed Type": dismissal_type,
            "Description": description
        }
        st.session_state.ball_data = st.session_state.ball_data.append(new_entry, ignore_index=True)
        st.success("Ball data added successfully!")

    st.divider()
    st.subheader("Collected Ball Data")
    st.dataframe(st.session_state.ball_data)

    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv_data = convert_df_to_csv(st.session_state.ball_data)

    st.download_button(
        label="Download Data ⬇️",
        data=csv_data,
        file_name='match_data.csv',
        mime='text/csv'
    )
