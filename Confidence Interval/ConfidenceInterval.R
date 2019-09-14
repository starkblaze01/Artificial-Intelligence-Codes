mean <- 5
sd <- 2
n <- 30

count = 0

y <- seq(1,100)

for(val in y){
sample <- rnorm(30,5,2)
samplemean <- mean(sample)

err <- qnorm(0.95)*sd/sqrt(n)
li <- samplemean - err
ri <- samplemean + err

if(mean > li && mean <ri){
  count = count +1
}
}
print(count)