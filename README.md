# My Songbook
Directory where I save txt files with chords and lyrics, a script to build a body, and one to compile my songbook.

## Requirements

Python <br>
PdfLatex

## Folder organization

```
Autor1
    Song1
    Song2
    Song3
Autor2
    Song1
    Song2
    Song3
Autor3
    Song1
    Song2
    Song3
```

Songs will appear in the songbook grouped by autor and in alphabetic order. Autors will appear in alphabetic order, too. 

## Compile the songbook

Run (double click)
```
run.bat
```

## How to contribute

Contributors are welcome to add songs at their wish. Please follow the structure Author/Song-Title.txt (where spaces are replaced by "-" and capital letters are used. Note that sometimes accents in the title are not welcome by the latex compiler, so I prefer to use '). Inside the txt files write only text and chords (without title, which is automatically added by the "body builder").