from fastapi import FastAPI
import random
import time

app = FastAPI()

@app.get("/")
def root():
    start_time = time.time()
    x = sum(list(random.randint(0, 99999) for r in range(100000)))
    end_time = time.time()
    return {"value": x, "time": end_time-start_time}

@app.get("/{id}")
def some_id():
    start_time = time.time()
    x = sum(list(random.randint(0, 99999) for r in range(100000)))
    end_time = time.time()
    return {"value": x, "time": end_time-start_time}    