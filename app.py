from fastapi import FastAPI




app = FastAPI()



@app.get('/')
async def hello():
    return {'message':'Hello Developer'}

@app.get('/about')
async def About():
    return {'message':'Full Stack Developer'}
