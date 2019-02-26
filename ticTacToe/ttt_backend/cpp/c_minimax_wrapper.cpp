#include "ttt_minimax.h"

extern "C" {
  int minimax(char (&array)[9], const char agent) {
    return ttt_minimax(array, agent);
  }
}
