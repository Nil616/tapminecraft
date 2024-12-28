import sys
import mcpi.minecraft as Minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import mcpi.event as event

mc = Minecraft.Minecraft.create()

mc.postToChat("Hello Minecraft World")
pos = mc.player.getTilePos()
agent = minecraftstuff.MinecraftTurtle(mc, pos)
agent.penblock(block.TNT)
agent.backward(19)
agent.penblock(block.REDSTONE_BLOCK)
agent.backward(1)


while True:
    chat_events = mc.events.pollChatPosts()
    for chat_event in chat_events:
        if chat_event.entityId == mc.getPlayerEntityId("Caoticus6") and chat_event.message == "hola":
            mc.postToChat("Hola, como estas?")
            break
        if chat_event.entityId == mc.getPlayerEntityId("Caoticus6") and chat_event.message == "adios":
            mc.postToChat("Adios, hasta luego")
            exit()
        
        