# lda_tuning.py
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

library(topicmodels)
library(doParallel)
library(ggplot2)
library(scales)
library(tidyverse)
library(RColorBrewer)
library(wordcloud)
library(ldatuning)
data("AssociatedPress", package="topicmodels")
full_data <- AssociatedPress


# system.time({
#   tunes <- FindTopicsNumber(
#     full_data,
#     topics = c(1:10 * 10, 120, 140, 160, 180, 0:3 * 50 + 200),
#     metrics = c("Griffiths2004", "CaoJuan2009", "Arun2010"),
#     method = "Gibbs",
#     control = list(seed = 77),
#     mc.cores = 4L,
#     verbose = TRUE
#   )
# })
# 
# FindTopicsNumber_plot(tunes)