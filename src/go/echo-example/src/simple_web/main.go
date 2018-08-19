package main

import (
	"fmt"
	"net/http"
	"strings"
	"log"
)

func sayhelloName(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()  // parse arguments, you have to call this by yourself
	fmt.Println(r.Form)  // print form information in server side
	fmt.Println("path", r.URL.Path)
	fmt.Println("scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k, v := range r.Form {
    	fmt.Println("key:", k)
    	fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprintf(w, "Hello astaxie!") // send data to client side
}

func hey(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "hey")
}

func hoge(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "this is just normal hanlde interface")
}

func main() {
  fmt.Println("Start a local server")
	http.HandleFunc("/", sayhelloName) // set router
  http.HandleFunc("/handle_func", hey)
  http.Handle("/handle", hoge)
	err := http.ListenAndServe(":9090", nil) // set listen port
	if err != nil {
    	log.Fatal("ListenAndServe: ", err)
	}
}
