from fastapi import FastAPI

app = FastAPI(title="Health Core API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Health Core API Online"}