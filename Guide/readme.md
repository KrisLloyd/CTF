##CTF Guide

Common CTF challenges, and how to approach them.

### ELF Files (PWN)

#### About

Executable and Linkable Format - A binary executable file built from c code.

An ELF binary is comprised of different sections, headers, sections, and segments.

![ELF File Structure](./ELF_Structure.PNG)

**Heasers** section contains metadata about the program and helps the process of execution.
**Sections** contain the **.text**, **.data** sections. These sections are where the code and variables are stored.

source code file:
```c
File: hello.c

#include <stdio.h>

int main() {
  printf("Hello world!");
  return 0;
}
```

Compile the file using **gcc**
```bash
root@localhost:~# gcc hello.c -o hello
```

run the binary
```bash
root@localhost:~# ./hello
Hello world!
```

#### Exploiting

1. Check for printable strings in the exectable:
  `strings ./hello`
2. Check a hex dump of the file:
  `xxd ./hello`
4. Use **readelf** to explore the file sections:
  `readelf <option flag> ./hello`
5. Read the MAN pages for any function to understand how it operates:
  `man execvp`
  
  
  
### Image Files (Stego)

Hidden messages in image files

1. If the image doesn't open, check the filetype and change extension if necessary
  `file image.png`
2. Load the image into [StegOnline](https://stegonline.georgeom.net/upload) and browse bit planes
3. Use the **strings** command to print any printable strings
  `strings image.png`
4. Check if there is anything hidden in the image EXIF metadata
  `exiftool image.png`
5. Load the imaage into the online EXIF tool [Jeffrey's Image Metadata Viewer](http://exif.regex.info/exif.cgi)
6. Check for embedded files with binwalk
  `binwalk -Me image.png`
7. Fix any corrupted chunks with pngcheck (-v verbose, -t7 text chunks, -p display other chunk content, -f force)
  `pngcheck -vt7pf image.png`