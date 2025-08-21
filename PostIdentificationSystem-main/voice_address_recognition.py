import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

def convert_to_wav(uploaded_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Convert to wav if needed
    if uploaded_file.name.endswith(".mp3"):
        sound = AudioSegment.from_mp3(file_path)
        file_path_wav = file_path.replace(".mp3", ".wav")
        sound.export(file_path_wav, format="wav")
    elif uploaded_file.name.endswith(".m4a"):
        sound = AudioSegment.from_file(file_path, format="m4a")
        file_path_wav = file_path.replace(".m4a", ".wav")
        sound.export(file_path_wav, format="wav")
    else:
        file_path_wav = file_path  # Already wav

    return file_path_wav

def recognize_speech(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "Speech recognition service unavailable."

def app():
    st.title("Voice-Based Address Recognition")
    st.write("Upload a voice recording to convert it into a textual address.")

    audio_file = st.file_uploader("Upload Voice Recording", type=["wav", "mp3", "m4a"])
    if audio_file:
        st.audio(audio_file)

        with st.spinner("Transcribing audio..."):
            wav_path = convert_to_wav(audio_file)
            transcription = recognize_speech(wav_path)

        st.success("Transcribed Address:")
        st.write(transcription)
