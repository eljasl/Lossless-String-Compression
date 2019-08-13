from flask import Flask, request

def compress_item(curr, prev):
    '''
    Returns the current word compressed by the previous word.
    curr: Current word
    prev: Previous word
    '''
    for i, letter in enumerate(curr):
        if i >= min(len(curr),len(prev)): break
        if letter != prev[i]: break
    return f'{i} {curr[i:]}'

def compress_loop(strList):
    '''
    Loops through a list of words and applies the compressor to each pair.
    Returns a list of compressed words.
    strList: Words as a list of strings
    '''
    compressedList = []
    previous = '' 
    for current in strList:
        compressedList.append(compress_item(current, previous))
        previous = current
    return compressedList

def decompress_item(curr, prev):
    '''
    Returns the current word decompressed by the previous word.
    curr: Current word
    prev: Previous word
    '''
    delta, suffix = curr.split(' ')
    prefix = prev[:int(delta)]
    return f'{prefix}{suffix}'

def decompress_loop(compressedList):
    '''
    Loops through a list of encoded words and applies the decoder to each pair.
    Returns a list of decoded words.
    encodedList: Encoded words as a list of strings
    '''
    decompressedList = []
    previous = ''
    for current in compressedList:
        current = decompress_item(current, previous)
        decompressedList.append(current)
        previous = current
    return decompressedList

app = Flask(__name__)

@app.route('/compress', methods=['GET','POST'])
def compress():
    '''
    Webapp to apply lossless string compression to a text file.
    Requires a curl POST with a .txt file named \"words\" where
    words are separated with a newline or a space.
    Returns a string of compressed words separated with a newline.
    '''
    if request.method == 'POST':
        if 'words' in request.files:
            file = request.files['words']
        else:
            return 'No file \"words\" found in request'
        requestString = file.read().decode('utf-8')
        wordList = requestString.replace(' ', '\n').strip().split('\n')
        compressedList = compress_loop(wordList)
        return '\n'.join(compressedList)
    else:
        return f'Only POST method is supported. Received {request.method}'

@app.route('/decompress', methods=['GET','POST'])
def decompress():
    '''
    Webapp to reverse lossless string compression for a text file.
    Requires a curl POST with a .txt file named \"words\" where
    compressed words are separated with a newline.
    Returns a string of decompressed words separated with newline.
    '''
    if request.method == 'POST':
        if 'words' not in request.files: 
            return 'No file \"words\" found in request'
        file = request.files['words']
        requestString = file.read().decode('utf-8')
        wordList = requestString.split('\n')
        decompressedList = decompress_loop(wordList)
        return '\n'.join(decompressedList)
    else:
        return 'Only POST method is supported.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
