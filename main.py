import io
from fastapi import FastAPI, File
from ocr import clova
from PIL import Image

app = FastAPI()

@app.post("/receipt")
async def receipt_scan(file: bytes = File()):
    img = Image.open(io.BytesIO(file))
    resized = img.resize((1080, 1440))
    
    buf = io.BytesIO()
    resized.save(buf, format='PNG')

    res = clova(buf.getvalue())
    return res
