par(mfrow=c(2,3))

overlap1<-read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_congenital_heart_block.txt",sep = "\t", header=F)
other1 <- read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/list1.txt",sep="\t",header=F)

label_overlap1<-data.frame(label=factor(x=character(nrow(overlap1)),labels=c(1)))
label_other1<-data.frame(label=factor(x=character(nrow(other1)),labels=c(0)))

overlap1_name <- overlap1[,1]
overlap1 <- overlap1[,1:6]
overlap1 <- overlap1[,-1]
overlap1 <- overlap1[,-1]
overlap1 <- overlap1[,-1]
overlap1 <- overlap1[,-1]
overlap1 <- overlap1[,-1]

data1 <- as.matrix(overlap1)

overlap1<-as.matrix(overlap1)

overlap1<-cbind(overlap1,label_overlap1)
rownames(overlap1) <- overlap1_name
colnames(overlap1) <- c("V1","label")

other1_name <- other1[,1]
other1 <- other1[,3]

data11 <- as.matrix(other1)

other1<-as.matrix(other1)

other1<-cbind(other1,label_other1)
rownames(other1) <- other1_name
colnames(other1) <- c("V1","label")

all1<-rbind(overlap1,other1)
all1<-as.data.frame(all1)

dataset <- data.frame(value = (all1$V1), group = all1$label)
boxplot( value ~ group, dataset, col = c("blue", "orange"),boxwex=c(0.3,0.3),names=c("overlap","other"),ylim=c(0,0.05),outline=FALSE,yaxt='n',ylab="frequency")
wilcox.test(value ~ group, dataset)
axis(side=2,at=c(0,0.01,0.02,0.03,0.04,0.05),labels=c(0,0.01,0.02,0.03,0.04,0.05),par(las=1),cex.axis=1)



overlap2<-read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_down_syndrome.txt",sep = "\t", header=F)
other2 <- read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/list2.txt",sep="\t",header=F)

label_overlap2<-data.frame(label=factor(x=character(nrow(overlap2)),labels=c(1)))
label_other2<-data.frame(label=factor(x=character(nrow(other2)),labels=c(0)))

overlap2_name <- overlap2[,1]
overlap2 <- overlap2[,1:6]
overlap2 <- overlap2[,-1]
overlap2 <- overlap2[,-1]
overlap2 <- overlap2[,-1]
overlap2 <- overlap2[,-1]
overlap2 <- overlap2[,-1]

data2 <- as.matrix(overlap2)

overlap2<-as.matrix(overlap2)

overlap2<-cbind(overlap2,label_overlap2)
rownames(overlap2) <- overlap2_name
colnames(overlap2) <- c("V1","label")

other2_name <- other2[,1]
other2 <- other2[,3]

data22 <- as.matrix(other2)

other2<-as.matrix(other2)

other2<-cbind(other2,label_other2)
rownames(other2) <- other2_name
colnames(other2) <- c("V1","label")

all2<-rbind(overlap2,other2)
all2<-as.data.frame(all2)

dataset <- data.frame(value = (all2$V1), group = all2$label)
boxplot( value ~ group, dataset, col = c("blue", "orange"),boxwex=c(0.3,0.3),names=c("overlap","other"),ylim=c(0,0.05),outline=FALSE,yaxt='n',ylab="frequency")
wilcox.test(value ~ group, dataset)

axis(side=2,at=c(0,0.01,0.02,0.03,0.04,0.05),labels=c(0,0.01,0.02,0.03,0.04,0.05),par(las=1),cex.axis=1)



overlap3<-read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_neuroblastoma.txt",sep = "\t", header=F)
other3 <- read.table("/Users/wenshen/Desktop/G4003_Project/output/10source/list3.txt",sep="\t",header=F)

label_overlap3<-data.frame(label=factor(x=character(nrow(overlap3)),labels=c(1)))
label_other3<-data.frame(label=factor(x=character(nrow(other3)),labels=c(0)))

overlap3_name <- overlap3[,1]
overlap3 <- overlap3[,1:6]
overlap3 <- overlap3[,-1]
overlap3 <- overlap3[,-1]
overlap3 <- overlap3[,-1]
overlap3 <- overlap3[,-1]
overlap3 <- overlap3[,-1]

data3 <- as.matrix(overlap3)

overlap3<-as.matrix(overlap3)

overlap3<-cbind(overlap3,label_overlap3)
rownames(overlap3) <- overlap3_name
colnames(overlap3) <- c("V1","label")

other3_name <- other3[,1]
other3 <- other3[,3]

data33 <- as.matrix(other3)
other3<-as.matrix(other3)

other3<-cbind(other3,label_other3)
rownames(other3) <- other3_name
colnames(other3) <- c("V1","label")

all3<-rbind(overlap3,other3)
all3<-as.data.frame(all3)

dataset <- data.frame(value = (all3$V1), group = all3$label)
boxplot( value ~ group, dataset, col = c("blue", "orange"),boxwex=c(0.3,0.3),names=c("overlap","other"),ylim=c(0,0.05),outline=FALSE,yaxt='n',ylab="frequency")
wilcox.test(value ~ group, dataset)
axis(side=2,at=c(0,0.01,0.02,0.03,0.04,0.05),labels=c(0,0.01,0.02,0.03,0.04,0.05),par(las=1),cex.axis=1)


