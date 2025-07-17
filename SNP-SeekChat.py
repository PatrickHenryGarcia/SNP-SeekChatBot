# Bioinformatics Chat Assistant (Web Version as per supervisor)
# Description: A Streamlit-based chatbot connected to a custom OpenAI Assistant
# that answers questions using uploaded documents (e.g., FAQs, guides).

import streamlit as st
import openai
import time
import re

# Set API credentials(to protect the API key, it is withheld) 
openai.api_key = "API_KEY"
ASSISTANT_ID = "asst_yYId6HPPTZb2O7ZE9gUP1wK8"

# Web UI setup (I used the emoji that would denote Rice |Genomics
st.set_page_config(page_title="Bioinformatics Assistant", page_icon="🌾🧬")
st.title("🌾 SNPSeek Chat Assistant 🧬")
st.write("Ask questions related to SNP-Seek FAQs, user guides, or research papers.")

# Start a new conversation thread if not already started
if "thread_id" not in st.session_state:
    thread = openai.beta.threads.create()
    st.session_state.thread_id = thread.id
    st.session_state.history = []

# Input box for user
user_input = st.text_input("Type your question below:", key="input")

if user_input:
    # Add user message to session history and send to OpenAI
    st.session_state.history.append(("user", user_input))
    openai.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=user_input
    )

    # Start assistant run and wait for reply
    with st.spinner("Processing..."):
        run = openai.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=ASSISTANT_ID
        )

        while True:
            status = openai.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread_id,
                run_id=run.id
            )
            if status.status == "completed":
                break
            time.sleep(0.7)

        # Get assistant response
        messages = openai.beta.threads.messages.list(thread_id=st.session_state.thread_id)
        msg = messages.data[0]
        reply_text = msg.content[0].text.value

        # Clean out in-text citation markers like  
        reply_text = re.sub(r"【\d+:\d+†source】", "", reply_text)

        # Extract file citation names
        source_info = []
        if hasattr(msg.content[0].text, "annotations"):
            for annotation in msg.content[0].text.annotations:
                if annotation.type == "file_citation":
                    file_id = annotation.file_citation.file_id
                    file_obj = openai.files.retrieve(file_id)
                    source_info.append(file_obj.filename)

        # Add filenames to the end of the assistant's reply
        if source_info:
            reply_text += "\n\n📁 **Source:** " + ", ".join(source_info)

        # Store assistant message
        st.session_state.history.append(("assistant", reply_text))

# Show conversation history
for sender, message in st.session_state.history:
    if sender == "user":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")
