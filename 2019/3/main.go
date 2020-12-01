// Solution in Go inspired after reading some solutions on the reddit solutions thread
// https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getLines() []string {
	scanner := bufio.NewScanner(os.Stdin)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func main() {
	// fmt.Println(reader.ReadString('\n'))
	// fmt.Println(reader.ReadString('\n'))
	// fmt.Println(reader.ReadString('\n'))
	lines := getLines()
	// fmt.Println(lines)
	splitLines := make([][]string, len(lines))
	for i, line := range lines {
		splitLine := strings.Split(line, ",")
		splitLines[i] = splitLine
	}

	// ================================================================================

	curPoint := complex64(complex(0, 0))
	for _, instruction := range splitLines[0] {
		dir := instruction[0]
		dis, _ := strconv.Atoi(instruction[1:])
		curPoint = updateGrid(dir, dis, gridOne, curPoint)
	}
	curPoint = complex64(complex(0, 0))
	for _, instruction := range splitLines[1] {
		dir := instruction[0]
		dis, _ := strconv.Atoi(instruction[1:])
		curPoint = updateGrid(dir, dis, gridTwo, curPoint)
	}
	var intersections []complex64
	for key := range *gridOne {
		if _, ok := (*gridTwo)[key]; ok {
			intersections = append(intersections, key)
		}
	}
	minManhatten := 10000000
	minP2 := 10000000
	for _, val := range intersections {
		r := abs(int(real(val)))
		c := abs(int(imag(val)))
		curManDist := r + c
		if curManDist == 0 {
			continue
		}
		if curManDist < minManhatten {
			minManhatten = curManDist
		}
		g1 := (*gridOne)[val]
		g2 := (*gridTwo)[val]
		curP2 := g1 + g2
		if curP2 < minP2 {
			minP2 = curP2
		}
	}
	fmt.Printf("Part 1: %v\n", minManhatten)
	fmt.Printf("Part 2: %v\n", minP2)
}

var directions = map[byte]complex64{
	'U': complex(1, 0),
	'D': complex(-1, 0),
	'L': complex(0, -1),
	'R': complex(0, 1),
}

var gridOne = &map[complex64]int{complex(0, 0): 0}
var gridTwo = &map[complex64]int{complex(0, 0): 0}

func updateGrid(dir byte, dis int, grid *map[complex64]int, curPoint complex64) complex64 {
	// fmt.Println(dir, dis)
	// fmt.Println(directions[dir])
	for i := 0; i < dis; i++ {
		curVal := (*grid)[curPoint]
		curVal++
		curPoint += directions[dir]
		(*grid)[curPoint] = curVal
	}
	return curPoint
}

func abs(a int) int {
	if a < 0 {
		a = -a
	}
	return a
}
