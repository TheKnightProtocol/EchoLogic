# app.py           
import streamlit as st        
from transcribe_audio import transcribe_audio                    
from summarize_text import       generate_summary    
           
st.title("EchoLogic – Voice to Docs")    
    
audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
if audio_file: 
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    transcript = transcribe_audio("temp_audio.wav")
    st.subheader("Transcript")
    st.write(transcript).  

    if st.button("Generate Summary"):
        summary = generate_summary(transcript)
        st.subheader("AI Summary") 
        st.write(summary)
                  