#!/usr/bin/env python3
'''
minify.py the simplest possible js minifier
'''
import re
import getopt
import sys
import fnmatch
import os

class Minify:
  '''
  '''
  def reduce(self, src):
    '''
    strip lines and comments
    '''
    rebang = re.compile('\/\*.+?\*\/')   
    reoneline = re.compile('[^:]\/\/.+')

    ps0 = re.sub(reoneline, ' ', src)
    ps1 = re.sub('\s+',     ' ', ps0)
    ps2 = re.sub(rebang,    ' ', ps1)
    return ps2

  def process(self, dirname=None):
    '''
    gather the src files
    '''
    minified = str()
    basedir = dirname if dirname else '.'

    for filename in os.listdir(basedir):
      if fnmatch.fnmatch(filename, '*.js'):
        jsfile = "{d}/{fn}".format(d=basedir, fn=filename)
        with open(jsfile, "r") as f:
          programSrc = f.read()
          minified = minified + self.reduce(programSrc)
    return minified

def usage():
  message = '''
-d dirname      optional path to src (defaults to '.')
-t testrun      get a sample input/output
-h	        this message
'''
  print(message)

def main():
  '''
  get inputs from command line
  '''
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:t", ["help", "dirname="])
  except getopt.GetoptError as err:
    print(err)  # will print something like "option -a not recognized"
    usage()
    sys.exit(2)
  dirname = None
  testrun = False
  for o, arg in opts:
    if o == "-t":
      testrun = True
    elif o in ("-d", "--dirname"):
      dirname = arg
    elif o in ("-h", "--help"):
      usage()
      sys.exit()
    else:
      assert False, "unhandled option"
  return (testrun, dirname)

if __name__ == '__main__':
  testFile = '''
/*  demonstrate
    how awesome
    minify.py is */

var url = 'http://example.com'; // avoid a double slash
var hash = window.location.hash.substr(1);
console.log(hash);  // this is another one line comment
     me.innerHTML = hash;
/* this a one line bang comment */
'''
  (testrun, dirname) = main()

  if (testrun):
    minify = Minify()
    print(testFile)
    print("")
    print(minify.reduce(testFile))
  elif (dirname):
    minify = Minify()
    print(minify.process(dirname))
  else:
    usage()
