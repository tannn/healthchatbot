from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

#agent = Agent.load(...)
interpreter = RasaNLUInterpreter("models/current/nlu/")
agent = Agent.load("models/current/dialogue", interpreter=interpreter)
#input_channel = WebChatInput(static_assets_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'index.html'))
agent.handle_channels([SocketIOInput()], 5500, serve_forever=True)