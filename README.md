You will have to implement the computation of the sp values from the KMP algorithm. You will receive a string of DNA letters in FASTA format (more below) and you will have to provide as an output a list of numbers corresponding to the sp[i] values for that string. 

As an example, for the input:

\> Sequence 1 

CAGCATGGTATCACAGCAGAG 

The corresponding output is:

0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
You can assume that your code will find a file named "input" in the local directory, and that this file will contain a DNA string in FASTA format.  The FASTA format has a series of blocks (in this case you can expect a single one) that are prefixed by a single line starting with a '>' sign followed by some identifier for the sequence. The subsequent lines contain the actual DNA sequence.

Your code will have to create a file called "output", again in the local directory, that will contain a string of numbers representing the sp values.  The number of values has to match the number of letters in the DNA sequence (a quick check you can add into your code to catch bugs).

The assignment is available in Gradescope: https://www.gradescope.com/courses/358896/assignments/1797803 .

It is equivalent to the Rosalind exercise KMP: https://rosalind.info/problems/kmp/ .
