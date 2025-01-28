from Agent import ReflectiveAgent
from mcpi import block

def deploy_prison(agent):
    x, y, z = agent.position.x, agent.position.y, agent.position.z
    offsets = [
        (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1),  # Sides
        (1, 1, 0), (-1, 1, 0), (0, 1, 1), (0, 1, -1),  # Top sides
        (1, -1, 0), (-1, -1, 0), (0, -1, 1), (0, -1, -1),  # Bottom sides
        (0, 1, 0), (0, -1, 0)  # Top and bottom
    ]
    for dx, dy, dz in offsets:
        agent.place_block(block.OBSIDIAN.id, x + dx, y + dy, z + dz)
    agent.send_message("You cannot escape from this prison!")
    
prison_bot = ReflectiveAgent("PrisonBot")
prison_bot.add_method("deploy_prison", deploy_prison)
prison_bot.deploy_prison()