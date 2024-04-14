import asyncio
import socketio

sio = socketio.AsyncClient()


@sio.on('connect', namespace='/stocks')
async def connect():
    print('connected to server')
    await sio.emit('subscribe', {'events': ['SQQQ']}, namespace='/stocks')


@sio.on('disconnect', namespace='/stocks')
async def disconnect():
    print('disconnected from server')


@sio.on('subscribe', namespace='/stocks')
def subscribe(message):
    print(message)

@sio.on('exception', namespace='/stocks')
def exception(message):
    print(message)


async def start_server():
    await sio.connect('wss://web-socket.techglobetrading.com/stocks', transports=['websocket'], namespaces=['/stocks'])
    await sio.wait()

if __name__ == "__main__":
    asyncio.run(start_server())