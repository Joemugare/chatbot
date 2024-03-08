import streamlit as st
import pandas as pd
from fuzzywuzzy import process

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("fishfry.csv")
    return df

df = load_data()

# Function to get bot response
def get_bot_response(user_input, df):
    # Use fuzzy matching to find similar venue names
    venue_names = df['venue_name'].tolist()
    closest_match, _ = process.extractOne(user_input, venue_names)
    
    # Retrieve venue details based on the closest match
    venue_details = df.loc[df['venue_name'] == closest_match].iloc[0]
    return venue_details

# Main function for the chat app
def main():
    st.title("Venue Details Chatbot")
    st.markdown("Welcome to the Venue Details Chatbot! Ask me about venue details.")

    # Get user input
    user_input = st.text_input("You:", "")

    # Check if user has inputted something
    if user_input:
        bot_response = get_bot_response(user_input, df)
        
        # Format the bot response
        formatted_response = f"**Venue Name:** {bot_response['venue_name']}\n" \
                             f"**Venue Type:** {bot_response['venue_type']}\n" \
                             f"**Venue Address:** {bot_response['venue_address']}\n" \
                             f"**Website:** {bot_response['website']}\n" \
                             f"**Menu URL:** {bot_response['menu_url']}\n" \
                             f"**Menu Text:** {bot_response['menu_text']}\n" \
                             f"**Phone:** {bot_response['phone']}\n" \
                             f"**Email:** {bot_response['email']}\n" \
                             f"**Alcohol:** {bot_response['alcohol']}\n" \
                             f"**Lunch:** {bot_response['lunch']}\n"
        
        st.text_area("Bot:", formatted_response)

if __name__ == "__main__":
    main()
