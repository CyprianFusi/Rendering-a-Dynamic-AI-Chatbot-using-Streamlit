# Rendering-a-Dynamic-AI-Chatbot-using-Streamlit
## OpenAI Large Language Model (LLM) powered Chatbot using Streamlit

This project involves creating an AI chatbot that can take on different personas, keep track of conversation history, and provide coherent responses.
The Chatbot is then rendered using [Streamlit](https://streamlit.io/).

Key skills we'll practice include:

* Using the **OpenAI API** to interact with a large language model.
* Crafting and managing distinct chatbot **personas with system messages**.
* Monitoring and handling **token usage to stay within a token budget**.
* Maintaining a **conversation history to achieve contextually aware interactions**.

### Creating the Chatbot Framework
The Chatbot Framework is implementated as a **ConversationManager** class in the module `conversation_manager.py` while the rendering using [Streamlit](https://streamlit.io/) is implemented in `chatbot_using_streamlit.py`

To test the bot from your local machine run `python -m streamlit run .\chatbot_using_streamlit.py` from the command line.
