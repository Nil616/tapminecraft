from mcpi.minecraft import Minecraft
from mcpi import block
import random
import types

# Initialize the Minecraft connection
mc = Minecraft.create()

class Agent:
    """Base class for Minecraft agents."""
    def __init__(self, name):
        self.name = name
        self.position = mc.player.getTilePos()

    def move(self, dx, dy, dz):
        self.position.x += dx
        self.position.y += dy
        self.position.z += dz
        mc.player.setTilePos(self.position.x, self.position.y, self.position.z)

    def place_block(self, block_type, x, y, z):
        mc.setBlock(x, y, z, block_type)

    def destroy_block(self, x, y, z):
        mc.setBlock(x, y, z, block.AIR)

    def send_message(self, message):
        mc.postToChat(f"<{self.name}> {message}")

class FunctionalAgent(Agent):
    """An agent that allows behaviors to be defined functionally."""
    def __init__(self, name):
        super().__init__(name)
        self.behaviors = []

    def add_behavior(self, behavior_function):
        self.behaviors.append(behavior_function)

    def run_behaviors(self):
        for behavior in self.behaviors:
            behavior(self)

class ReflectiveAgent(Agent):
    """An agent that uses reflection for dynamic behavior."""
    def add_method(self, name, func):
        setattr(self, name, types.MethodType(func, self))

    def invoke_method(self, name, *args, **kwargs):
        method = getattr(self, name, None)
        if method:
            return method(*args, **kwargs)
        else:
            raise AttributeError(f"Method {name} not found")
