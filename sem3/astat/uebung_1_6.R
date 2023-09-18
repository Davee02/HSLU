data <- read.csv("weather.csv")
data[2, 3]
data[4,]
data1 <- data[, c("Luzern", "Zurich")]
write.csv(data1, "weather2.csv")
colnames(data)[3]
colnames(data)[2] <- "Genf"

data3 <- data[order(data[, "Zurich"]), ]
data3
