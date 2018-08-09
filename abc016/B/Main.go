package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	isPlus := a+b == c
	isMinus := a-b == c
	if isPlus && isMinus {
		fmt.Println("?")
	} else if isPlus {
		fmt.Println("+")
	} else if isMinus {
		fmt.Println("-")
	} else {
		fmt.Println("!")
	}
}
