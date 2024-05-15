from gtts import gTTS
import PyPDF2

with open("book.pdf", "rb") as file: # Put the name of your file
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + " " 

tts = gTTS(text=text, lang="en") # Put the language of your file
tts.save("audio_paper.mp3") # Put the name of your output
