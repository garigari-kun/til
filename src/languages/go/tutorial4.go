package main

import "fmt"


func main() {
  x := 15
  a := &x

  fmt.Println(x)
  fmt.Println(*a)

  *a = 5

  fmt.Println(x)
  fmt.Println(*a)
  

}
