df <- read.table("sw03/income.dat", header = T)
head(df)

plot(df$Educ, df$Income2005,
     xlab = "Anzahl Schuljahre",
     ylab = "Einkommen 2005",
     col = "blue",
     pch = 20)
abline(lm(df$Income2005 ~ df$Educ), col="green", lwd=3)

plot(df$AFQT, df$Income2005,
     xlab = "IQ",
     ylab = "Einkommen 2005",
     col = "green",
     pch = 20)
abline(lm(df$Income2005 ~ df$AFQT), col="blue", lwd=3)
