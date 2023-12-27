import pyttsx3
import PyPDF2

def pdf_to_audio(pdf_path, output_path):
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    speaker = pyttsx3.init()

    full_text = ""

    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()  # Use pages instead of getPage
        full_text += text

    clean_text = full_text.strip().replace('\n', ' ')
    print(clean_text)

    speaker.save_to_file(clean_text, output_path)
    speaker.runAndWait()
    speaker.stop()

if __name__ == '__main__':
    pdf_to_audio('hello.pdf', 'hello.mp3')
