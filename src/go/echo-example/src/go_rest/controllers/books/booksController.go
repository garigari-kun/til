package booksController

import (
  "net/http"
  "encoding/json"
  "go_rest/models/books"
)


func IndexController(w http.ResponseWriter, r *http.Request) {
  var books []Book
  books = append(books, Book{ID: "1", Isbn: "438227", Title: "Book One", Author: &Author{Firstname: "John", Lastname: "Doe"}})
  books = append(books, Book{ID: "2", Isbn: "454555", Title: "Book Two", Author: &Author{Firstname: "Steve", Lastname: "Smith"}})
  w.Header().Set("Content-type", "application/json")
  json.NewEncoder(w).Encode(books)
}
