# Makefile

obj-m := test.o

# export ARCH=arm

# export CROSS_COMPILE=arm-none-linux-gnueabi-

KERNEL_DIR := /usr/src/linux-headers-$(shell uname -r)
CURRENT_DIR := $(shell pwd)

all:
	make -C $(KERNEL_DIR) M=$(CURRENT_DIR) modules
clean:
	make -C $(KERNEL_DIR) M=$(CURRENT_DIR) clean
