# Lossless String Compression
Simple algorithm for compressing strings via a remote machine using curl commands.

# Dependencies
You'll need Python >=3.6 on your machine and the Flask module for Python.
Python installers are found here: https://www.python.org/
After installing python, run the following in command line:
```
pip install flask
```

# Files
- lsc.py: The main script
- words.txt: Contains 3000 English words
- words_mini.txt: Contains a small sample of words.txt
- words_comp.txt: Contains the 3000 English words compressed
- words_comp_mini.txt: Contains a small sample of words_comp.txt

# Usage
lsc.py expects a curl **POST** with a **.txt** file named **"words"** via **port 80**. The words in .txt file need to be separated with either spaces or newlines.

Use HOST:PORT/compress to compress the contents of a .txt file

Use HOST:PORT/decompress to decompress the contents of a .txt file

# Example
To test the script locally, cd to repositry in command line and run the lsc.py script:
```
python lsc.py
```

Then open up another command line and run the following:
```
curl -X POST -F "words=@C:\path\lsc\words_mini.txt" http://127.0.0.1:80/compress
```
Replace with the correct path and host if necessary 
