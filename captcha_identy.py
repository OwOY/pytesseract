import cv2
import pytesseract


def read_word():
    img = cv2.imread(r'captcha.png')
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 灰階設定
    (h, w) = gry.shape[:2] # 取得圖像長寬
    gry = cv2.resize(gry, (w*5, h*5)) # 重製圖片大小
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None) # 型態變換(先膨脹後侵蝕)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # 設置圖片臨界點，增強對比
    pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'
    text = pytesseract.image_to_string(thr)
    
    return text
