import tkinter as tk
from tkinter import ttk

from deepl import Translator

# Create the main window
root = tk.Tk()
root.title("KoEsEn Translator")

# Set the theme to a modern one
style = ttk.Style(root)
style.theme_use("clam")

# Create a frame for the input field
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.pack(fill="x")

# Create a label and entry field for the input
input_label = ttk.Label(input_frame, text="Input Text:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry = ttk.Entry(input_frame, width=30)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a frame for the translation output
output_frame = ttk.Frame(root, padding="10 10 10 10")
output_frame.pack(fill="x")

# Create labels and text boxes for the translation output
languages = ["Spanish", "English", "Korean"]
language_codes = ["ES", "EN-GB", "KO"]
translation_labels = []
for i, language in enumerate(languages):
    label = ttk.Label(output_frame, text=f"{language} Translation:")
    label.grid(row=i, column=0, padx=5, pady=5)
    text_box = tk.Text(output_frame, width=30, height=5, font=("NanumGothic", 12))
    text_box.grid(row=i, column=1, padx=5, pady=5)
    translation_labels.append((language, text_box))

# Create a translate button
translator = Translator("DeepL-API-Key")  # Replace with your Deepl API key
translate_button = ttk.Button(root, text="Translate", command=lambda: translate_text(translator, language_codes, input_entry, translation_labels))
translate_button.pack(fill="x", padx=10, pady=10)

def translate_text(translator, language_codes, input_entry, translation_labels):
    # Get the input text from the entry field
    input_text = input_entry.get()

    # Use the Deepl API to translate the text
    translations = []
    for code in language_codes:
        result = translator.translate_text(input_text, target_lang=code)
        translations.append(result.text)

    # Display the translations in the output text boxes
    for i, (_, text_box) in enumerate(translation_labels):
        text_box.delete(1.0, "end")
        text_box.insert("end", translations[i])

root.mainloop()
