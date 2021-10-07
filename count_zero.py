from flask import Flask
import sys, json

app = Flask(__name__)

'''a function that counts numbers of zeros in a given array'''

def countZeros():
    '''Array A contains driver values'''
    A = ['0', '0', '0', '1', '2', '2']
    counts = A.count('0')
    return ({"number of zeros":counts})


'''same method not inside a function, counts numbers of zeros in a given array'''
A = ['0', '0', '9', '1', '2', '2']
count = A.count('0')
print(count)

if __name__ == "__main__":
    app.run(debug=True)
    # A = ['0','0','0','1','2','2']
