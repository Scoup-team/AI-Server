import easyocr
reader = easyocr.Reader(['ko','en'])
results = reader.readtext('receipt1.jpeg')
print(results)
