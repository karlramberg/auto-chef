from sanic import Sanic
from sanic import response
from sanic.response import json

app = Sanic()

@app.route('/peanutbutter')
async def test(request):
    return json({'hello': 'world'})

@app.route('/')
async def test(request):
    return await response.file('./website/index.html')

app.static("/website", "./website")
app.run("127.0.0.1", port=80)
