from fastapi import FastAPI
from fastapi.responses import JSONResponse  # Using JSONResponse to convert the python dictionary to JSON format.
from web_scraping import *

app = FastAPI()

@app.get("/")
def read_root():
    response = JSONResponse(content=gpu_prices_map)

    '''
      In the below lines I'm handling CORS error which occurs because I am opening index.html in browser which opens as a file domain and in that I'm trying to fetch data from HTTP domain which is restricted due to security policy. Hence in the following lines I am setting HTTP headers to manage CORS and telling the browser which domains are allowed to make requests to the server.
    '''

    response.headers["Access-Control-Allow-Origin"] = "*"  # This allows all domains to make requests.
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS" # 
    response.headers["Access-Control-Allow-Headers"] = "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range"

    return response