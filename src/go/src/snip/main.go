package main

import (
  "fmt"
)

func main() {
  type Person struct {
    name string
    age int
  }

  person1 := Person{name: "Keisuke", age: 26}
  fmt.Println(person1)
  fmt.Println(person1.name)

  person2 := &Person{name: "Negan", age: 50}
  fmt.Println(person2)

  person3 := &person1
  person3.name = "hogehoge"
  fmt.Println(*person3)
}
