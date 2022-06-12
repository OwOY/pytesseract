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
- Windows
[DownloadLink](https://github.com/UB-Mannheim/tesseract/wiki)
- CentOS
```
cd /etc/yum.repos.d/
wget https://download.opensuse.org/repositories/home:Alexander_Pozdnyakov:tesseract5/CentOS_8/home:Alexander_Pozdnyakov:tesseract5.repo
yum install tesseract
```

### Use
```
import pytesseract

pytesseract.pytesseract.tesseract_cmd = f'{Engine_Path}' # Set pytesseract engine
text = pytesseract.image_to_string(img, lang=None) # lang > can set language
print(text)
```
