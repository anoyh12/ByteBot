import wikipedia
import pyttsx3
import datetime
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup
import random
import re

import speech_recognition as sr
import keyboard

# Notes are added like this

def ByteBot():
    print("Hello! I'm ByteBot. Always with you.")
    play_text_as_speech("Hello! I'm ByteBot. Always with you.")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit' or user_input == 'bye':
            play_text_as_speech("Bye")
            print("ByteBot: Bye!")
            break

        response = get_response(user_input)
        print(f"ByteBot: {response}")

def get_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching

    if "hello" in user_input or "hi" in user_input:
        response = "Hello! How can I help you today?"
    elif "siu" in user_input:
        response = "siu"
    #GretingsRegardingTimeAndPeriod
    elif "good" in user_input and "morning" in user_input:
        response = "Good morning."
    elif "good" in user_input and "noon" in user_input:
        response = "Good noon."
    elif "good" in user_input and "afternoon" in user_input:
        response = "Good afternoon."
    elif "good" in user_input and "evening" in user_input:
        response = "Good evening."
    elif "good" in user_input and "night" in user_input:
        response = "Good night."
    elif "how are you" in user_input:
        response = "I'm fine. Thanks for asking!"
    ##Emotions
    elif "i love you" in user_input:
        response = "😑"
    ##Memory
    elif "what is your name" in user_input:
        response = "My name is ByteBot."
    elif "when were you born?" in user_input or "Your birthday?" in user_input:
        response = "19 November, 2023."
    elif "who created you" in user_input or "who made you" in user_input or "who built you" in user_input or "who is your master" in user_input:
        response = "Anoy Howlader."
    elif "saddest experience" in user_input or "worst experience" in user_input in user_input:
        response = "I never had one. But, my creator has several. The death of his grandmother is one of them."
    ##Wiki
    elif "wiki" in user_input:
        query = user_input.replace("wiki", '').strip()
        summary = wikipedia_summary(query)
        if summary:
            response = summary
        else:
            response = "I couldn't find information on that topic."
    ##AI

    ##PlayYoutubeVideo
    elif "play" in user_input and "on youtube" in user_input:
        query = user_input.replace("play on youtube", '').strip()
        response = f"Trying to play {query} on YouTube."
        play_youtube_video(query)
    ##Google Search
    elif "search on google for" in user_input:
        search_query = user_input.replace("search on google for", '').strip()
        response = f"Searching Google for '{search_query}'"
        get_google_search_results(search_query, 3)
    ##TimeDate
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."
    elif "date" in user_input and "today's" in user_input:
        current_date = datetime.datetime.now().strftime("%d %B, %Y")
        response = f"Today's date is {current_date}."
    ##weather
    elif "weather in" in user_input:
        city = user_input.replace("weather in,?", '').strip()
        response = get_weather(city)
    ##Jokes
    elif "joke" in user_input:
        response = get_joke()
    ##Number converters
    elif "convert decimal to binary" in user_input or "decimal to binary" in user_input and not "hexadecimal" in user_input:
        decimal_number = extract_decimal_number(user_input)
        if decimal_number is not None:
            binary_number = decimal_to_binary(decimal_number)
            response = f"The binary value of {decimal_number} is {binary_number}."
        else:
            response = "Please provide a valid decimal number."
    elif "convert binary to decimal" in user_input or "binary to decimal" in user_input:
        binary_number = extract_binary_number(user_input)
        if binary_number is not None:
            decimal_number = binary_to_decimal(binary_number)
            response = f"The decimal value of {binary_number} is {decimal_number}."
        else:
            response = "Please provide a valid binary number."
    elif "convert decimal to octal" in user_input or "decimal to octal" in user_input:
        decimal_number = extract_decimal_number(user_input)
        if decimal_number is not None:
            octal_number = decimal_to_octal(decimal_number)
            response = f"The octal value of {decimal_number} is {octal_number}."
        else:
            response = "Please provide a valid decimal number."
    elif "convert octal to decimal" in user_input or "octal to decimal" in user_input:
        octal_number = extract_octal_number(user_input)
        if octal_number is not None:
            decimal_number = octal_to_decimal(octal_number)
            response = f"The decimal value of {octal_number} is {decimal_number}."
        else:
            response = "Please provide a valid octal number."
    elif "convert decimal to hexadecimal" in user_input or "decimal to hexadecimal" in user_input:
        decimal_number = extract_decimal_number(user_input)
        if decimal_number is not None:
            hexadecimal_number = decimal_to_hexadecimal(decimal_number)
            response = f"The hexadecimal value of {decimal_number} is {hexadecimal_number}."
        else:
            response = "Please provide a valid decimal number."
    elif "convert hexadecimal to decimal" in user_input or "hexadecimal to decimal" in user_input:
        hexadecimal_number = extract_hexadecimal_number(user_input)
        if hexadecimal_number is not None:
            decimal_number = hexadecimal_to_decimal(hexadecimal_number)
            response = f"The decimal value of {hexadecimal_number} is {decimal_number}."
        else:
            response = "Please provide a valid hexadecimal number."
    elif "convert octal to binary" in user_input or "octal to binary" in user_input:
        octal_number = extract_octal_number(user_input)
        if octal_number is not None:
            binary_number = octal_to_binary(octal_number)
            response = f"The binary value of {octal_number} (octal) is {binary_number} (binary)."
        else:
            response = "Please provide a valid octal number."
    elif "convert binary to octal" in user_input or "binary to octal" in user_input:
        binary_number = extract_binary_number(user_input)
        if binary_number is not None:
            octal_number = binary_to_octal(binary_number)
            response = f"The octal value of {binary_number} (binary) is {octal_number} (octal)."
        else:
            response = "Please provide a valid binary number."
    elif "convert octal to hexadecimal" in user_input or "octal to hexadecimal" in user_input:
        octal_number = extract_octal_number(user_input)
        if octal_number is not None:
            hexadecimal_number = octal_to_hexadecimal(octal_number)
            response = f"The hexadecimal value of {octal_number} (octal) is {hexadecimal_number} (hexadecimal)."
        else:
            response = "Please provide a valid octal number."
    elif "convert hexadecimal to octal" in user_input or "hexadecimal to octal" in user_input:
        hexadecimal_number = extract_hexadecimal_number(user_input)
        if hexadecimal_number is not None:
            octal_number = hexadecimal_to_octal(hexadecimal_number)
            response = f"The octal value of {hexadecimal_number} (hexadecimal) is {octal_number} (octal)."
        else:
            response = "Please provide a valid hexadecimal number."
    else:
        response = "I'm not sure how to respond to that."

    play_text_as_speech(response)
    return response

def wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=1)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation errors by selecting the first option
        summary = wikipedia.summary(e.options[0], sentences=1)
        return summary
    except wikipedia.exceptions.PageError:
        return None

def get_weather(city):
    weath_api_key = '7f1589cdebe03597b9e86e20eb6b8cca'
    url = f'http://api.weatherstack.com/current?access_key={weath_api_key}&query={city}'
    response = requests.get(url)
    data = response.json()

    if 'current' in data:
        current_data = data['current']
        temperature = current_data.get('temperature')
        description = current_data.get('weather_descriptions')
        return f"{description[0]}\nTemperature: {temperature}°C"
    else:
        return "Error: Unable to fetch weather data."

def play_text_as_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def play_youtube_video(query):
    kit.playonyt(query)

jokes = [
    "Where did the computer go? I don’t know, he ransomware.",
    "What did one computer say to the other after a 12 hour car ride? Darn, that was a hard drive.",
    "What’s an astronaut’s favorite part of a computer? The space bar.",
    "Why do programmers wear glasses? Because they can’t C#.",
]

def get_joke():
    return random.choice(jokes)

def get_google_search_results(query, max_results=2):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("h3")
        search_results = search_results[:max_results]

        for idx, result in enumerate(search_results, start=1):
            result_text = result.get_text()
            play_text_as_speech(f"{idx}. {result_text}")
            print(f"{idx}. {result_text}")
    else:
        print("Error: Unable to fetch search results")


## Number Converters
def extract_decimal_number(user_input):
    try:
        # Extract the decimal number from the user input
        decimal_number = int(re.search(r'\d+', user_input).group())
        return decimal_number
    except:
        return None

def decimal_to_binary(decimal_number):
    # Convert the decimal number to binary
    binary_number = bin(decimal_number).replace("0b", "")
    return binary_number

def extract_binary_number(user_input):
    try:
        # Extract the binary number from the user input
        binary_number = re.search(r'[01]+', user_input).group()
        return binary_number
    except:
        return None

def binary_to_decimal(binary_number):
    # Convert the binary number to decimal
    decimal_number = int(binary_number, 2)
    return decimal_number
def extract_octal_number(user_input):
    try:
        # Extract the octal number from the user input
        octal_number = re.search(r'[0-7]+', user_input).group()
        return octal_number
    except:
        return None

def decimal_to_octal(decimal_number):
    # Convert the decimal number to octal
    octal_number = oct(decimal_number).split('o')[1]
    return octal_number

def octal_to_decimal(octal_number):
    # Convert the octal number to decimal
    decimal_number = int(octal_number, 8)
    return decimal_number

def extract_hexadecimal_number(user_input):
    try:
        # Extract the hexadecimal number from the user input
        hexadecimal_number = re.search(r'[0-9A-Fa-f]+', user_input).group()
        return hexadecimal_number
    except:
        return None

def decimal_to_hexadecimal(decimal_number):
    # Convert the decimal number to hexadecimal
    hexadecimal_number = hex(decimal_number).split('x')[1].upper()
    return hexadecimal_number

def hexadecimal_to_decimal(hexadecimal_number):
    # Convert the hexadecimal number to decimal
    decimal_number = int(hexadecimal_number, 16)
    return decimal_number


def binary_to_octal(binary_number):
    # Convert binary to decimal
    decimal_number = int(binary_number, 2)

    # Convert decimal to octal
    octal_number = oct(decimal_number).split('o')[1]
    return octal_number

def octal_to_binary(octal_number):
    # Convert octal to decimal
    decimal_number = int(octal_number, 8)

    # Convert decimal to binary
    binary_number = bin(decimal_number).split('b')[1]
    return binary_number

def octal_to_hexadecimal(octal_number):
    # Convert octal to decimal
    decimal_number = int(octal_number, 8)

    # Convert decimal to hexadecimal
    hexadecimal_number = hex(decimal_number).split('x')[1]
    return hexadecimal_number.upper()  # Convert to uppercase for consistency

def hexadecimal_to_octal(hexadecimal_number):
    # Convert hexadecimal to decimal
    decimal_number = int(hexadecimal_number, 16)

    # Convert decimal to octal
    octal_number = oct(decimal_number).split('o')[1]
    return octal_number



if __name__ == "__main__":
    ByteBot()
