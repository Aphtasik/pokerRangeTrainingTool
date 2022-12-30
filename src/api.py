from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def status():
    return {"status": "ok"}


@app.get("/v1/hand")
def get_hand():
    

    return {}

