import pandas as pd

# Function to convert built in sklearn datasets to pandas dataframes
def sklearn_to_df(sklearn_dataset, data):
    data = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)
    data['target'] = pd.Series(sklearn_dataset.target)
    return data