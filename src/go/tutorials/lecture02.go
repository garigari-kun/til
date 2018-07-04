package main

import (
  "fmt"
  "reflect"
  )

// func add(x float64, y float64) float64 {
//   return x + y
// }

// func add(x, y float64) float64 {
//   return x + y
// }

func add(x, y float64) float64 {
  return x + y
}

func concat(x, y string) (string, string) {
  return x, y
}

func main() {
  // var num1 float64 = 6.4
  // var num2 float64 = 5.9

  // var num1, num2 float64 = 6.4, 5.9

  num1, num2 := 6.4, 5.9

  fmt.Println(add(num1, num2))

  w1, w2 := "Hey", "there"

  fmt.Println(concat(w1, w2))

  a := 3.4
  b := 1234567788
  fmt.Println(reflect.TypeOf(a))
  fmt.Println(reflect.TypeOf(b))

}
