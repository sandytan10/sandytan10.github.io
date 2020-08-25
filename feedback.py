#!/usr/bin/python3

import cgi
import random

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="utf-8" >
            <title> DROPBOX </title>
        </head>
        <body>''')


def htmlTail():
    print ('''</body>
        </html>''')

def getData():
    form = cgi.FieldStorage()
    rating = form.getvalue("rating")
    help = form.getvalue("help")
    like = form.getvalue("like")
    print('<center><h2> Thank you for the feedback! </h2></center>')
    print('<h4>Copy of your answers: </h4>')
    print('<h3>On a scale of 1-3, what would you rate this website?</h3>')
    print('<h3>You selected: </h3>')
    print(rating)
    print('<h3>On a scale of 1-3, how helpful was this website?</h3>')
    print('<h3>You selected: </h3>')
    print(help)
    print('<h3>Did you like the website?</h3>')
    print('<h3>You selected: </h3>')
    print(like)

def main():
    htmlTop()
    print(''.format(getData()))
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
