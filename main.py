from fastapi import FastAPI, File
from ocr import clova

app = FastAPI()

@app.post("/receipt")
async def receipt_scan(file: bytes = File()):
    res = clova(file)
    return res
