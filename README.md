Big Data Analysis - **Household income prediction**
===========================

### Final Presentation
- powerpoint version: https://guyleaf.pse.is/3crryq
- pdf version: https://guyleaf.pse.is/3cccv7

### 這是什麼專案？
此專案屬於大數據分析課程的期末專題，選定一個題目來做數據分析  
使用來自 Kaggle 網站的公開資料集，該資料集屬於菲律賓政府的統計部門所提供  
主要想藉此了解菲律賓國家 人民的薪水分布(target) v.s. 各項支出數值&家庭指標(features) 之間的關係，並結論出關聯性

### 資料集格式
Type of file: CSV file  
Source: Kaggle (https://www.kaggle.com/grosvenpaul/family-income-and-expenditure/)  
Data Provider: The Philippine Statistics Authority  

File Size: 21.61 MB(bytes)  
Data Size:  
* 60 columns
* 43554 rows  

Each column represents: one household feature  
Each row represents: one household

#### Features:
![image](https://user-images.githubusercontent.com/43506966/131159095-baa80466-d4a6-47b0-a189-6cd64c95da31.png)
![image](https://user-images.githubusercontent.com/43506966/131159124-71cdac45-f1f9-4cc4-82e4-edf8e3e21ece.png)


### Target 預測目標
以四分位距分為四類，收入前25%、25% ~ 50%、50% ~ 75%、75% ~ 100%  
四類資料量皆在1.2萬筆左右 (原始資料)

![image](https://user-images.githubusercontent.com/43506966/131157928-1cd964c4-e3f9-419c-b496-06c766ec99f2.png)

### Team members and task responsibility

| Member | Task                                            |
| ------ | ----------------------------------------------- |
| 李承紘 | KNN, MDC                                        |
| 楊宗洺 | SVM                                             |
| 朱柏霖 | RandomForest, DecisionTree                      |
| 應耀德 | Data Preprocessing, Data Visualization, SOM + XGBoost, XGBoost |


### Installation

```
pip install scikit-learn numpy pandas matplotlib minisom boruta
```


### Execution instructions
Total: 7 models (9 files)

```
cd models
jupyter
# choose one of jupyter files below
```
* baseline.ipynb
* DecisionTree.ipynb
* RandomForest.ipynb
* SOM.ipynb
* KNN + MDC.ipynb
* SVM (directory)
  * categorical_only.ipynb
  * mixed.ipynb
  * numeric_only.ipynb
  * selected_features_only.ipynb
