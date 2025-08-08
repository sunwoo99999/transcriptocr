import pytesseract
from PIL import Image

# 1) Tesseract 실행 파일의 경로를 지정합니다.
#    만약 Tesseract를 기본 경로(C:/Program Files/Tesseract-OCR)에 설치했다면:
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/sunwo/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

# 2) 이미지를 불러옵니다.
image = Image.open('sample.png')

# 3) OCR 수행
text = pytesseract.image_to_string(image, lang='eng')  # lang='eng'는 영어로 인식

# 4) 결과 출력
print("인식된 텍스트:")
print(text)
