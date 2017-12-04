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

# data("AssociatedPress", package="topicmodels")
# full_data <- AssociatedPress

# read in files
path = "/Users/swetharevanur/Documents/2_Sophomore/1_Fall/CS 221/cs221-final-project/data/"
setwd(path)
rm(df)
fileNames = unlist(list.files(pattern = "second_total_list_working*.xlsx"))
print(fileNames)
# fileName = "second_total_file_working*.xlsx"

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
  filedf = read.xls(filePath,sheet = 1,header = TRUE)
  df = rbind(filedf)  
}

print(ncol(df))

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
