from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

interpreter = RasaNLUInterpreter("models/current/nlu/")
agent = Agent.load("models/current/dialogue", interpreter=interpreter)
agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)