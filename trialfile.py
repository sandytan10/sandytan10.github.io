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
    first = form.getvalue("fname")
    last = form.getvalue("lname")
    Comment = form.getvalue("Comments")
    print('<h2> Thanks for leaving a comment! </h2>')
    print(first, last, '<p> commeted: </p>')
    print(Comment)
        
 

def main():
    htmlTop()
    print(''.format(getData()))
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
