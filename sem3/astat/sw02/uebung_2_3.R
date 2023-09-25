data <- read.csv("./sw02/mannfrau.csv")
head(data)

diff <- data["alter.mann"] - data["alter.frau"]

boxplot(diff)
