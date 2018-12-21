case <- read.table("/Users/wenshen/Desktop/G4003_Project/output/HPO_freq.txt",header=F,sep="\t")
case_congenital_heart_block <- case[1:329,]
case_congenital_heart_block<-case_congenital_heart_block[,-1]
rownames(case_congenital_heart_block)<-case_congenital_heart_block[,1]
case_congenital_heart_block<-case_congenital_heart_block[,-1]
matrix1<- as.matrix(case_congenital_heart_block[,5])
rownames(matrix1) <- rownames(case_congenital_heart_block)


annotation1 <- read.table("/Users/wenshen/Desktop/G4003_Project/output/overlap_congenital_heart_block.txt", sep ="\t",header=F)
rownames(annotation1) <- annotation1[,1]
annotation1 <- annotation1[,-1]
matrix2 <- as.matrix(annotation1[,5])
rownames(matrix2) <- rownames(annotation1)

annotation_overlap <-data.frame(Overlap=factor(x=character(nrow(matrix2)),labels=c("Overlap")))
rownames(annotation_overlap) <- rownames(matrix2)
Overlap<-c("blue")
names(Overlap)<-c("Overlap")
anno_colors<-list(Overlap=Overlap)

c = c(0.5,0.3,0.22,0.20,0.12,0.1,0.08,0.06,0.057,0.048,0.041,0.039,0.036,0.034,0.032,0.029,0.025,0.024,0.02,0.018,0.016,0.015,0.013,0.011,0.009,0.008,0.006,0.004,0.002,0)

mycolors <- colorRampPalette(rev(heat.colors(10)))(29)
pheatmap(matrix1,cluster_rows=F,cluster_cols=F,color=mycolors,breaks=rev(c),annotation_row=annotation_overlap,annotation_colors=anno_colors,annotation_names_row=TRUE,annotation_names_col=TRUE,show_rownames=FALSE,show_colnames=FALSE, cellwidth=30)


#c =c(0.471731449,0.287985866,0.210247350,0.196113074,0.114840989,0.090106007,0.072438163,0.058303887,0.056537102,0.047703180,0.040636042,0.038869258,0.035335689,0.033568905,0.031802120,0.028268551,0.024734982,0.022968198,0.019434629,0.017667845,0.015901060,0.014134276,0.012367491,0.010600707,0.008833922,0.007067138,0.005300353,0.003533569,0.001766784)

#mycolors <- c("white","aliceblue","antiquewhite3","aquamarine","aquamarine4","blue","blueviolet","brown1","burlywood","cadetblue1","chartreuse","chartreuse4","chocolate1","coral1","cyan","cyan4","darkblue","darkgoldenrod1","darkorchid1","darkred","darksalmon","darkseagreen1","darkslategray1","deeppink","deepskyblue","firebrick1","gold","goldenrod","goldenrod4")

#mycolors <- colorRampPalette(rev(rainbow(6)))(29)


#"white","aliceblue","antiquewhite3","aquamarine","aquamarine4","blue","blueviolet","brown1","burlywood","cadetblue1","chartreuse","chartreuse4","chocolate1","coral1","cyan","cyan4","darkblue","darkgoldenrod1","darkorchid1","darkred","darksalmon","darkseagreen1","darkslategray1","deeppink","deepskyblue","firebrick1","gold","goldenrod","goldenrod4"


case <- read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO_freq+cui.txt",header=F,sep="\t")
case_congenital_heart_block <- case[428:1181,]

case_congenital_heart_block<- case_congenital_heart_block[,-1]



rownames(case_congenital_heart_block)<- make.names(case_congenital_heart_block[,1],unique=TRUE)


case_congenital_heart_block<-case_congenital_heart_block[,-1]


matrix1<- as.matrix(case_congenital_heart_block[,5])



rownames(matrix1) <- make.names(rownames(case_congenital_heart_block),unique=TRUE)



annotation1 <- read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_down_syndrome.txt", sep ="\t",header=F)
rownames(annotation1) <- annotation1[,1]
annotation1 <- annotation1[,-1]
matrix11 <- as.matrix(annotation1[,5])
rownames(matrix11) <- make.names(rownames(annotation1),unique=TRUE)

annotation_overlap <-data.frame(Overlap=factor(x=character(nrow(matrix11)),labels=c("Overlap")))
rownames(annotation_overlap) <- make.names(rownames(matrix11),unique=TRUE)
Overlap<-c("blue")
names(Overlap)<-c("Overlap")
anno_colors<-list(Overlap=Overlap)

c = c(0.22,0.19017930734435368, 0.11171685464387489, 0.09149803790619107, 0.06769460320806021, 0.06260575437072871, 0.04996231161899083, 0.0354105018339085, 0.03119268730114705, 0.028980789038737742, 0.02836853555052907, 0.025910098872341088, 0.024907981973771087, 0.022411866121374052, 0.020677403869512345, 0.018813054823314496, 0.017437364078157377, 0.014962094600828126, 0.014194014435059804, 0.011436809180865136, 0.009104825347791081, 0.007481089125201251, 0.005906145805676888, 0.004389472673104386, 0.0018533978243858188,0)

mycolors <- colorRampPalette(rev(heat.colors(10)))(25)
pheatmap(matrix1,cluster_rows=F,cluster_cols=F,color=mycolors,breaks=rev(c),annotation_row=annotation_overlap,annotation_colors=anno_colors,annotation_names_row=TRUE,annotation_names_col=TRUE,show_rownames=FALSE,show_colnames=FALSE, cellwidth=30)

