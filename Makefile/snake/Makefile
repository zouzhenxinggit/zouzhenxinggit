#snakey game

all:bean snake Calculation
	gcc -o all bean.o snake.o Calculation.o

.PHONY: bean snake Calculation	

bean:
	gcc -c bean.c 
snake:
	gcc -c snake.c
Calculation:
	gcc -c Calculation.c 

clean:
	rm all *.o 
