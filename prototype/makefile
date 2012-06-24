# Makefile for Alexander Brown's Dissertation Prototyping.
# 
# Version 0.1

# Variable Definitions
SRC=src
BIN=bin
EXE=prototype

CC=gcc
CFLAGS=-Wall

# Build all modules
all: mkdirs compile_all

# Make ay directorys which need to exist.
mkdirs:
	test -d ${BIN} || mkdir ${BIN}

compile_all: visualisation

visualisation:
	echo "Halp!"
	

# Remove the binaries directory
clean:
	rm -rf ${BIN}/*
	test ! -f EXE || rm EXE
