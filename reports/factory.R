data <- read.csv("factory_trans.csv", header=FALSE)
inputData <- data.frame(data[, c(6, 11, 131)], response = as.factor(data[, c(216)]))
svmfit <- svm(response ~ ., data = inputData, kernel = "radial", cost = 10, gamma = 1000, scale = FALSE)
result = mean(inputData$response == predict(svmfit))
print(result)
set.seed(100)
rowIndices <- 1 : nrow(inputData) 
sampleSize <- 0.8 * length(rowIndices) 
trainingRows <- sample (rowIndices, sampleSize) 
trainingData <- inputData[trainingRows, ] 
testData <- inputData[-trainingRows, ] 
tuned <- tune.svm(response ~., data = trainingData, gamma = 10^(-3:1), cost = 10^(1:3))
print(summary (tuned))