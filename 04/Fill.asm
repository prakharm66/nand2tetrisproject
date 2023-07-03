// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//loop start
(loopStart)

@KBD
D=M
@displaywhite
D;JEQ//JUMP if equal to 0

//display black

@8192 //nuber of loop iterations
D=A
@i
M=D

(innerloop)
@i
D=M
@i
M=M-1
@SCREEN
A=A+D
M=-1

@i
D=M
@innerloop
D;JGE

//loop end
@loopStart
0;JMP

//display white
(displaywhite)
@8192
D=A
@i
M=D

(innerloopblack)
@i
D=M
@i
M=M-1
@SCREEN
A=A+D
M=0

@i
D=M
@innerloopblack
D;JGE

@loopStart
0;JMP