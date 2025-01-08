import pyautogui
import time
import keyboard
import sys

# Maximum number of messages that can be sent
MAX_MESSAGES = 25

def send_message(message, count):
    # Enforce maximum message limit
    if count > MAX_MESSAGES:
        print(f"\nWarning: Count reduced to maximum limit of {MAX_MESSAGES} messages")
        count = MAX_MESSAGES

    # Add a 5-second delay to give time to focus on WhatsApp chat
    print("You have 5 seconds to focus on the WhatsApp chat input box...")
    time.sleep(5)
    
    messages_sent = 0
    print("Spamming started! Press 'q' to stop...")
    
    try:
        while messages_sent < count:
            if keyboard.is_pressed('q'):
                print("\nSpamming stopped by user!")
                break
                
            # Type and send message
            pyautogui.typewrite(message)
            pyautogui.press('enter')
            
            messages_sent += 1
            print(f"Messages sent: {messages_sent}")
            
            # Small delay to prevent system overload
            time.sleep(0.5)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print(f"\nTotal messages sent: {messages_sent}")

def main():
    print("WhatsApp Spammer - Press 'q' at any time to stop")
    print(f"Maximum messages allowed: {MAX_MESSAGES}")
    print("-" * 50)
    
    # Get message and count from user
    message = input("Enter the message you want to spam: ")
    while True:
        try:
            count = int(input("How many times do you want to send the message? "))
            if count <= 0:
                print("Please enter a positive number!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    print("\nINSTRUCTIONS:")
    print("1. Open WhatsApp Web or Desktop")
    print("2. Select the chat where you want to spam")
    print("3. Click on the message input box")
    print("4. The spam will start in 5 seconds")
    print("5. Press 'q' at any time to stop the spam")
    
    # Start spamming
    send_message(message, count)

if __name__ == "__main__":
    main() 