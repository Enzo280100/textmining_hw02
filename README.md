# Analysis 

## Project Description
In this project, we will practice project pipelining through the example of a simple pipeline to develop a dictionary generation. For this, we need a corpus and a clear idea of the type of vocabulary we want to track in this corpus using a dictionary method. we must identify a sample of text that aligns with the type of vocabulary we want to track, keeping this in mind throughout the process. It's best to read all the questions first and then think about the corpus, vocabulary, and question together.

## Project Structure
```
textmining_booking/
|-- booking/
|   |-- packages/
|   |   |-- __pycache__/
|   |   |-- __init__.py         # Package initialization file
|   |   |-- dataloading.py      # Data loading and cleaning
|   |   |-- processing.py       # Data processing
|   |   |-- scraper.py          # Web scraper from Booking
|   |   |-- selenium_setup.py   # Selenium setup for scraping
|   |-- Barcelona_MWC.csv       # Data extracted from Barcelona
|   |-- Milan_MWC.csv           # Data extracted from Milan
|   |-- geckodriver.exe         # Selenium driver for Firefox
|-- ITM_HW1.ipynb               # Principal Notebook
|-- hw1.pdf                     # Document with project requirements
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
### Usage
1. **Selenium Setup:**
   - Download `geckodriver.exe` for Firefox or use the appropriate driver for Chrome.
   - Place it in the project folder.
   
2. **Run the Files:**
   ```sh
   python packages/scraper.py
   python packages/dataloading.py
   python packages/processing.py
   ```
    These files generate searches on Booking webpages, extract data according to our delimitations, and preprocess the description of each hotel.

3. **Data Analysis:**
   - Run the `ITM_HW1.ipynb` notebook in Jupyter Notebook to visualize exploratory analysis, data cleaning, and the DiD regression. In this notebook, we use pipelines to call all the functions from the .py files.

## Methodology
### 1. Web Scraping
- Rental price data is collected from Booking for Barcelona and Milan.
- Navigation through multiple result pages is automated.
- Accommodation descriptions are also extracted for text analysis.

### 2. Text Analysis
- Text preprocessing is performed by removing stopwords and applying stemming.
- Wordclouds are generated before and after preprocessing.
- Terms associated with higher prices are explored.

### 3. 
- The impact of the event on prices is estimated using a difference-in-differences model.
- Additional controls based on text descriptions are included.
- Heterogeneous effects are explored according to accommodation quality.

## Contributions
This project was developed as part of an academic assignment. It is recommended to follow good practices in web scraping and respect the terms of service of the platforms used.


