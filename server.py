# karl ramberg, paul ramberg, trenton morgan, isaih slater
# pickhacks 2019 - 3/1/2019
import generator
import json
from sanic import Sanic
from sanic import response


app = Sanic()
diet = []

@app.route('/peanutbutter')
async def test(request):
    return response.json({'hello': 'world'})

@app.route('/')
async def test(request):
    return await response.file('./website/index.html')

@app.get("/jsonget")
def handle_request(request):
    return response.text(generator.newRecipe())

@app.post("/jsonyes")
def post_handler(request):
    ingredients = json.loads(request.body)

    # for ingredient in ingredients:
    #     for food in diet:
    #         if(ingredient["name"] == food.name):
    #             food.probability += 0.1
    #             food.probability = chomp(food.probability, 0.01, 1.0)

    generator.addPairs(ingredients);

    return response.json({ "received": True, "message": request.json })

@app.post("/jsonmaybe")
def post_json(request):
    return response.json({ "received": True, "message": request.json })

@app.post("/jsonno")
def post_json(request):
    ingredients = json.loads(request.body)

    # for ingredient in ingredients:
    #     for food in diet:
    #         if(ingredient["name"] == food.name):
    #             food.probability -= 0.1
    #             food.probability = chomp(food.probability, 0.01, 1.0)

    return response.json({ "received": True, "message": request.json })

def chomp(num, low, high):
    if num < low:
        return low
    elif num > high:
        return high
    else:
        return num

diet = generator.setDiet()
app.static("/website", "./website")
app.run("0.0.0.0", port=80)
