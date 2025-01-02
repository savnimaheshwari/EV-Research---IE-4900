# Install and load required packages
install.packages(c(
  "readxl", "ggplot2", "dplyr", "gridExtra", "corrplot", "car", 
  "glmnet", "MASS", "rpart", "rpart.plot", "randomForest", 
  "gam", "splines", "vioplot", "e1071"
))

library(readxl)
library(ggplot2)
library(dplyr)
library(gridExtra)
library(corrplot)
library(car)
library(glmnet)
library(MASS)
library(rpart)
library(rpart.plot)
library(dplyr)
library(randomForest)
library(gam)
library(splines)
library(vioplot)
library(e1071)
# Read the Excel file
evdata <- read_excel("~/Desktop/FullDataFile.xlsx")  # Replace with the correct file path
evdata <- na.omit(evdata)


# Split the data (e.g., 80% for training, 20% for testing)
set.seed(1234)  # For reproducibility
train_index <- sample(1:nrow(evdata), 0.8 * nrow(evdata))
evdata.train <- evdata[train_index, ]
evdata.test <- evdata[-train_index, ]

gam.full <- gam(EVREG~.-STATE-YEAR,data = evdata.train)
gam.full.in <- predict(gam.full, evdata.train)
gam.full.out <- predict(gam.full,evdata.test)

in_sample_mse <- mean((evdata.train$EVREG - gam.full.in)^2)
out_sample_mse <- mean((evdata.test$EVREG - gam.full.out)^2)

in_sample_rmse <- round(sqrt(in_sample_mse),2)
out_sample_rmse <- round(sqrt(out_sample_mse),2)
adj_r2_in <- round(1- (in_sample_mse / var(evdata.train$SALES)),4)
adj_r2_out <- round(1 - (out_sample_mse / var(evdata.test$SALES)),4)

print(paste("Full GAM In Sample RMSE:" , in_sample_rmse ))
print(paste("Full GAM  Out of Sample RMSE:", out_sample_rmse))
print(paste("Full GAM  In Sample Adjusted R^2:", adj_r2_in))
print(paste("Full GAM  Out of Sample Adjusted R^2:", adj_r2_out))

