This file was used for scientific research only.
The Hofstede.py file ran on Python 3.11.5. smoothly.

Create a virtual environment and make sure the necessary python libraries are installed. 


Bibliography:

Geert Hofstede. (2024). Country comparison graphs. Retrieved from https://geerthofstede.com/country-comparison-graphs/

Geert Hofstede. (n.d.). Dimension Data Matrix. Geert Hofstede. Retrieved June 16, 2024, from https://geerthofstede.com/research-and-vsm/dimension-data-matrix/


├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data               <- Should be in your computer but not on Github (only in .gitignore)
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's name, and a short `-` delimited description, e.g.
│                         `1.0-alban-data-exploration`.
│
├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
│
├── reports            <- The reports that you'll make during this project as PDF
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
│   │   └── visualize.py
