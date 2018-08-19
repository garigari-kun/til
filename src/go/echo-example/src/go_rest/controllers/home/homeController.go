package homeController

import (
  "fmt"
  "net/http"
)

func IndexController(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "Index Page from package")
}