#this is the scope list. I have added EVREG
scope_list = list("SALES" = ~1 + SALES + s(SALES, df = 2) + s(SALES, df = 3) + s(SALES, df = 4) + s(SALES, df = 5),
  "EDU"= ~1+ EDU+ s(EDU, df=2)+s(EDU, df=3)+s(EDU, df =4)+s(EDU, df=5),
 # "MEDINC"= ~1+ MEDINC+ s(MEDINC, df=2)+s(MEDINC, df=3)+s(MEDINC, df =4)+s(MEDINC, df=5),
  "TIME"= ~1+ TIME+ s(TIME, df=2)+s(TIME, df=3)+s(TIME, df =4)+s(TIME, df=5),
  "SOLAR" = ~1 + SOLAR + s(SOLAR, df=2) + s(SOLAR, df=3) + s(SOLAR, df =4) + s(SOLAR, df=5),
  "WIND" = ~1 + WIND + s(WIND, df=2) + s(WIND, df=3) + s(WIND, df =4) + s(WIND,    df=5),
 # "SGDP" = ~1 + SGDP + s(SGDP, df=2) + s(SGDP, df=3) + s(SGDP, df =4) + s(SGDP,    df=5),
  #"CO2" = ~1 + CO2 + s(CO2, df=2) + s(CO2, df=3) + s(CO2, df =4) + s(CO2, df=5),
  "PUBTR" = ~1 + PUBTR + s(PUBTR, df=2) + s(PUBTR, df=3) + s(PUBTR, df =4) + s(PUBTR,df=5),
  "EMPLOY"= ~1+ EMPLOY+ s(EMPLOY, df=2)+s(EMPLOY, df=3)+s(EMPLOY, df =4)+s(EMPLOY, df=5),
  "HH1VEH"= ~1+ HH1VEH+ s(HH1VEH, df=2)+s(HH1VEH, df=3)+s(HH1VEH, df =4)+s(HH1VEH, df=5),
 # "HH2VEH"= ~1+ HH2VEH+ s(HH2VEH, df=2)+s(HH2VEH, df=3)+s(HH2VEH, df =4)+s(HH2VEH, df=5),
  "TOTVEH" = ~1 + TOTVEH + s(TOTVEH, df=2) + s(TOTVEH, df=3) + s(TOTVEH, df =4) + s(TOTVEH,df=5),
  "GAS" = ~1 + GAS + s(GAS, df=2) + s(GAS, df=3) + s(GAS, df =4) + s(GAS,df=5),
  "ELEC"= ~1+ ELEC+ s(ELEC, df=2)+s(ELEC, df=3)+s(ELEC, df =4)+s(ELEC, df=5),
  "POP"= ~1+ POP+ s(POP, df=2)+s(POP, df=3)+s(POP, df =4)+s(POP, df=5),
  "POVERTY"= ~1+ POVERTY+ s(POVERTY, df=2)+s(POVERTY, df=3)+s(POVERTY, df =4)+s(POVERTY, df=5),
  "EVMOD"= ~1+ EVMOD+ s(EVMOD, df=2)+s(EVMOD, df=3)+s(EVMOD, df =4)+s(EVMOD, df=5),
  "PORTS" = ~1 + PORTS + s(PORTS, df=2) + s(PORTS, df=3) + s(PORTS, df =4) + s(PORTS,df=5),
  "STATIONS" = ~1 + STATIONS + s(STATIONS, df=2) + s(STATIONS, df=3) + s(STATIONS, df =4) + s(STATIONS,df=5),
  "AFPOL" = ~1 + AFPOL + s(AFPOL, df=2) + s(AFPOL, df=3) +  s(AFPOL, df =4) + s(AFPOL,df=5),
  "OOH" = ~1 + OOH + s(OOH, df=2) + s(OOH, df=3) + s(OOH, df =4) + s(OOH,df=5),
 # "DETACH" = ~1 + DETACH + s(DETACH, df=2) + s(DETACH, df=3) +  s(DETACH, df =4) + s(DETACH,df=5),
  "RANGE"= ~1+ RANGE+ s(RANGE, df=2)+s(RANGE, df=3)+s(RANGE, df =4)+s(RANGE, df=5),
  "CHARGE" = ~1 + CHARGE + s(CHARGE, df=2) + s(CHARGE, df=3) +  s(CHARGE, df =4) + s(CHARGE,df=5), 
  "ZEM" = ~1 + ZEM + s(ZEM, df=2) + s(ZEM, df=3) + s(ZEM, df =4) + s(ZEM,df=5),
  "LAND"= ~1+ LAND+ s(LAND, df=2)+s(LAND, df=3)+s(LAND, df =4)+s(LAND, df=5),
  "POPDENS"= ~1+ POPDENS+ s(POPDENS, df=2)+s(POPDENS, df=3)+s(POPDENS, df =4)+s(POPDENS, df=5),
 # "DETACH_PER"= ~1+ DETACH_PER+ s(DETACH_PER, df=2)+s(DETACH_PER, df=3)+s(DETACH_PER, df =4)+s(DETACH_PER, df=5),
  "OOH_PER" = ~1 + OOH_PER + s(OOH_PER, df=2) + s(OOH_PER, df=3) +             s(OOH_PER, df =4) + s(OOH_PER,df=5),
  "VMT"= ~1+ VMT+ s(VMT, df=2)+s(VMT, df=3)+s(VMT, df =4)+s(VMT, df=5),
  "VEHMFG"= ~1+ VEHMFG+ s(VEHMFG, df=2)+s(VEHMFG, df=3)+s(VEHMFG, df =4)+s(VEHMFG, df=5),
  "PRICE" = ~1 + PRICE + s(PRICE, df=2) + s(PRICE, df=3) + s(PRICE, df =4) + s(PRICE,df=5),
  "TRAVELCOST" = ~1 + TRAVELCOST + s(TRAVELCOST, df=2) + s(TRAVELCOST, df=3) + s(TRAVELCOST, df =4) + s(TRAVELCOST,df=5),
  "TRAVELCOST_INC" = ~1 + TRAVELCOST_INC + s(TRAVELCOST_INC, df=2) + s(TRAVELCOST_INC, df=3) + s(TRAVELCOST_INC, df =4) + s(TRAVELCOST_INC,df=5),
  "RENEWGEN"= ~1 + RENEWGEN + s(RENEWGEN, df=2) + s(RENEWGEN, df=3) + s(RENEWGEN, df =4) + s(RENEWGEN,df=5),
  "TOTGEN"= ~1 + TOTGEN + s(TOTGEN, df=2) + s(TOTGEN, df=3) + s(TOTGEN, df =4) + s(TOTGEN,df=5),
  "TOTNEWGEN"= ~1 + TOTNEWGEN + s(TOTNEWGEN, df=2) + s(TOTNEWGEN, df=3) + s(TOTNEWGEN, df =4) + s(TOTNEWGEN,df=5),
  # "HOSOLAR"= ~1 + HOSOLAR + s(HOSOLAR, df=2) + s(HOSOLAR, df=3) + s(HOSOLAR, df =4) + s(HOSOLAR,df=5),
  "PRIVEH" = ~1 + PRIVEH + s(PRIVEH, df=2) + s(PRIVEH, df=3) + s(PRIVEH, df =4) + s(PRIVEH,df=5))



