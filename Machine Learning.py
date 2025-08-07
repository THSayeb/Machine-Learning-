import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": 'you are',
    "i was": 'you were',
    "i": 'you',
    "i'm": 'you are',
    "i'd": 'you would',
    "i've": 'you have',
    "i'll": 'you will',
    "my": 'your',
    "you are": 'i am',
    "you were": 'i was',
    "you've": 'i have',
    "you'll": 'i will',
    "your": 'my',
    "yours": 'mine',
    "you": 'me',
    "me": 'you'
}

pairs = [
    [
        r'my name is (.*)',
        ['Hello %1, How are you today?']
    ],
    [
        r'hi|hey|hello',
        ['Hello', 'Hey there']
    ],
    [
        r'what is your name ?',
        ['I am a bot created by Codingal Edu. Pvt. Ltd. You can call me JARVIS!']
    ],
    [
        r'how are you ?',
        ["I'm doing good. How about you?"]
    ],
    [
        r'sorry (.*)',
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r'I am fine',
        ['Great to hear that, How can I help you?']
    ],
    [
        r'I (.*) doing good',
        ["Nice to hear that", "How can I help you?"]
    ],
    [
        r'(.*) age?',
        ["I'm a computer program dude. Seriously you are asking me this?"]
    ],
    [
        r'what (.*) want ?',
        ["Make me an offer I can't refuse"]
    ],
    [
        r'(.*) created ?',
        ["Shreyan created me using Python's NLTK library. Top secret!"]
    ],
    [
        r'(.*) (location|city) ?',
        ['Bangalore, Karnataka']
    ],
    [
        r'how is weather in (.*)?',
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1", "Never even heard about %1"]
    ],
    [
        r'i work in (.*)?',
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days."]
    ],
    [
        r'(.*)raining in (.*)',
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r'how (.*) health(.*)',
        ["I'm a computer program, so I'm always healthy"]
    ],
    [
        r'(.*)sports?(.*)',
        ["I'm a very big fan of Football and Cricket"]
    ],
    [
        r'who (.*) sportsperson ?',
        ["Messi", "Ronaldo", "Rooney", "Virat", "M.S. Dhoni", "Rohit"]
    ],
    [
        r'who (.*) (moviestar|actor)?',
        ["Benedict Cumberbatch"]
    ],
    [
        r'I am looking for online guides and courses to learn data science, can you suggest?',
        ["GeeksforGeeks has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r'quit',
        ["Bye take care. See you soon :)", "It was nice talking to you. See you soon"]
    ]
]

def chat():
    print("Hi! I am a chatbot created by Codingal Edu. Pvt. Ltd. for your service")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()