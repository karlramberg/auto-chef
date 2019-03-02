# karl ramberg, paul ramberg, trenton morgan, isaih slater
# pickhacks 2019 - 3/1/2019

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

@app.route('/json')
def post_json(request):
    return json("received": True, "message": request.json)

app.static("/website", "./website")
app.run("127.0.0.1", port=80)
