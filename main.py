import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# Basic chatbot responses
def chatbot_response(text):
    text = text.lower()
    if "hello" in text:
        return "Hello! How can I help you?"
    elif "your name" in text:
        return "I am your voice chatbot assistant."
    elif "how are you" in text:
        return "I'm doing great, thank you!"
    elif "bye" in text:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."

# Speak out text
def speak(text):
    print("Bot:", text)
    tts.say(text)
    tts.runAndWait()

# Listen for voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You:", query)
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Sorry, my speech service is down."

# Main loop
if __name__ == "__main__":
    speak("Hi! I am your voice chatbot. Say something!")
    while True:
        user_input = listen()
        if "bye" in user_input.lower():
            response = chatbot_response(user_input)
            speak(response)
            break
        response = chatbot_response(user_input)
        speak(response)
