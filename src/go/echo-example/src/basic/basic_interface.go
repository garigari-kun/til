package main

import (
  "fmt"
)

type Human struct {
  name string
  age int
  phone string
}

type Student struct {
  Human
  school string
  loan float32
}

type JustSayHi interface {
  SayHi()
}

func (h Human) SayHi() {
  fmt.Printf("Hi, I am %s. You can call me at %s\n", h.name, h.phone)
}

func (s *Student) BorrowMoney(amount float32) {
  s.loan += amount
}

func (s *Student) Loan() float32 {
  return s.loan
}

func main() {
  student1 := Student{Human{"Keisuke", 25, "123456"}, "De anza college", 32000}
  student1.SayHi()
  fmt.Println(student1.Loan())
  student1.BorrowMoney(1000)
  fmt.Println(student1.Loan())

  var machine JustSayHi
  machine = student1
  machine.SayHi()
  // can not call it!
  // machine.BorrowMoney(50000)
}
