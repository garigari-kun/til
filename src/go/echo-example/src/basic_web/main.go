package main

import (
  "fmt"
  "net/http"
  "github.com/gorilla/mux"
  "html/template"
)

var templates *template.Template

func main() {
  fmt.Println("Start a local server...")
  loadTemplates()
  router()
}

// View Loader
func loadTemplates() {
  templates = template.Must(template.ParseGlob("templates/*.html"))
}

// Router
func router() {
  r := mux.NewRouter()

  // static files
  fs := http.FileServer(http.Dir("./static/"))
  r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", fs))


  r.HandleFunc("/", indexController).Methods("GET")
  r.HandleFunc("/", indexCreateController).Methods("POST")
  r.HandleFunc("/welcome", welcomeController).Methods("GET")
  http.Handle("/", r)
  http.ListenAndServe(":8080", nil)
}

// Controller
func indexController(w http.ResponseWriter, r *http.Request) {
  templates.ExecuteTemplate(w, "index.html", nil)
}

func indexCreateController(w http.ResponseWriter, r *http.Request) {
  r.ParseForm()
  comment := r.PostForm.Get("comment")
  fmt.Printf("%s will be saved", comment)
  http.Redirect(w, r, "/", 302)
}

func welcomeController(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "This is a welcome page")
}
