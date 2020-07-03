# Q1

library(MASS)
mammals$r = mammals$brain / mammals$body
Biggest = which.max(mammals$r)
mammals[Biggest,]
Smallest = which.min(mammals$r)
mammals[Smallest,]

options(device="windows")
plot(mammals$body, mammals$r, xlab = "Body Size", ylab = "Ratio")

# Q2

db = c(dbinom(0:3, 4, 0.312))
possiblity = c(db[1:3], 1 - sum(db[1:3]))
games = c(17, 31, 17, 5)

result = chisq.test(games, p = possiblity)
result

db = c(dbinom(0:4, 5, 0.312))
possiblity = c(db[1:3], 1 - sum(db[1:3]))
games = c(5, 5, 4, 11)

result = chisq.test(games, p = possiblity)
result

# Q3

dices = c(17, 16, 20, 25, 12, 10)
possiblity[1:6] = 1 / 6
result = chisq.test(dices, p = possiblity)
if (result$p.value > 0.05) {
  print("Tossing 1 is not fair")
} else {
  print("Tossing 1 is fair")
}

possiblity[1:3] = 1 / 3
dices = c(33, 45, 22)
result = chisq.test(dices, p = possiblity[1:3])
result
if (result$p.value > 0.05) {
  print("Tossing 2 is not fair")
} else {
  print("Tossing 2 is fair")
}

#  Q4

result = prop.test(120, 276, 0.375)
result

result$conf.int

binom.test(120, 276, 0.375)

#  Q5

x1 = rnorm(100, mean = 0, sd = 1)
y1 = rnorm(100, mean = 0.2, sd = 1)
t.test(x1, y1)

x2 <- rnorm(500, mean = 0, sd = 1)
y2 <- rnorm(500, mean = 0.2, sd = 1)
t.test(x2, y2)