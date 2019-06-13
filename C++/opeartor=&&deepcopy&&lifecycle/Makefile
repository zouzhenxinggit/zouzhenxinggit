#snakey game

.PHONY : clean

override OBJ = obj
override print ?= OK.....Succeed

obj-source := main.o deepcopy.o

$(OBJ) : $(obj-source)
	@echo building.......
	g++ -o $(OBJ) $^
	@echo $(print)

clean:
	-rm $(OBJ)
	-rm *.o
