[< Back to All CTFs](https://github.com/KrisLloyd/Python/tree/master/CTF#ctf-solves)

[< Back to BIT Olympics CTF](https://github.com/KrisLloyd/Python/tree/master/CTF#bit-olymipcs-march-2021)
***

# Ex or me

### Challenge:
##### uvr}hb#hL+&Euo]Ea+*r$g
##### 100 Points


### Solve:

Being a crypto challenge, I knew what I was given was ciphertext and that it was just a matter of finding the correct method to decode. The clue was the title which pointed me to XOR.

Using CyberChef, I used XOR Brute Force first with with key length 1 with no useful results. Moving up to a key length of 2 greatly increased the returned results, however I knew what I was looking for, and searched the results for values that contained *flag*.


### Flag
```
flag{x0r_15_fuN_r19h7}
```
