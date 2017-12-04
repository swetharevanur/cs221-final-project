# lda_tuning.R
# Computes optimal LDA hyperparamater (number of topics) 
# by optimizing 3 metrics.
# Authors: Swetha Revanur and Keanu Spies

# install.packages("topicmodels")
# install.packages("doParallel")
# install.packages("ggplot2")
# install.packages("scales")
# install.packages("tidyverse")
# install.packages("RColorBrewer")
# install.packages("wordcloud")
# install.packages("ldatuning")
# install.packages("gdata")
# install.packages("tm")
# install.packages("readxl")

library(topicmodels)
library(doParallel)
library(ggplot2)
library(scales)
library(tidyverse)
library(RColorBrewer)
library(wordcloud)
library(ldatuning)
library(gdata)
library(tm)
library(readxl)

# data("AssociatedPress", package="topicmodels")
# full_data <- AssociatedPress

# read in files
path = "/Users/swetharevanur/Documents/2_Sophomore/1_Fall/CS 221/cs221-final-project/data/"
setwd(path)
fileNames = unlist(list.files(pattern = "filtered_third_total_file_list.xlsx"))
print(fileNames)

# declare empty dataframe
columnNames = c("postCategory", "postDay", "postDistrict", "postID",
                "postLocation", "postMonth", "postOtherAds", 
                "postPhone", "postText", "postTime", "postTitle", "postYear")
df <- data.frame(matrix(ncol = length(columnNames), nrow = 0), stringsAsFactors = FALSE)
colnames(df) = columnNames

# populate df
for (fileName in fileNames) {
  fileName = toString(fileName)
  filePath = paste(path, fileName, sep = "")
  filedf = read_excel(filePath)
  # filedf = read.xls(filePath, sheet = 1, header = TRUE)
  df = rbind(filedf)  
}

# add another column that is the concatenation of the title + text columns
colsToPaste = c('postText', 'postTitle')

# create a new column `x` with the three columns collapsed together
df$mergedPost <- apply(df[, colsToPaste], 1, paste, collapse = " ")

corpus<-Corpus(VectorSource(c(df['mergedPost'])))

full_data = DocumentTermMatrix(corpus)

system.time({
  tunes <- FindTopicsNumber(
    full_data,
    topics = c(1:10 * 10, 120, 140, 160, 180, 0:3 * 50 + 200),
    metrics = c("Griffiths2004", "CaoJuan2009", "Arun2010"),
    method = "Gibbs",
    control = list(seed = 77),
    mc.cores = 4L,
    verbose = TRUE
  )
})

FindTopicsNumber_plot(tunes)

#----------------5-fold cross-validation, different numbers of topics----------------
burnin = 1000
iter = 1000
keep = 50

cluster <- makeCluster(detectCores(logical = TRUE) - 1) # leave one CPU spare...
registerDoParallel(cluster)

clusterEvalQ(cluster, {
  library(topicmodels)
})

folds <- 5
splitfolds <- sample(1:folds, n, replace = TRUE)
candidate_k <- c(2, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300) # candidates for how many topics
clusterExport(cluster, c("full_data", "burnin", "iter", "keep", "splitfolds", "folds", "candidate_k"))

# we parallelize by the different number of topics.  A processor is allocated a value
# of k, and does the cross-validation serially.  This is because it is assumed there
# are more candidate values of k than there are cross-validation folds, hence it
# will be more efficient to parallelise
system.time({
  results <- foreach(j = 1:length(candidate_k), .combine = rbind) %dopar%{
    k <- candidate_k[j]
    results_1k <- matrix(0, nrow = folds, ncol = 2)
    colnames(results_1k) <- c("k", "perplexity")
    for(i in 1:folds){
      train_set <- full_data[splitfolds != i , ]
      valid_set <- full_data[splitfolds == i, ]
      
      fitted <- LDA(train_set, k = k, method = "Gibbs", control = list(burnin = burnin, iter = iter, keep = keep))
      results_1k[i,] <- c(k, perplexity(fitted, newdata = valid_set))
    }
    return(results_1k)
  }
})
stopCluster(cluster)

results_df <- as.data.frame(results)

ggplot(results_df, aes(x = k, y = perplexity)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  ggtitle("5-fold cross-validation of topic modelling with the 'Associated Press' dataset",
          "(ie five different models fit for each candidate number of topics)") +
  labs(x = "Candidate number of topics", y = "Perplexity when fitting the trained model to the hold-out set")

