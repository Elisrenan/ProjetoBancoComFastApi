from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.post("/accounts")
def create_account(account: dict):
  # Código para criar uma nova conta bancária
  return {"status": "success"}
