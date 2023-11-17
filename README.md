# ByteBot
A python chatbot fetching Wikipedia, playing YouTube, sharing jokes, weather updates, Google searches, number conversions, time info. Modular for expansion, ideal for AI projects.

# ByteBot is a Python-based chatbot capable of interacting with users through text input. It utilizes various APIs and libraries to perform tasks ranging from fetching information from Wikipedia, playing YouTube videos, retrieving weather data, telling jokes, conducting Google searches, and performing number conversions.

# Features
Conversation Handling: ByteBot engages in conversation by responding to greetings, emotions, and specific queries.
Wikipedia Queries: It can retrieve summaries of Wikipedia topics based on user input.
YouTube Video Playback: ByteBot can search and play YouTube videos based on user queries.
Google Search: It conducts Google searches and retrieves a specified number of search results.
Time and Date Information: ByteBot provides current time and today's date when prompted.
Weather Information: It fetches and presents weather details for specified cities.
Jokes: ByteBot entertains users with computer-related jokes.
Number Conversions: It performs conversions between decimal, binary, octal, and hexadecimal numbers.
Speech Synthesis: ByteBot can convert text responses into speech using pyttsx3.
# Modules and Libraries Used
wikipedia for accessing Wikipedia content
pyttsx3 for speech synthesis
datetime for handling date and time
pywhatkit for playing YouTube videos
requests for making HTTP requests
BeautifulSoup from bs4 for web scraping
random for generating random elements
re for regular expressions
speech_recognition for speech recognition
# Structure
The code contains functions to handle various user queries and interactions.
It's designed to continuously engage with the user until an exit command is received.
# Extensibility
The code structure allows for easy expansion by adding more functionality or integrating additional APIs.
Each specific task or interaction is handled by dedicated functions, promoting modularity and ease of maintenance.
# Usage
Users can interact with ByteBot by entering text-based queries or commands.
The bot responds with relevant information, performs actions, or communicates with APIs to fulfill user requests.
This code can serve as a foundational framework for a conversational bot with expandable functionality, suitable for learning, experimentation, or as a base for more sophisticated chatbot projects.
