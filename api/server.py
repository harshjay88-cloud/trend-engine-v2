from fastapi import FastAPI

app = FastAPI()

@app.get("/trends")

def trends():

    return {"message":"trend engine running"}
