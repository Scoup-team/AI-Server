import cv2
from hangul_utils import split_syllables, join_jamos
from symspellpy import SymSpell, Verbosity


class CustomOCR():
  
  def __init__(self):
    import easyocr
    self.reader = easyocr.Reader(['ko'])
  
  def send_info(self, ):
    path = 'receipt1.jpeg'
    img = cv2.imread(path)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    text = self.reader.readtext(img)
    result_words = []

    for arr in text:
        result_words.append(arr[-2])

    # 오타 교정
    sym_spell = SymSpell(max_dictionary_edit_distance=1)
    sym_spell.load_dictionary('menu.txt', 0, 1)

    for i in range(len(result_words)):
        term = result_words[i]
        term = split_syllables(term)
        suggestions = sym_spell.lookup(term, Verbosity.ALL, max_edit_distance=1)
        for sugg in suggestions:
            result_words[i] = join_jamos(sugg.term)

    return result_words


lens_ocr = CustomOCR()
menuinfo = lens_ocr.send_info()
print(menuinfo)
