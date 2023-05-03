# N-Crypt
### number based pure-python text encypting algorithm

N-crypt is a text encrypting algorithm whic is completely developed by me alone.
this algorithm itself have few uniqe fetures,

- It only use numbers for encryption process
- Every singel time your encrypted string will be random 

## Installation

N-Crypt requires python 3.8+ to run

Clone the repo or download it as a zip

```sh
git clone https://github.com/Danushka-Madushan/N-Crypt.git
cd N-Crypt
```

Now you have your encryption algorithm in N-Crypt folder
Now open encode.py with your favorite Code-Editor

## Encode
```python
encoded = encode("Python is Awesome", KeyList, NumList, Special)
print(encoded)
```

It will give you the encoded text string, which is something like this

```sh
3:2:04:1:07:307:403:20:4:1:0:511:91:1040:3:3021:10:2073:0:7:2021:0:630:511:3:4:21:3145:782:63:26:08:0:1:4:914:7
```

for you to note - Every Singele time you generate a encoded string it will be random but how many times you generate it, it can be decoded

## Decode

```python
decoded = decode("3:2:04:1:07:307:403:20:4:1:0:511:91:1040:3:3021:10:2073:0:7:2021:0:630:511:3:4:21:3145:782:63:26:08:0:1:4:914:7", KeyList, NumList, Special)
print(decoded)
```

It will give you the decoded text string :)

## Development

Want to Cusomize Great :)
when you open encode.py You can see three different list with data like this

```python
Special = [' ', '~`!@','$%^&','*()-','_+={','}[]|','\\/:;','"\'<>', ',.?#']
KeyList = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
NumList = ['01', '23', '45', '67', '89']
```
This is the text recognition date which uses to encrypt your text string you can
insert new characters but remember editing this lists may cause algorithm to
malfunction. the lenght of first two list must be 9 and last one must be 5


> Note: `this algorithm is currently only supports characters in US keyboard` 

## License

**Free Software, Hell Yeah!**

