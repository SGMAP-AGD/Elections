# Open Data Elections
# données INA
setwd("~/Dropbox/projets-R/ina/")
ina<-read.csv2("ina//hertzien_UTF8.csv")
ina<-ina[,c("generique")]
ina2<-ina

ina3<-gsub("s/\\([^)]*\\)//","",ina2)
