from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "good morning from fast api livereload works"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000) 