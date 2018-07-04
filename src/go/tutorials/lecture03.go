package main

import "fmt"

func passByValue(a *int) {
  fmt.Println(a)
  fmt.Println(*a)
  *a = 5
}

func main() {
  x := 15

  a := &x

  fmt.Println(x)
  fmt.Println(a)
  fmt.Println(*a)

  exp := 100
  passByValue(&exp)


}
