from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


sentiment_model = pipeline("sentiment-analysis")


def get_sentiment(query_sentence):
    # sentiment_query_sentence = get_random_comment(top_comments)
    sentiment = sentiment_model(query_sentence)
    print(f"Sentiment test: {query_sentence} == {sentiment}")
    return sentiment


class PredictionRequest(BaseModel):
    query_string: str


app = FastAPI()


@app.get("/health")
def health():
    return "Service is online."


@app.post("/get-sentiment")
def my_endpoint(request: PredictionRequest):
    return get_sentiment(request.query_string)
