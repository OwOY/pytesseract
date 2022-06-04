<div align='center'>
    <img src='https://miro.medium.com/max/500/1*_2nsdmjpH6VsGp1imcJJqQ.png'/>
</div>
  
----
# How to use
1. Install Package
2. Download Engine
3. Use
---- 
### Install Package
```
python -m pip install pytesseract
```

### Download Engine
- [DownloadLink](https://github.com/UB-Mannheim/tesseract/wiki)

### Use
```
import pytesseract

pytesseract.pytesseract.tesseract_cmd = f'{Engine_Path}' # Set pytesseract engine
text = pytesseract.image_to_string(img, lang=None) # lang > can set language
print(text)
```
