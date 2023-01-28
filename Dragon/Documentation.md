## Lexical Analysis

A program written in Dragon is read by Scanner.py. The code which is the input is divided into tokens for further use.
Below documentation shows how the scanner.py scans the file and divides into tokens based on keywords, identifier, 
number or string. 

#### Allowed Keywords:
    and      class     else     false     for     if
    nil      or        return   super     this    true
    var      while     let      in        int     bool
    float    mute      fun
                
#### Some common nuances:
    1. Not a token:
          Whitespace: ' '
          Raw string: '\r'
          Tab:        '\t'
    2. A token:
          Newline:    '\n'
          
                
