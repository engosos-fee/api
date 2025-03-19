from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running successfully!"}

@app.get("/run")
def run_script():
    url = "http://ososbus.rf.gd/os.php"
    try:
        response = requests.get(url)
        return {"status": "success", "response": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}
