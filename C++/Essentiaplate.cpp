#include <iostream>
#include "essentia.h"

using namespace essentia::streaming;

int main(int argc, char* argv[]) {

  if (argc != 3) {
    std::cout << "ERROR: incorrect number of arguments." << std::endl;
    std::cout << "Usage: " << argv[0] << " audio_input yaml_output" << std::endl;
    exit(1);
  }

  std::string audioFilename = argv[1];
  std::string outputFilename = argv[2];

  // register the algorithms in the factory(ies)
  essentia::init();

  Pool pool;

  /////// PARAMS //////////////
  Real sampleRate = 44100.0;
  int frameSize = 2048;
  int hopSize = 1024;