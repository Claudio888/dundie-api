from fastapi import FastAPI

app = FastAPI(
    title="dundie",
    version="0.1.0",
    description="dundie is a rewards API",
)


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/teste")
def test():
    return {"test": "1"}
