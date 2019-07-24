#snakey game

.PHONY : clean

override SNAKE = snake
override print ?= OK.....Succeed

obj-source := snake.o bean.o frame.o key.o Calculation.o

$(SNAKE) : $(obj-source)
	@echo building.......
	gcc -o $(SNAKE) $^
	@echo $(print)

clean:
	-rm $(SNAKE)
	-rm *.o 
