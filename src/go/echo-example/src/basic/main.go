package main

import (
  "fmt"
)

func main() {
  fmt.Println("main is running")

  i := 5
  n := 10
  passByPointer(&i)

  passByValue(n)
}

func passByPointer(i *int) {
  fmt.Println(*i)
}

func passByValue(i int) {
  fmt.Println(i)
}
