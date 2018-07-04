package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
  "encoding/xml"
)

const SourceUrl = "https://www.washingtonpost.com/news-sitemap-index.xml"

type SitemapIndex struct {
  Locations []string `xml:"sitemap>loc"`
}

type News struct {
  Titles []string `xml:"url>news>title"`
  Keywords []string `xml:"url>news>keywords"`
  Locations []string `xml:"url>loc"`
}

func main() {
  resp, _ := http.Get(SourceUrl)
  bytes, _ := ioutil.ReadAll(resp.Body)
  resp.Body.Close()

  var s SitemapIndex
  xml.Unmarshal(bytes, &s)

  for _, Location := range s.Locations {
    fmt.Println("\n%s", Location)
  }
}
