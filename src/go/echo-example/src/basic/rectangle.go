package main

import (
  "fmt"
)

type Rectangle struct {
  width, height float64
}

// Just normal function
func area(r Rectangle) float64 {
  return r.width * r.height
}

// This is a method!
// Rob pike said,,"A method is a function with an implicit first argument, called a receiver."
func (r *Rectangle) Area() float64 {
  return r.width * r.height
}

func main() {
  r1 := Rectangle{width: 5, height: 5}
  fmt.Println(area(r1))
  fmt.Println(r1.Area())
}
