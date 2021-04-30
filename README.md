Paper: [Frequent Sequence Mining approach to Video Compression](https://link.springer.com/chapter/10.1007/978-981-13-0716-4_8#:~:text=This%20work%20provides%20an%20approach,sequence%20mining%20in%20video%20compression.&text=Redundant%20information%20and%20repeating%20sequences,data%20mining%20and%20coding%20techniques.)

# Instructions

The process in short : 

1) Convert the 3D matrix into a 2D matrix for all the 3 components(Red ,Green, Blue)
2) Seperate them into blocks of predefined size.
3) Mine the frequent patterns for each block.
4) Replace the frequent patterns with the code for each block.
5) Combine the replaced blocks into a single file.

Description of the process done by each script : 

main.py
-------
1) Converts the 3D data structure of the video into a 2D format and then divide them into a blocks of predefined size.
2) Converts and stores these block to the format that could be used for mining(SPMF).

Mining frequnt patterns 
-----------------------
1) Mining is done using the tool SPMF(http://www.philippe-fournier-viger.com/spmf/index.php?link=download.php)
2) main.py converts the video into .txt file with the specified format required to mine using SPMF.
3) Frequent sequences are mined from each block and are stored in a seperate files by SPMF.

rep.py
------
1) This takes as input each block and it's corresponding frequent seqences and then replaces it with a code.
2) This is done for each block an the location of each replacement and the sequence associated with it is stored in a dictionary .

combine.py
----------
1) After replacement all the blocks are combined for all the thress components with a padding to identify the sepertion.
2) Then the three components are combined into a single file that is the compressed file.
3) The dictionary is stored as a seperate file.


IMPORTANT NOTE:
---------------
Please read the paper to fully understand the process.
Running the program might take up a lot of space to store the intermediate files.
