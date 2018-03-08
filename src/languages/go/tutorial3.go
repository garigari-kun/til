package main

import (
  "fmt"
)

func add(x, y float32) float32 {
  return x + y
}

func multiple(a, b string) (string, string) {
  return a, b
}


func main() {

  fmt.Println(add(3.2, 4.2))
  fmt.Println(multiple("Keisuke", "Tsukamoto"))

}
