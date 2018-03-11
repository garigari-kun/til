package main

import "fmt"


type Vertex struct {
  X int
  Y int
}


func main() {
  vertex := Vertex{1, 2}
  p_vertex := &vertex
  fmt.Println(vertex)
  p_vertex.X = 100000
  fmt.Println(vertex)
}
