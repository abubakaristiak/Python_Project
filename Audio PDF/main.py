import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfile


book = askopenfile(mode='rb')  
if book is not None:
    pdfreader = PyPDF2.PdfReader(book)  
    pages = len(pdfreader.pages)  
    
    player = pyttsx3.init()

    for num in range(pages):
        page = pdfreader.pages[num]
        text = page.extract_text()
        if text:  
            player.say(text)

    player.runAndWait()
