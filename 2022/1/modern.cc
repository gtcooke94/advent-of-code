
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>



uint64_t max_calories(const std::vector<std::string>& data) {
  auto by_elf = data |
      // group by elf: range{range{string}}
      std::views::lazy_split(std::string{}) | 
      // sum up the calories for each elf: range{uint64_t}	
      std::views::transform([](const auto& elf) -> uint64_t {
          // std::string -> uint64_t
          auto to_unsigned = 
            [](const auto& in) { return std::stoull(in); };
          // make a view of uint64_t: range{string} -> range{uint64_t}
          auto rng = elf | 
            std::views::transform(to_unsigned) | 
            std::views::common; // std::reduce requires a common range
          // reduce into the sum: range{uint64_t} -> uint64_t
          return std::reduce(rng.begin(), rng.end());
      });
  // find the elf with the maximum number of calories
  auto it = std::ranges::max_element(by_elf);
  return *it; // and return
}

uint64_t max_calories(const std::vector<std::string>& data) {
    auto by_elf = data |
        std::views::lazy_split(std::string{})
}

int parse_and_run(std::string path) {
    std::vector<std::string> data;
    std::ifstream file(path);
    if (!file.is_open()) {
        std::cerr << "Can't open file: " << path << std::endl;
        return 1;
    }
    std::string line;
    while (std::getline(file, line)) {
        data.push_back(line);
    }
    int answer1 = soln1(data);
    std::cout << answer1 << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cerr << "Need one parameter that is the input file.\n";
        return 1;
    }
    return parse_and_run(argv[1]);
}