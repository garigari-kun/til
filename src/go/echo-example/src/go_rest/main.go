package main

import (
  "fmt"
  "log"
  "net/http"
  "github.com/gorilla/mux"
  "go_rest/controllers/home"
  "go_rest/controllers/books"
)


func main() {
  fmt.Println("Start the local server...")
  router()
}

// Router
func router() {
  r := mux.NewRouter()

  r.HandleFunc("/", homeController.IndexController).Methods("GET")
  r.HandleFunc("/books", booksController.IndexController).Methods("GET")

  err := http.ListenAndServe(":8080", r)
  if err != nil {
    log.Fatal(err)
  }
}


// Controller
// func homeIndexController(w http.ResponseWriter, r *http.Request) {
//   fmt.Fprintf(w, "Index Page")
// }
