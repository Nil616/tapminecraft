import sys
import mcpi.minecraft as Minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import mcpi.event as events
import random
from Agent import FunctionalAgent

def anvil_trap(agent):
    x, y, z = agent.position.x, agent.position.y, agent.position.z
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
    for dx, dz in offsets:
        agent.place_block(block.ANVIL.id, x + dx, y + 30, z + dz)
    agent.send_message("Anvil trap deployed!")

anvil_bot = FunctionalAgent("AnvilBot")
anvil_bot.add_behavior(anvil_trap)
for int in range(10):
    anvil_bot.run_behaviors()
