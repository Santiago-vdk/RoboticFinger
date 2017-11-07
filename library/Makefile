PROG = lib
CC = g++
CPPFLAGS = -g -Wall 
OBJS = lib.o

$(PROG) : $(OBJS)
	$(CC) -o $(PROG) $(OBJS)

all:	
	g++ -Wall  -c -o lib.o lib.cpp

clean:
	rm -f core $(PROG) $(OBJS)
