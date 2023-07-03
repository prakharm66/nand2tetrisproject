// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

//repeated addition

//i=r0
@R0
D=M
@i
M=D

//sum=0
@sum
M=0

// loop
(LOOP)
@i
D=M
// if i<0 jmp done
@DONE
D;JLE

// i=i-1
@i
M=M-1

// sum=sum+r1
@R1
D=M
@sum
M=M+D

@LOOP
0;JMP

(DONE)
//r2= sum
@sum
D=M
@R2
M=D


(END)
@END
0;JMP


