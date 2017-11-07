PROG = lib
CC = g++
CPPFLAGS = -g -Wall 
OBJS = lib.so

#$(PROG) : $(OBJS)
#	$(CC) -o $(PROG) $(OBJS)

all:	
	g++ -Wall -fPIC -O3 -shared lib.cpp -o lib.so

clean:
	rm -f core $(PROG) $(OBJS)
