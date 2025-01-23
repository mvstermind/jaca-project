#include "whisper.h"
#include <iostream>

int main() {
    // Initialize the Whisper context from a model file
    const char *model_path = "./whisper.cpp/models/ggml-base.en.bin"; // Replace with your actual model path
    struct whisper_context *ctx = whisper_init_from_file(model_path);

    if (!ctx) {
        std::cerr << "Failed to initialize Whisper context." << std::endl;
        return 1;
    }

    std::cout << "Whisper.cpp is successfully set up!" << std::endl;

    // Free the context when done
    whisper_free(ctx);

    return 0;
}

