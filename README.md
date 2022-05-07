## Sentiment Analyzer ##

A simple API service to show sentiment score by sending query string.

### How to run the app ###

#### Install git and clone this repo ####
```
git clone https://github.com/cindyliuyn/FastAPI-HuggingFace.git
```

#### Build docker image and run it ####
```
cd FastAPI-HuggingFace
docker build -t hugging-face .
docker run -p 8000:8000 hugging-face
```

#### Access the server ####
```
GET http://${IP Address}/health

POST http://${IP Address}/get-sentiment
Example Body:
{
    "query_string": "Happy"
}
```