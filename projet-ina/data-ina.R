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
df4<-subset(df3,!is.na(df3$value))

personnages<-aggregate(NB~value,data=df4,sum)
personnages<-subset(personnages,personnages$NB>20)

df5<-subset(df4,df4$value%in%personnages$value)

df5<-acast(df5, ID~value,value.var="NB")

df6<-t(df5) %*% df5


rs<-rowSums(df6)
cs<-colSums(df6)
N<-sum(cs)
model.mat<-rs %*% t(cs)
model.mat<-model.mat/N
model.mat<-round(model.mat)
mat<-df6-2.5*model.mat
mat[mat<1]<-0
mat<-as.matrix(mat)
mode(mat)<-"numeric"
g<-graph.adjacency(mat,mode="upper",weighted=TRUE)

g<-simplify(g)
g<-induced.subgraph(g,degree(g)>1)

w<-walktrap.community(g)
l<-length(w) #length=nombre de communautés
w<-as.factor(w$membership)
levels(w)<-rainbow(l,start=.1,alpha=.8) 
w<-as.character(w)
V(g)$color<-w
V(g)$label.cex<-.7
V(g)$label.color<-"black"
V(g)$frame.color<-"#ffffff00"
l<-layout.fruchterman.reingold(g)
pdf("reseau.pdf",width=8,height=8)
par(mar=c(0,1,0,1))
plot(g,layout=l)
dev.off()