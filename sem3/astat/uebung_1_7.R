d.fuel <- read.table(file = "./d.fuel.dat" ,header = T, sep = ",")

d.fuel[5,]

d.fuel[1:5,]

d.fuel[c(1:3, 57:60),]

mean(d.fuel[,3])

mean(d.fuel[7:22,3])

t.kml <- d.fuel[,3] * 1.6093 / 3.789
t.kg <- d.fuel[,"weight"] * 0.45359

mean(t.kml)
mean(t.kg)
