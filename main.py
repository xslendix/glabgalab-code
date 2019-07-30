#!/usr/bin/python3

debug = True

#import basic
from language import run
import sys
import os.path
import readline
import optparse

parser = optparse.OptionParser()

parser.add_option('-f', '--file',
                action='store', dest='filename',
                help='File name', default=None
                )

options, args = parser.parse_args()

if options.filename != None:
    if os.path.isfile(options.filename):
        with open(options.filename) as f:
            result, error = run.run(options.filename, f.read())
            if error:
                print(error.as_string())
            elif result:
                print(result)
else:
    motd = (
    'Glabgalab interpreter 0.0.1\n'
    '---------------------------')
    
    print(motd)

    while True:
        try:
            text = input('>>> ')

            if text.strip() == '': continue            

            if text != 'exit':
                #result, error = basic.run('<stdin>', text)
                result, error = run.run('<stdin>', text)
                if error:
                    print(error.as_string())
                elif result:
                    if len(result.elements) == 1:
                       print(repr(result.elements[0]))
                    else:
                        print(repr(result))
            else: break
        except:
            if debug == False: print('\nIf you try to exit, use the `exit` command god dammit')
            else:
                print('')
                raise
