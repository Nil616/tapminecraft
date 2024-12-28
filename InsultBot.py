import sys
import mcpi.minecraft as Minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import mcpi.event as event
import random

mc = Minecraft.Minecraft.create()
insults = ["gilipollas", "idiota", "imbécil", "tonto", "estúpido"]

while True:
    chat_events = mc.events.pollChatPosts()
    for chat_event in chat_events:
        if chat_event.message != "adios":
            insult = random.choice(insults)
            mc.postToChat(insult)
            break
        if chat_event.message == "adios":
            mc.postToChat("Adios, hasta luego")
            exit()