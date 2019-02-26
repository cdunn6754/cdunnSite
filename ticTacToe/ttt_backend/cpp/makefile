TTT_DIR = /home/clint/cpp/Projects/tic_tac_toe_cpp

MMDIR = $(TTT_DIR)/src/ttt_minimax
PDIR = $(TTT_DIR)/src/player
BDIR = $(TTT_DIR)/src/ttt_board
CFLAGS = -c -I$(MMDIR) -I$(PDIR) -I$(BDIR) -fPIC

MMLDIR = $(TTT_DIR)/build/src/ttt_minimax

libc_minimax_wrapper.so: c_minimax_wrapper.o
	g++ -L$(MMLDIR) -shared  \
	-Wl,-rpath,$(MMLDIR),-soname,libc_minimax_wrapper.so \
	-o libc_minimax_wrapper.so c_minimax_wrapper.o -lttt_minimax

c_minimax_wrapper.o: c_minimax_wrapper.cpp
	g++ $(CFLAGS) c_minimax_wrapper.cpp -o c_minimax_wrapper.o
	
