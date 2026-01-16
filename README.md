
# Machine Learning Practice

This repository contains my implementations and experiments while studying
"Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow".

## Covered topics
- Linear Regression (from scratch + sklearn)
- Logistic Regression
- Classification (MNIST, Titanic)
- Model training and evaluation
- Working with real datasets

Purpose: learning and practice.
## Some questions to answer

# Can I defend why preprocessing is inside pipelines?
- Preprocessing is inside pipelines because preprocessing steps (such as scaling, imputation, and encoding) learn parameters from data.
- If preprocessing is done outside the pipeline, these parameters may be computed using validation or test data, causing data leakage.
-Pipelines guarantee that preprocessing is fit only on the training data and then reused unchanged for validation and test data, ensuring realistic evaluation and preventing overly optimistic metrics.

# Can I design a pipeline without looking at docs?
Yes. Given a real-world dataset, I would:

- Split the data into training, validation, and test sets.
- Apply numeric preprocessing (median imputation and feature scaling).
- Apply categorical preprocessing (most-frequent imputation and one-hot encoding).
- Combine numeric and categorical transformations using a ColumnTransformer.
- Attach the model at the end of the pipeline so all preprocessing and training happen as a single, leak-free workflow.
# Why might a reported metric be lying?
- A reported metric may be misleading if the evaluation protocol allows information from validation or test data to influence training.
- Common causes include data leakage, improper train–test splitting, preprocessing performed on the full dataset, or repeated tuning on the test set.
- In such cases, the metric appears high, but the model fails to generalize to truly unseen real-world data..

# What happens if you tune hyperparameters on the test set?
- If you tune on test set:
- Test set becomes part of training
- Test error becomes meaningless
- You have no true measure of generalization

# Difference between cross-validation and a validation set?
# Validation Set
- One fixed split
- Simple
- Can be noisy (depends on luck of split)
# Cross-Validation
- Multiple splits (k-fold)
- Average performance
- More reliable
- Slower but safer when data is small