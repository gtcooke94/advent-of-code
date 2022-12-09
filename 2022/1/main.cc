#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

// Using main function from https://github.com/HappyCerberus/moderncpp-aoc-2021
int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Need one parameter that is the input file.\n";
        return 1;
    }
    std::ifstream input(argv[1]);
    if (!input.is_open()) {
        std::cerr << "Can't open file: " << argv[1] << std::endl;
        return 1;
    }

    std::string line;
    int cur_sum = 0;
    int max_weight = 0;
    while (std::getline(input, line)) {
        std::istringstream iss(line);
        int weight;
        if (!(iss >> weight)) {
            if (cur_sum > max_weight) {
                max_weight = cur_sum;
            }
            cur_sum = 0;
            continue;
        }
        else {
            cur_sum += weight;
        }

    }

    int answer = max_weight;
    
    std::cout << "Answer is\n" << answer << std::endl;
}