#doing reduced GAM
gam_test <- gam(EVREG~-STATE-YEAR, data = evdata.train)

gam_red <- step.Gam(gam_test,scope_list, direction = "both",trace = TRUE)

#added EVREG as a linear term / maybe should add it as a smooth term
gam_final <- gam(EVREG ~ EDU + s(SOLAR, df = 5) + s(WIND, df = 5) + HH1VEH +
                   GAS + ELEC + s(PORTS, df = 5) + OOH + s(RANGE, df = 3) + 
                   CHARGE + s(POPDENS, df = 2) + OOH_PER + PRICE +  
                   + TOTGEN + SALES, data = evdata.train)


summary(gam_final)


par(mfrow = c(2,2))
plot(gam_final, se=T)

gam.model.in <- predict(gam_final, evdata.train)
gam.model.out <- predict(gam_final,evdata.test)

in_sample_mse <- mean((evdata.train$EVREG - gam.model.in)^2)
out_sample_mse <- mean((evdata.test$EVREG - gam.model.out)^2)

in_sample_rmse <- round(sqrt(in_sample_mse),2)
out_sample_rmse <- round(sqrt(out_sample_mse),2)
adj_r2_in <- round(1- (in_sample_mse / var(evdata.train$EVREG)),4)
adj_r2_out <- round(1 - (out_sample_mse / var(evdata.test$EVREG)),4)

print(paste("Reduced GAM In Sample RMSE:" , in_sample_rmse ))
print(paste("Reduced GAM  Out of Sample RMSE:", out_sample_rmse))
print(paste("Reduced GAM  In Sample Adjusted R^2:", adj_r2_in))
print(paste("Reduced GAM  Out of Sample Adjusted R^2:", adj_r2_out))


set.seed(2804)
folds<-10
evdata$fold<-sample(x=1:folds,size=nrow(evdata),replace=T) # assign folds

#Random Forest with CV (10 folds)
RFIS.mse <- 0
RFOS.mse <- 0
RFIS.adjr <- 0
RFOS.adjr <- 0

for(i in 1:folds){
  set.seed(2804)
  ev.train <- evdata[-which(evdata$fold == i),]
  ev.test <- evdata[which(evdata$fold == i),]
  RF.mod <- randomForest(EVREG ~ ., data = ev.train)
  
  RF.predIS <- predict(RF.mod, newdata = ev.train)
  RF.predOS <- predict(RF.mod, newdata = ev.test)
  
  # Remove NA values from predictions and actual values
  valid_train_idx <- !is.na(RF.predIS) & !is.na(ev.train$EVREG)
  valid_test_idx <- !is.na(RF.predOS) & !is.na(ev.test$EVREG)
  
  # Only keep non-NA data for MSE and Adjusted R^2 calculations
  RF.predIS <- RF.predIS[valid_train_idx]
  ev.train.reg <- ev.train$EVREG[valid_train_idx]
  
  RF.predOS <- RF.predOS[valid_test_idx]
  ev.test.reg <- ev.test$EVREG[valid_test_idx]
  
  # Calculate MSE and Adjusted R^2
  RFIS.mse[i] <- mean((RF.predIS - ev.train.reg)^2)
  RFOS.mse[i] <- mean((RF.predOS - ev.test.reg)^2)
  
  RFIS.adjr[i] <- 1 - (RFIS.mse[i] / var(ev.train.reg, na.rm = TRUE))
  RFOS.adjr[i] <- 1 - (RFOS.mse[i] / var(ev.test.reg, na.rm = TRUE))
}

# Print results
print(paste0("The mean of 10-fold Random Forest in-sample RMSE was: ", round(sqrt(mean(RFIS.mse)), 2)))
print(paste0("The mean of 10-fold Random Forest out-sample RMSE was: ", round(sqrt(mean(RFOS.mse)), 2)))
print(paste0("The mean of 10-fold Random Forest In Sample Adjusted R^2 was: ", round(mean(RFIS.adjr), 4)))
print(paste0("The mean of 10-fold Random Forest Out of Sample Adjusted R^2 was: ", round(mean(RFOS.adjr), 4)))

