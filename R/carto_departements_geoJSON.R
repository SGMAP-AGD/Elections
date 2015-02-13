# source : https://github.com/gregoiredavid/france-geojson
# source : https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson
library("rgdal")
library("rgeos")
library("maptools")
library("ggplot2")
library("dplyr")
library("stringr")
library("mapproj")
library("ggthemes")

depts <- readOGR("data/departements.geojson", "OGRGeoJSON")

plot(depts)

depts <- fortify(depts, region = "code") %>% 
  arrange(id, order)

ggplot(data = depts) + 
  geom_polygon(aes(x = long, y = lat, group = id), color = "white", fill = "grey") + 
  coord_map()

