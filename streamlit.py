import streamlit as st

# Define the chatbot function
def chatbot():
    st.title("Simple Chatbot")

    user_input = st.text_input("You:", "")
    
    if user_input:
        response = get_bot_response(user_input)
        st.text_area("Bot:", response, height=100)

# Define the function to generate bot responses
def get_bot_response(user_input):
    # You can replace this with your own logic to generate responses
    return "Bot: Thanks for saying: " + user_input

# Run the chatbot function
if __name__ == '__main__':
    chatbot()

