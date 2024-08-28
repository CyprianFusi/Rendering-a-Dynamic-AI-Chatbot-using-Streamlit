import streamlit as st
from conversation_manager import ConversationManager
from conversation_manager import DEFAULT_MAX_TOKENS, DEFAULT_TOKEN_BUDGET, DEFAULT_TEMPERATURE


st.title("Binati Chatbot")
if 'chat_manager' not in st.session_state:
    st.session_state['chat_manager'] = ConversationManager()
    
chat_manager = st.session_state['chat_manager']

st.sidebar.title('Bot Parameters')
with st.sidebar:
    token_budget = st.slider(f"Set token budget on a scale of 25 to {DEFAULT_TOKEN_BUDGET}", 25, DEFAULT_TOKEN_BUDGET, DEFAULT_MAX_TOKENS)
with st.sidebar:
    chat_temperature = st.slider("Set teperature on a scale of 0 to 1", 0.0, 1.0, DEFAULT_TEMPERATURE)
with st.sidebar:
    persona = st.selectbox("Select Chatbot Persona", list(chat_manager.system_messages.keys()))  
if persona in ["Sassy Assistant", "Angry Assistant", "Thoughtful Assistant"]:
    chat_manager.set_persona(persona)
else:
    custom_persona = st.text_area("Describe your Custom Persona here")
    if custom_persona:
        st.button("Set Custom Persona", on_click = chat_manager.set_custom_system_message, args = (custom_persona,))
    
user_input = st.chat_input("Chat with me...") 

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = chat_manager.conversation_history
if user_input:
    ai_response = chat_manager.chat_completion(prompt = user_input,
                                               temperature = chat_temperature,
                                               max_tokens = token_budget
                                              )

for chat in chat_manager.conversation_history:
    if chat["role"] != "system":
        with st.chat_message(chat["role"]):
            st.write(chat["content"])

st.button("Clear Chat History", on_click = chat_manager.reset_conversation_history)