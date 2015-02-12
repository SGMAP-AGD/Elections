# Ce script permet de réaliser une carte des départements en R avec leaflet
# devtools::install_github("rstudio/leaflet")

library("leaflet")
library("sp")
library("rgdal")
library("rgeos")
library("maptools")
library("ggplot2")
library("dplyr")
library("stringr")
library("mapproj")
library("ggthemes")

leaflet() %>% addTiles()

leaflet() %>%
  addTiles() %>% 
  setView(lng = 1.87528, lat = 46.60611, zoom = 6) # centre de la France 

leaflet() %>%
  addTiles() %>% 
  setView(lng = 1.87528, lat = 46.60611, zoom = 6) %>% 
  addPopups(1.87528, 46.60611, popup = "Centre de la France") 

dept <- readOGR("data/departements/", layer= "departements-20140306-5m") # Contour des départements issus d'OSM
lpoly <- SpatialPolygons(dept@polygons)

leaflet() %>%
  addTiles() %>% 
  setView(lng = 1.87528, lat = 46.60611, zoom = 6) %>% 
  addPolygons(data = lpoly)

