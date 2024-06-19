import openai
import tkinter as tk
from tkinter import scrolledtext

openai.api_key = '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'


class LightGPT_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LightGPT- Nano")


        # Styling for the title text
        title_font = ("Arial", 16, 'bold')

        # Title label
        self.title_label = tk.Label(root, text="LightGPT- CREATED by Abu Bakar Istiak",font=title_font)
        self.title_label.pack(pady=10)

        # Styling for the output box
        self.messages_text = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=60, height=20,
            font=("Roboto", 12),
            bg='#474547',
            relief=tk.GROOVE,
            borderwidth=2,
            padx=10,
            pady=10,
            fg = '#cbc7d6'
        )
        self.messages_text.pack(padx=10, pady=10)

        # Styling for the prompt bar (user input (what you want)
        self.user_input = tk.Entry(
            root, width=50,
            font=("Roboto", 12),
            bg='#48464d',
            relief=tk.GROOVE,
            borderwidth=2,
            fg = '#cbc7d6'
        )
        self.user_input.pack(pady=10)

        # Styling for the send button
        self.send_button = tk.Button(
            root, text="Send", command=self.send_message,
            font=("Roboto", 12),
            bg='#4caf50',
            fg='#ffffff',
            relief=tk.GROOVE,
            borderwidth=2
        )
        self.send_button.pack(pady=10)

        # Bind the Enter key to execute the program
        self.user_input.bind("<Return>", lambda event: self.send_message())

        self.messages = [{"role": "system", "content": "You are a kind helpful assistant."}]
        self.update_chat()

    def send_message(self):
        user_message = self.user_input.get()
        if user_message:
            self.messages.append({"role": "user", "content": user_message})
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
            assistant_reply = chat.choices[0].message.content
            self.messages.append({"role": "assistant", "content": assistant_reply})
            self.update_chat()
            # Clear the user input after sending the message
            self.user_input.delete(0, tk.END)

    def update_chat(self):
        self.messages_text.config(state=tk.NORMAL)
        self.messages_text.delete(1.0, tk.END)
        for message in self.messages:
            role = message['role'].capitalize()
            content = message['content']

            # Special formatting for system messages (headings)
            if message['role'] == 'system':
                self.messages_text.insert(tk.END, f"{role}: {content}\n\n", 'heading')
            else:
                self.messages_text.insert(tk.END, f"{role}: {content}\n\n")

        self.messages_text.config(state=tk.DISABLED)
        self.messages_text.tag_configure('heading', font=('Roboto', 12, 'bold'))


if __name__ == "__main__":
    root = tk.Tk()
    Nano_GPT_gui = LightGPT_GUI(root)
    root.mainloop()
