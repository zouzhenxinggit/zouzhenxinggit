#snakey game

all:bean snake Calculation frame
	gcc -o all bean.o snake.o Calculation.o \
		frame.o

.PHONY: bean snake Calculation frame

bean:
	gcc -c bean.c 
snake:
	gcc -c snake.c
Calculation:
	gcc -c Calculation.c 
frame:
	gcc -c frame.c
clean:
	rm all *.o 
