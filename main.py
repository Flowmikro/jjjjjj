from fastapi import FastAPI

app = FastAPI(name='API')


@app.get('/')
async def start():
    return 'dvsdvsd'
