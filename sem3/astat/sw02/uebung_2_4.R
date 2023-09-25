head(InsectSprays)

tapply(InsectSprays[, "count"], InsectSprays[, "spray"], FUN = mean)

boxplot(count ~ spray,
        data = InsectSprays,
        col=c("orange", "blue", "darkseagreen", "deeppink",
              "brown", "aquamarine")
)

