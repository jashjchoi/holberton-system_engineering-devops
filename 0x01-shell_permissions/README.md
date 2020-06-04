### 0x01. Shell, Permissions
---


1. Symbolic Mode
------

```$ chmod [references][operator][modes] file ...```

##### Reference

Reference | Class | Description
------------ | -------------
u | user | File owner
g | group | Other users in the file's group
o | others | Other users not in the file's group
a | all | all three of the above, same as `ugo`

##### Operator

Operator | Description
------------ | -------------
+ | Adds the specified modes to the specified classes
- | Removes the specified modes from the specified classes
= | The modes specified are to be made the exact modes for the specified classes

##### Mode

Mode | Permission | Description
------------ | -------------
r | Read | Read a file or list a directory's contents
w | Write | write to a file or directory
x | Execute | Execute or recurse a directory tree


2. Numerical permissions

# | Permission | rwx | Binary
------------ | -------------
7 | Read, write and execute | rwx | 111
6 | Read and write | rw- | 110
5 | Read nad execute | r-x | 101
4 | Read only | r-- | 100
3 | Write and execute | -wx | 011
2 | Write only | -w- | 010 
1 | Execute only | --x | 001
0 | None | --- | 000

- For example, `754` would allow:

  -"read" (4), "write" (2), and "execute" (1) for the user class, as the binary value of 7 (4+2+1) is 111.
  -"read" (4) and "execute" (1) for the Group class, as the binary value of 5 (4+1) is 101.
Only "read" (4) for the Others class, as the binary value of 4 (4) is 100.

