#### Import Libraries ####
library(dplyr)

#### Build Dataset #####
family1 <- c("Person1","Person2","Person3","Person4","Person5","Person6")
family2 <- c("Person7","Person8")
family3 <- c("Person9")
family4 <- c("Person10","Person11","Person12","Person13","Person14")

f1 <- cbind(person = family1, family = "family1")
f2 <- cbind(family2, "family2")
f3 <- cbind(family3, "family3")
f4 <- cbind(family4, "family4")
participants <- as.data.frame(rbind(f1,f2,f3,f4))
participants$person <- as.character(participants$person)
participants$family <- as.character(participants$family)

successfulMatch <- vector(mode="character")

#### Perform Matching ####
while (length(successfulMatch) != nrow(participants)) {
  successfulMatch <- vector(mode="character")
  
  for (i in 1:nrow(participants)){
    participants[i,2]
    availableMatches <- 
      participants %>%
      filter(family != participants[i,2]) %>%
      filter(!(person %in% successfulMatch)) %>%
      select(person)
    successfulMatch <- c(successfulMatch,
                         availableMatches[sample(nrow(availableMatches),size = 1),1])
  }
}

#### Print Results ####
print(cbind(participants,recipient = successfulMatch))

 