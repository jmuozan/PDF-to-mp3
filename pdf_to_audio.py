from gtts import gTTS
import PyPDF2

# Open the PDF file
with open("book.pdf", "rb") as file: # Open file
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    # Extract text of each page
    for page in reader.pages:
        text += page.extract_text() + " "  # Space after each page text

# gTTS with the extracted text
tts = gTTS(text=text, lang="en") # Language
tts.save("audio_paper.mp3") # Output
