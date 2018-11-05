from networking import Client

client = Client()
client.connect('localhost', 9234)
client.send_data("Hello!")
client.send_input()

