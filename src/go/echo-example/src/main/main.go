package main

import (
  "fmt"
  "net/http"
  "github.com/labstack/echo"
)

// /
func yallo(c echo.Context) error {
  return c.String(http.StatusOK, "yallo page")
}

// /cats/:data
func getCats(c echo.Context) error {
  catName := c.QueryParam("name")
  catType := c.QueryParam("type")

  dataType := c.Param("data")

  if dataType == "string" {
    return c.String(http.StatusOK, fmt.Sprintf("Cat name is %s and type is %s", catName, catType))
  } else if dataType == "json" {
    return c.JSON(http.StatusOK, map[string]string {
      "name": catName,
      "type": catType,
    })
  } else {
    return c.JSON(http.StatusBadRequest, map[string]string {
      "error": "You must specify what data type is you want.",
    })
  }

}


func main() {
  fmt.Println("Start Fusuma.....")

  e := echo.New()

  e.GET("/", yallo)
  e.GET("/cats/:data", getCats)

  e.Start(":3000")
}
