---
title: How To Create a Random Pairing Generator For Your Secret Holiday Gift Exchange
layout: post
date: '2020-11-03'
excerpt: "How to create a script that will randomly pair individuals for gift giving this holiday season"
excerpt_separator:  <!--more-->
tags: 
    - R
    - Automate The Boring Things
    - Holiday
    - Quick Reads

categories: 
    - Tutorial
---

Every year in our household we hold a "Secret Maccabee" gift exchange. And, while it's not hard to manually arrange the pairings for our small family, it is tedious to do it every year (and way more fun to do it with code). Plus, by sharing this code with you here, maybe I can save some large 50 person family from headache! 

The goal is simple: Randomly match each person participating in the gift exchange with another person. The kicker in our family is that we want to always make sure that no one is matched with someone in their inner circle (i.e. no father-daughter, sibling, or in-law matchups).

I've chosen to tackle this problem with the R language for two reasons. First, because it is what I'm comfortable with and second, because it's open source for anyone that wants to utilize my code. 

The first few lines are dedicated to loading in the required packages and building a dataset. The dataset could be imported much more efficiently using a flat file but I've built it this way to show what is happening. The last 14 or so lines do all the heavy lifting.

``` R
#### Import Libraries ####
library(dplyr)

#### Declare Families and their Members #####
family1 <- c("Person1","Person2","Person3","Person4","Person5","Person6")
family2 <- c("Person7","Person8")
family3 <- c("Person9")
family4 <- c("Person10","Person11","Person12","Person13","Person14")

#### Combine Families Together In One Dataset ####
f1 <- cbind(person = family1, family = "family1")
f2 <- cbind(family2, "family2")
f3 <- cbind(family3, "family3")
f4 <- cbind(family4, "family4")
participants <- as.data.frame(rbind(f1,f2,f3,f4))

#### Recode Columns As Character Data Types ####
participants$person <- as.character(participants$person)
participants$family <- as.character(participants$family)

#### Create An Empty Vector To Hold The Matches ####
successfulMatch <- vector(mode="character")

# Check to see if the successfulMatch list is the same length as the participants list so that everyone is matched.
while (length(successfulMatch) != nrow(participants)) {
    # Recreate the empty vector if the previous pass didn't work
  successfulMatch <- vector(mode="character")
  
  #Loop through all participants
  for (i in 1:nrow(participants)){
    #Gather the participants who have not been chosen and are not in the same family as the current participant
    availableMatches <- 
      participants %>%
      filter(family != participants[i,2]) %>%
      filter(!(person %in% successfulMatch)) %>%
      select(person)
    #Randomly choose an available participant and add them to the successfulMatch vector
    successfulMatch <- c(successfulMatch,
                         availableMatches[sample(nrow(availableMatches),size = 1),1])
  }
}

#### Print Results ####
print(cbind(participants,recipient = successfulMatch))
```

And that's all there is to it! In essentially 13 lines of code, I have eased the woes of secret maccabee organizers for the foreseeable future. That said, there are undoubtedly improvements to be made. 

For instance, as I am using random numbers to select participants and families are not all the same size, sometimes I get a list where not everyone recieves a gift. I've avoided this by re-running the selection process until the number of recipients matches the number of gifters (using the `while()` loop above). I've also used the `dplyr` package to make the code more human-readible even though all functions could be performed using base R. Lastly, the process is still very manual as everytime a new family is made (marriage), or a family member enters or leaves (kids, divorce, etc.) I will need to update the data creation step. 

For now though, this process fits my need perfectly and I hope you can find some use in it as well! As always, feel free to reach out on GitHub or LinkedIn should you have any questions. 

Until next time! 🙋‍♂️📈