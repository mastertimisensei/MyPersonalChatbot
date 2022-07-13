from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

my_bot = ChatBot(name = "TimiBot", read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbox.logic.BestMatch'])

small_talk = ['hi there!','hi','how do you do?','how are you?','i\'m cool.']