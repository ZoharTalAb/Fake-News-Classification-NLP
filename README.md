# Fake News Classification using Custom Multinomial Naive Bayes 📰🤖

This project was developed as part of the Machine Learning course at HIT (Holon Institute of Technology).
The goal is to classify news articles as fake or real using NLP techniques and a custom implementation of Multinomial Naive Bayes.

## Authors

- Zohar Avramoviz
- [Add partner name]

## Project Overview

This project includes:

- Data loading and exploration
- Text preprocessing and cleaning
- Feature engineering (CountVectorizer, TF-IDF, bigrams)
- Custom Naive Bayes implementation
- Grid Search with 5-Fold Cross Validation
- Model evaluation (F1, Precision, Recall, Accuracy)

## Dataset

Fake News Classification dataset from Kaggle:
https://www.kaggle.com/datasets/aadyasingh55/fake-news-classification

Files used:

- train.csv
- test.csv
- evaluation.csv

## Results

- Best Model: CountVectorizer with title + text
- Best Alpha: 0.5
- Cross Validation F1: ~0.935
- Final Test F1: ~0.94
- Accuracy: ~0.94

## Technologies

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Jupyter Notebook

## How to Run

1. Clone the repository:
   git clone https://github.com/ZoharTalAb/Fake-News-Classification-NLP.git

2. Enter the folder:
   cd Fake-News-Classification-NLP

3. Create environment:
   python -m venv .venv
   source .venv/Scripts/activate

4. Install packages:
   python -m pip install pandas numpy scikit-learn matplotlib jupyter

5. Run:
   jupyter notebook

## Notes

- The Naive Bayes model was implemented from scratch.
- scikit-learn was used only for tools like vectorizers and evaluation.
- The focus is on demonstrating the full ML pipeline.

## Conclusion

The project demonstrates that Multinomial Naive Bayes combined with proper feature engineering can achieve strong performance on fake news classification tasks.
