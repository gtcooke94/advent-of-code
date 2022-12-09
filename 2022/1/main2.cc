#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <sstream>
#include <string>

void update_top_3(int* max_weights, int cur_weight) {
    for (int pos = 2; pos > 0; pos--) {
        if (cur_weight > *(max_weights + pos)) {
            if (pos == 2) {
                *(max_weights + pos) = cur_weight;
                break;
            } else if (pos == 1) {
                *(max_weights + pos + 1) = *(max_weights + pos);
                *(max_weights + pos) = cur_weight;
            } else {
                *(max_weights + pos + 2) = *(max_weights + pos + 1);
                *(max_weights + pos + 1) = *(max_weights + pos);
                *(max_weights + pos) = cur_weight;
            }
        }
    }
}

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
    int top_3_sums[3] = {0, 0, 0};
    int first_3_counter = 0;
    while (std::getline(input, line)) {
        std::istringstream iss(line);
        int weight;
        if (!(iss >> weight)) {
            std::cout << "[" << top_3_sums[0] << "," << top_3_sums[1] << "," << top_3_sums[2] << std::endl;
            if (first_3_counter < 3 ) {
                top_3_sums[first_3_counter] = weight;
                first_3_counter++;
            } else {
                update_top_3(top_3_sums, cur_sum);
            }
            std::sort(top_3_sums, top_3_sums + 3, std::greater<int>());
            cur_sum = 0;
            continue;
        }
        else {
            cur_sum += weight;
        }

    }

    int answer = std::accumulate(top_3_sums, top_3_sums + 3, 0);
    
    std::cout << "Answer is\n" << answer << std::endl;
}
