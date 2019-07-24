#c practive

obj-source ?= c.c
obj-source-c := cc
obj-source-o := *.o

.PHONY : cc clean

$(obj-source-c):
	@echo building......
	gcc -o $(obj-source-c) $(obj-source)

clean : 
	-rm $(obj-source-o) 
	-rm $(obj-source-c) 

