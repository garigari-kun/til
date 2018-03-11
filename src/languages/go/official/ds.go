package main

import "fmt"

func main() {

  var a [2]string

  a[0] = "Keisuke"
  a[1] = "Tsukamoto"
  fmt.Println(a)

  city := [5]string{"Kawagoe", "Niigata", "Shibata"}

  fmt.Println(city)

  var slice_city []string = city[1:2]

  fmt.Println(slice_city)




}
