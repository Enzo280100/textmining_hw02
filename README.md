# Homework 02 = Text Mining

## Project Description
This project involves developing a pipeline for dictionary generation from a text corpus. The goal is to track specific vocabulary within the corpus using a dictionary method. The project requires selecting a relevant corpus, defining the vocabulary categories, and implementing a methodology to extract meaningful insights.

## Project Structure
```
textmining_hw02/
|-- documents/                  # Documents for the project
|   |-- Gentzkow (2010).pdf
|   |-- Hassan (2019).pdf
|   |-- hw02.pdf
|-- packages/                   # Package initialization file
|   |-- __pycache__.py          
|   |-- categories.py           # Create new categories
|   |-- preprocessing.py        # Data processing
|-- hw02.ipynb                  # Principal Notebook
|-- README.md                   # Description the project structure
|-- requirements.txt            # Dependencies required to run
|-- setup.py                    # Installation and setup script
```

## Installation and Setup
### Requirements
To install the required dependencies, run:
```sh
pip install -r requirements.txt
```
### Running the Pipeline
1. **Prepare the Corpus:**
   - Choose a dataset from class materials or other sources like Kaggle, Google Books, or scraped web content.
   - Ensure the dataset covers diverse topics and contains metadata.
   
2. **Preprocess the Text:**
   - Run the preprocessing script to clean and normalize the text:
   ```sh
   python packages/preprocessing.py
   ```
   - This step includes removing stopwords, lemmatization, tokenization, and metadata extraction.

3. **Generate Dictionaries:**
   - Define dictionary categories in `categories.py`.
   - Run the script to generate dictionaries:
   ```sh
   python packages/categories.py
   ```
   - The script uses TF-IDF and other statistical methods to extract meaningful vocabulary.

4. **Analyze the Data:**
   - Open the Jupyter Notebook and execute the analysis:
    ```sh
   jupyter notebook hw02.ipynb
   ``` 
   - This notebook visualizes dictionary distributions and metadata-based insights.

## Methodology
1. **Data Collection**
   - The corpus consists of diverse text sources, ensuring topic coverage.
   - Metadata is extracted to categorize documents over time.
2. **Dictionary Generation**
   - Uses TF-IDF and predefined heuristics to build dictionaries.
   - Inspired by approaches from Gentzkow & Shapiro (2010), Hassan et al. (2019), and García-Uribe (2024).
3. **Analysis**
   - Computes dictionary term distributions across metadata groups.
   - Explores patterns and relationships within the corpus.

## Contributions
This project is an academic exercise in text mining and dictionary-based analysis. Ethical considerations apply when scraping and analyzing text data.

## References
- Gentzkow, M., & Shapiro, J. (2010). Media Bias and Reputation.
- Hassan, T. A., et al. (2019). Firm-Level Political Risk: Measurement and Effects.
- García-Uribe, S., et al. (2024). Economic Uncertainty and Divisive Politics.