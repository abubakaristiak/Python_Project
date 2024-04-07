import tkinter as tk
from tkinter import scrolledtext
import requests
import os
import openai

# Set up your OpenAI API key as an environment variable
os.environ['OPENAI_API_KEY'] = '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'

# Set up your Pexels API key
pexels_api_key = 'LY81GZhabWQTgBaXrQ9yTqL6RlW5If4J34IF6a7QrOfAoVfvlE554qxP'

class LightGPT_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LightGPT- Nano")

        # Styling for the title text
        title_font = ("Arial", 16, 'bold')

        # Title label
        self.title_label = tk.Label(root, text="LightGPT- CREATED by Abu Bakar Istiak", font=title_font)
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
            fg='#cbc7d6'
        )
        self.messages_text.pack(padx=10, pady=10)

        # Styling for the prompt bar (user input)
        self.user_input = tk.Entry(
            root, width=50,
            font=("Roboto", 12),
            bg='#48464d',
            relief=tk.GROOVE,
            borderwidth=2,
            fg='#cbc7d6'
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
            # Query Pexels API for images related to the user's input
            pexels_url = f'https://api.pexels.com/v1/search?query={user_message}&per_page=3'
            headers = {'Authorization': pexels_api_key}
            response = requests.get(pexels_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                # Append image URLs to messages
                for photo in data['photos']:
                    self.messages.append({"role": "assistant", "content": photo['src']['large']})
            else:
                self.messages.append({"role": "assistant", "content": "Sorry, couldn't find any images."})
            # Use OpenAI to generate a response
            completion = openai.Completion.create(
                engine="text-davinci-002",  # Choose an appropriate engine
                prompt=" ".join([msg["content"] for msg in self.messages]),  # Concatenate all messages as prompt
                max_tokens=50  # Adjust max_tokens as needed
            )
            assistant_reply = completion.choices[0].text.strip()
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
                # Display images if available
                if 'http' in content:
                    self.insert_image(content)
                else:
                    self.messages_text.insert(tk.END, f"{role}: {content}\n\n")

        self.messages_text.config(state=tk.DISABLED)
        self.messages_text.tag_configure('heading', font=('Roboto', 12, 'bold'))

    def insert_image(self, url):
        try:
            # Download the image from URL
            image = requests.get(url)
            # Create a Tkinter PhotoImage object from the image data
            photo = tk.PhotoImage(data=image.content)
            # Insert the image into the scrolled text widget
            self.messages_text.image_create(tk.END, image=photo)
            # Ensure the image is retained by keeping a reference to the PhotoImage object
            self.messages_text.image = photo
            self.messages_text.insert(tk.END, '\n\n')
        except Exception as e:
            print(f"Error inserting image: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    Nano_GPT_gui = LightGPT_GUI(root)
    root.mainloop()
