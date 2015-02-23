# Open Data Elections
# données INA

#packages
library(plyr)
library(reshape2)
# 

setwd("~/Dropbox/projets-R/ina/")
ina<-read.csv2("ina//hertzien_UTF8.csv")
ina<-ina[,c("generique")]
ina2<-ina

ina3<-gsub("s/\\([^)]*\\)//","",ina2)
ina3<-gsub("JOU,","",ina3)
ina3<-gsub("PAR,","",ina3)
ina3<-gsub(" ","",ina3)
splitage<-strsplit(ina3,";")
df <- ldply (splitage, rbind)


df2<-melt(df,id=c("ID"))
df3<-df2[,c(1,3)]
