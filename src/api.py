from fastapi import FastAPI
from src.card_model.deck_model import Deck

app = FastAPI()


@app.get("/")
def status():
    return {"status": "ok"}


@app.get("/v1/hand")
def get_hand():
    cards = Deck()
    return {"hand": cards.get_hand(), "representation": cards.get_hand_str()}
