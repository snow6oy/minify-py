# minify.py

minify.py the simplest possible javascript minifier.

Unlike slimit, calmjs and others it does not really try to understand javascript (E5, E6 etc). All it tries to do is remove comments, spaces and new lines. There is no installer. To use it, copy it into your project directory and run at the command line. The default help output will be shown.
```
-d dirname      optional path to src (defaults to '.')
-t testrun      get a sample input/output
-h              this message
```
There is no outfile option. Easiest way is to just direct the output at runtime `./minify.py > example-min.js`. There are a couple of regular expressions, chained together. If minify.py causes errors in your Javascript you could try to comment one out. Thanks.
