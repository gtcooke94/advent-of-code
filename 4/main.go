// Solution in Go inspired after reading some solutions on the reddit solutions thread
// https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/
package main

import (
	"fmt"
	"strconv"
)

func main() {
	num1 := 245318
	// num2 := 245320
	num2 := 765747
	part1Counter := 0
	part2Counter := 0
	for num := num1; num <= num2; num++ {
		str := strconv.Itoa(num)
		digits := make([]int, 6)
		for i, digit := range str {
			d, err := strconv.Atoi(string(digit))
			if err != nil {
				panic(err)
			}
			digits[i] = d
		}
		differences := make([]int, 5)
		for i := 0; i < 5; i++ {
			differences[i] = digits[i+1] - digits[i]
		}

		// Part 1
		containsDouble := false
		nonNegative := true
		for i := 0; i < len(differences); i++ {
			if differences[i] < 0 {
				nonNegative = false
				break
			}
			if differences[i] == 0 {
				containsDouble = true
			}
		}
		if containsDouble && nonNegative {
			part1Counter++
		}

		// Part 2
		nonNegative = true
		containsDouble = false
		for i := 0; i < len(differences); i++ {
			if differences[i] < 0 {
				nonNegative = false
				break
			}
			if !containsDouble {
				if differences[i] == 0 {
					if i == 0 {
						containsDouble = differences[i+1] != 0
					} else if i == len(differences)-1 {
						containsDouble = differences[i-1] != 0
					} else {
						containsDouble = differences[i-1] != 0 && differences[i+1] != 0
					}
				}
			}
		}
		if containsDouble && nonNegative {
			part2Counter++
		}
	}
	fmt.Println(part1Counter, part2Counter)
}
