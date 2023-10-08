daten <- read.csv("sw03/mannfrau.csv")
head(daten)

plot(daten$groesse.mann, daten$groesse.frau,
     xlab = "Grösse Mann (in cm)",
     ylab = "Grösse Frau (in cm)",
     col = "blue",
     pch = 20
)

regressionsgerade <- lm(daten$groesse.frau ~ daten$groesse.mann)
abline(regressionsgerade)
regressionsgerade # y = 110.440 + 0.2884x

