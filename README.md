# Amazon Review Score Predictor

This NLP project is the result of the third project of the [Data Science](https://www.acamica.com/data-science)
career at Acámica.

The steps to fulfill the minimum requirements were:

* Perform a exploratory data analysis.
* State a hypothesis.
* Perform all necessary transformations to provide a tidy dataset.
* Train and evaluate a machine learning model and optimize its hyper-parameters.
* Interpret the results.
* Explain the difference between the expected and actual results.
* State next steps to improve the model.

Some complementary readings to improve the result are the following (spanish articles):

* [Deep learning, introducción práctica con Keras](https://torres.ai/deep-learning-inteligencia-artificial-keras/).
* [Predicciones con Incertidumbre](https://www.bbvaaifactory.com/es/improving-predictions-in-deep-learning-by-modelling-uncertainty-2/).
* [Aprendizaje automático teórico y avanzado con TensorFlow](https://www.tensorflow.org/resources/learn-ml/theoretical-and-advanced-machine-learning?hl=es-419).

### Dataset

**Note:** Amazon has deprecated their original dataset on [AWS Open Data Registry](https://registry.opendata.aws/amazon-reviews-ml/). Instead, we are using the Amazon Reviews Multi dataset from [Kaggle](https://www.kaggle.com/datasets/mexwell/amazon-reviews-multi) which provides multilingual Amazon product reviews including Spanish reviews that are the focus of this project.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile            <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         amazon_review_score_predictor and configuration for tools like black
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│
└── environment.yml    <- The requirements file for reproducing the analysis environment
```
