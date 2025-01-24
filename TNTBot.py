from Agent import ReflectiveAgent
from mcpi import block

def deploy_tnt(agent):
    x, y, z = agent.position.x, agent.position.y, agent.position.z
    agent.place_block(block.TNT.id, x + 1, y, z)
    agent.send_message("TNT placed!")

def ignite_tnt(agent):
    x, y, z = agent.position.x, agent.position.y, agent.position.z
    agent.place_block(block.REDSTONE_BLOCK.id, x + 2, y, z)
    agent.send_message("BOOM!")

tnt_bot = ReflectiveAgent("TNTBot")
tnt_bot.add_method("deploy_tnt", deploy_tnt)
tnt_bot.add_method("ignite_tnt", ignite_tnt)

# Demonstration
tnt_bot.invoke_method("deploy_tnt")
tnt_bot.invoke_method("ignite_tnt")
tnt_bot.deploy_tnt()
