winner <- c(183, 191, 185, 185, 182, 182, 188, 188, 188, 185, 185, 177,
            182, 182, 193, 183, 179, 179, 175)
opponent <- c(191, 165, 187, 175, 193, 185, 187, 188, 173, 180, 177, 183,
              185, 180, 180, 182, 178, 178, 173)

length(winner)
length(opponent)

winner[6:9]
winner[c(3,5,10:12)]

winner[7:8] = c(189,189)
winner

winner_mean <- mean(winner)
opponent_mean <- mean(opponent)

winner_mean - opponent_mean

var(winner)
sd(winner)

winner_var <- sum((winner - winner_mean)^2) / (length(winner)-1)
winner_sd <- sqrt(winner_var)
winner_var
winner_sd

