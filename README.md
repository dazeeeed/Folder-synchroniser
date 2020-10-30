Simple GUI program for folder synchronization.

=--------------------------------------------=
Updates selected folder with another, but the main goal of this script is to update it with NEWER files.

--Example--
-> /Documents/presentation.pptx created and added few slides to it on PC1
-> moving it to external HDD /mnt/d
-> copying from HDD /mnt/d to PC2 /MyFiles/
-> working on file from PC2
-> copying from PC2 /MyFiles/presentation.pptx to HDD /mnt/d
-> working on example file in /Documents/ExampleFile.txt on PC1
-> HERE COMES THE PROBLEM - moving /Documents/ from PC1 to HDD /mnt/d overwrites presentation.pptx with older file
-> SOLUTION - python-synchroniser.py
