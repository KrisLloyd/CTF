placeholder for guide.


### ELF Files

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
