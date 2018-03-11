package main

import "fmt"

func main() {
  i := 4

  pointer := &i
  fmt.Println(pointer)
  fmt.Println(*pointer)

  *pointer = 1
  fmt.Println(i)
  fmt.Println(*pointer)

}
