package main

import (
  "fmt"
)

func add(x, y int) int {
  return x + y
}

func swap(x, y string) (string, string) {
  return y, x
}

// named return var
func add_one(variable int) (x int) {
  x = variable + 1
  return
}

func main() {
  fmt.Println(add(4, 8))
  fmt.Println(swap("world", "hello"))
  fmt.Println(add_one(1))
}
