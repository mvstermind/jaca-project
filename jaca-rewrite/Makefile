CXX = g++
CXXFLAGS = -Iwhisper.cpp/include -Iwhisper.cpp/ggml/include -std=c++17
LDFLAGS = -Lwhisper.cpp/build/src -lwhisper -lm
SRC = main.cpp
OBJ = $(SRC:.cpp=.o)
EXEC = main

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CXX) -o $(EXEC) $(OBJ) $(LDFLAGS)

%.o: %.cpp
	$(CXX) -c $< -o $@ $(CXXFLAGS)

clean:
	rm -f $(OBJ) $(EXEC)

rebuild: clean all

.PHONY: all clean rebuild

