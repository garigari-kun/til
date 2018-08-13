package main


import (
  "fmt"
)

func main() {
  // fmt.Println("It is gonna be panicked soon..")
  // panic("PANICKED!!!!!!")

  person1 := person{ first_name: "Keisuke", last_name: "Tsukamoto" }
  fmt.Println(person1.getFirstName())
  person1.speak()

  person2 := person{ first_name: "Go", last_name: "Pher" }
  person2.speak()

  foo(person1)
}

type error interface {
  Error() string
}

type ErrZeroDivision struct {
  message string
}

type human interface {
  speak()
  // walk()

}

func foo(h human) {
  fmt.Println(h)
}

type person struct {
  first_name string
  last_name string
}

func(p person)getFirstName() string {
  return p.first_name
}

func(p person)speak() {
  fmt.Println("what is up? i am ", p.getFirstName())
}
