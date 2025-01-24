import pytest
import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Agent import FunctionalAgent, ReflectiveAgent

@pytest.fixture
def functional_agent():
    return FunctionalAgent("TestAgent")

@pytest.fixture
def reflective_agent():
    return ReflectiveAgent("TestAgent")

def test_functional_agent(functional_agent):
    def behavior(agent):
        agent.test_value = "behavior executed"
    
    functional_agent.add_behavior(behavior)
    functional_agent.run_behaviors()
    
    assert hasattr(functional_agent, 'test_value')
    assert functional_agent.test_value == "behavior executed"

def test_reflective_agent(reflective_agent):
    def dynamic_method(self):
        return "dynamic method executed"
    
    reflective_agent.add_method("dynamic_method", dynamic_method)
    result = reflective_agent.invoke_method("dynamic_method")
    
    assert result == "dynamic method executed"

def test_functional_agent_lambda(functional_agent):
    functional_agent.add_behavior(lambda agent: setattr(agent, 'test_value', "lambda executed"))
    functional_agent.run_behaviors()
    
    assert hasattr(functional_agent, 'test_value')
    assert functional_agent.test_value == "lambda executed"
    
def test_reflective_agent_direct_call(reflective_agent):
    def dynamic_method(self):
        return "dynamic method executed"
    
    reflective_agent.add_method("dynamic_method", dynamic_method)
    result = reflective_agent.dynamic_method()
    
    assert result == "dynamic method executed"