import sys
import mcpi.minecraft as Minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import mcpi.event as events
import random
from Agent import FunctionalAgent

mc = Minecraft.Minecraft.create()

def insult_behavior(agent):
    insults = ["gilipollas", "idiota", "imbecil", "tonto", "estupido"]
    agent.send_message(random.choice(insults))

# Initialize InsultBot
insult_bot = FunctionalAgent("InsultBot")
insult_bot.add_behavior(insult_behavior)
insult_bot.add_behavior(lambda agent: agent.send_message("I'm InsultBot!"))

print("InsultBot initialized and running...")
mc.postToChat("InsultBot initialized and running...")

while True:
    chat_events = mc.events.pollChatPosts()
    for chat_event in chat_events:
        print(f"Received chat event: {chat_event.message}")
        if chat_event.message != "adios":
            insult_bot.run_behaviors()
            break
        if chat_event.message == "adios":
            mc.postToChat("Adios, hasta luego")
            exit()
