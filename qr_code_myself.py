import qrcode

user_name = input("Enter your name: ")
print("Welcome", user_name, "to read my short description")

myself_me = '''Assalamu alaikum. I am Abu Bakar Istiak, a dedicated and passionate programmer. My journey in the realm of programming has been both fulfilling and enriching. I find genuine happiness in the logic and creativity that coding demands.
With a keen interest in staying abreast of the latest technologies, I am committed to continuous learning and honing my skills. Problem-solving is not merely a task but a source of genuine excitement for me. I take pride in transforming ideas into functional code and am always eager to explore new challenges.
Collaboration is a value I hold in high regard, and I actively seek opportunities to engage with the programming community. Being part of a network where ideas are shared and knowledge is exchanged contributes significantly to my growth as a programmer.
As I navigate this dynamic field, I am enthusiastic about contributing meaningfully to the ever-evolving landscape of technology. Programming, for me, is not just a career; it is a pathway to both professional success and personal fulfillment.
Thank you for considering my introduction.'''

# Generate the QR code
qr_code_generate = qrcode.make(myself_me)

# Save the QR code to an image file (optional)
qr_code_generate.save('qr_code_show_myself_save.png')

# Display the QR code
qr_code_generate.show()
