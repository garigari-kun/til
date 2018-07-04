package main

import ("fmt"
        "net/http")

func index_handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "Index view")
  fmt.Fprintf(r)
  fmt.Fprintf(w)
}


func main() {
  http.HandleFunc("/", index_handler())
  http.ListenAndServe(":8000", nil)
}
