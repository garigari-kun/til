package main

import (
  "fmt"
  "time"
)

func main() {
  go count("nohenohe")
  count("hoge")
}

func count(target string) {
  for index, _ := range(target) {
    fmt.Printf("%d: %s\n", index, target)
    time.Sleep(time.Millisecond * 500)
  }
}
