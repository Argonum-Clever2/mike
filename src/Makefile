# 编译器版本 c++11
CPP_FLAGS = "-std=gnu++11"
PREFIX=../bin

#mike : combine.o command.o commandhash.o commandlist.o commandsimilarity.o threadhash.o similarity.o mike.o
#cc = g++

mike: libcommand.a
		g++ ${CPP_FLAGS} mike.cpp libcommand.a -lpthread -o mike

#mike.o: mike.cpp
#		g++ ${CPP_FLAGS} mike.cpp -c -o mike.o

libcommand.a: combine.o command.o commandhash.o commandlist.o commandsimilarity.o commanddist.o threadhash.o similarity.o dist.o
		ar -r libcommand.a combine.o command.o commandhash.o commandlist.o commandsimilarity.o commanddist.o threadhash.o similarity.o dist.o

combine.o: combine.cpp combine.h
		g++ -Wl,--no-as-needed ${CPP_FLAGS} combine.cpp -c -o combine.o

threadhash.o: threadhash.cpp threadhash.h
		g++  -Wl,--no-as-needed ${CPP_FLAGS} threadhash.cpp -c -o threadhash.o

similarity.o: similarity.cpp similarity.h
		g++  -Wl,--no-as-needed ${CPP_FLAGS} similarity.cpp -c -o similarity.o

dist.o: dist.cpp dist.h
		g++  -Wl,--no-as-needed ${CPP_FLAGS} dist.cpp -c -o dist.o

command.o: command.cpp command.h
		g++ -Wl,--no-as-needed ${CPP_FLAGS} command.cpp -c -o command.o

commandhash.o: commandhash.cpp commandhash.h
		g++ -Wl,--no-as-needed ${CPP_FLAGS} commandhash.cpp -c -o commandhash.o

commandlist.o: commandlist.cpp commandlist.h
		g++ -Wl,--no-as-needed ${CPP_FLAGS} commandlist.cpp -c -o commandlist.o

commandsimilarity.o: commandsimilarity.cpp commandsimilarity.h
		g++ -Wl,--no-as-needed ${CPP_FLAGS} commandsimilarity.cpp -c -o commandsimilarity.o

commanddist.o: commanddist.cpp commanddist.h
		g++ -Wl,--no-as-needed ${CPP_FLAGS} commanddist.cpp -c -o commanddist.o

install: mike
		mkdir -p ${PREFIX}
		cp mike ${PREFIX}
clean:
	rm *.o *.a
