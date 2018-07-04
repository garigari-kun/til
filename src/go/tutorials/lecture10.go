package main

import ("fmt"
        "net/http"
        "io/ioutil")

const source_url = "https://www.washingtonpost.com/news-sitemap-index.xml"

func main() {
  resp, _ := http.Get(source_url)
  bytes, _ := ioutil.ReadAll(resp.Body)
  string_body := string(bytes)
  fmt.Println(string_body)
  resp.Body.Close()
}
