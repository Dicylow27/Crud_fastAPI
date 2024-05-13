from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def primer_mensaje():
    return "Hola Mundo"