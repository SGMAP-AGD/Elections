# Ce script permet de réaliser une simple carte des départements en R
# Les contours des départements issus d'OSM
# URL : https://www.data.gouv.fr/fr/datasets/contours-des-departements-francais-issus-d-openstreetmap/

library("rgdal")
library("rgeos")
library("maptools")
library("ggplot2")
library("dplyr")
library("stringr")
library("mapproj")
library("ggthemes")

dept <- readOGR("data/departements/", layer= "departements-20140306-5m")
dept <- fortify(dept, region = "code_insee")

dept %>% 
  filter(str_length(id) == 2) %>% 
  ggplot() + 
    geom_polygon(aes(x = long, y = lat, group = group), color = "grey", fill = "white") + 
    coord_map(projection = "mercator") + 
    theme_tufte(ticks = FALSE) + 
    theme(axis.text = element_blank(), 
          axis.title = element_blank()) + 
    labs(title = "Carte des départements de France métropolitaine en 2014")


