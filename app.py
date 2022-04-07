from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
import datetime as dt
import math
import random

load_dotenv()

app = Flask(__name__)

now = dt.datetime.now()


@app.route('/')
def index():
    year = now.year
    return render_template('cipher-template.html', year=year)


@app.route('/encode')
def encode_form():
    year = now.year
    return render_template('encodeform-template.html', year=year)


@app.route('/encode', methods=['POST'])
def encode_process():
    coded_message = ""
    key = []
    key_print = ""
    split_message = ""
    global current_key
    year = now.year
    msg_to_encode = request.form['mtoencode']
    split_message = msg_to_encode.split()
    for word in split_message:
        for alphabet in word:
            def rand_key(alphabet):
                return random.randint(1, 9)
            current_key = rand_key(alphabet)
            key.append(current_key)
            coded_message += chr(ord(alphabet) + current_key)
        coded_message += " "
    print("Your coded message is: " + coded_message)
    print(key)
    for a in range(len(key)):
                key_print += str(key[a])
    print(key_print)
    # flash("Encoding Successful")
    return render_template('encodeform-template.html', year=year,
                           codedmsg=coded_message,
                           key_print=key_print)


@app.route('/decode')
def decode_form():
    year = now.year
    return render_template('decodeform-template.html', year=year)


@app.route('/decode', methods=['POST'])
def decode_process():
    decoded_message = ""
    split_message = ""
    i = 0
    year = now.year
    msg_to_decode = request.form['mtodecode']
    key_to_decode = request.form['keytodecode']
    split_message = msg_to_decode.split()
    for word in split_message:
        for alphabet in word:
            print(alphabet)
            decoded_message += chr(ord(alphabet)-int(key_to_decode[i]))
            print(decoded_message)
            i += 1
        decoded_message += " "
    print("Your message is: " + decoded_message)
    return render_template('decodeform-template.html', year=year,
                            decoded_message=decoded_message)

@app.route('/caesarencode')
def cencode_form():
    year=now.year
    return render_template('caesarcoding-template.html', year=year)

@app.route('/caesarencode', methods=['POST'])
def cencode_process():
    small_letters = list("abcdefghijklmnopqrstuvwxyz")
    capital_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    split_message = ""
    coded_message = ""
    year=now.year
    msg_to_cencode = request.form['mtocencode']
    key_to_cencode = int(request.form['keytocencode'])
    split_message= msg_to_cencode.split()
    for word in split_message:
        for alphabet in word:
            if alphabet.isalnum():
                if alphabet in small_letters:
                    if 25 - small_letters.index(alphabet) < key_to_cencode:
                        coded_message += small_letters[small_letters.index(alphabet)-(26-key_to_cencode)]
                    else:
                        coded_message += small_letters[small_letters.index(alphabet) + key_to_cencode]
                else:
                    if 25 - capital_letters.index(alphabet) < key_to_cencode:
                        coded_message += capital_letters[small_letters.index(alphabet) - (26 - key_to_cencode)]
                    else:
                        coded_message += capital_letters[capital_letters.index(alphabet) + key_to_cencode]
            else:
                coded_message += alphabet
        coded_message += " "
    print("Your coded message is: " + coded_message)
    return render_template('caesarcoding-template.html', year=year, 
                            cencodedmsg=coded_message)


# "magic code" -- boilerplate


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
