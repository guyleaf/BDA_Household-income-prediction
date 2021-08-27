Big Data Analysis - **Household income prediction**
===========================


### Final Presentation
- powerpoint version: https://guyleaf.pse.is/3crryq
- pdf version: https://guyleaf.pse.is/3cccv7

### Data Source
- Kaggle: https://www.kaggle.com/grosvenpaul/family-income-and-expenditure/

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
