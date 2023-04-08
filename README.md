# keylogger-python
This is a simple keylogger application that records keyboard inputs and saves them to a file. The application also sends the recorded file to a specified email address after 30 seconds.

Disclaimer: This application is intended for educational purposes only. It is not meant to be used for any illegal or malicious activities. The author of this application is not responsible for any damages caused by its use.

How to Use
Download or clone this repository to your local machine.
Install the required dependencies by running pip install.
Open the config.py file and enter your email address and password in the EMAIL_ADDRESS and EMAIL_PASSWORD variables, respectively. Also, enter the recipient's email address in the RECIPIENT_ADDRESS variable. 

NOTE
Although, due to simplicity of the code, the author already declared the required variables within the code scripts as required.

Run the keylogger.py file.
The keylogger will start recording keystrokes and save them to a file called keys.txt in the same directory as the keylogger.py file.
After 30 seconds, the keylogger will send the keys.txt file to the specified email address.