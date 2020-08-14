### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#project motivation)
3. [File Descriptions](#file descriptions)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing, authors, acknowledgements)


## Installation

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. 
The code should run with no issues using Python versions 3.*.
Nevertheless, as not everyone is using anaconda you can find the used packages in the
[requirements.txt](requirements.txt)-file and install them via
`pip install -r requirements.txt`.


## Project Motivation
For this project, I was interested in using Stack Overflow data from 2017 to better understand:

1. Which programming languages give developers the highest satisfaction?
2. Which programming languages provide developers with the highest salary?
3. Which programming languages seem to have a promising future?
4. How reliable are our answers to question 3?
(To check that I used the Stack Overflow data from 2018 and compared it with our predictions based on the 2017 data.)


## File Descriptions
There are 3 jupyter notebooks available in the
[notebooks](notebooks)-folder to showcase work related to the above questions.  

[language_satisfaction_salary.ipynb](notebooks/language_satisfaction_salary.ipynb)
corresponds to question 1 and question 2.
[language_popularity_2017.ipynb](notebooks/language_popularity_2017.ipynb)
corresponds to question 3.
[language_popularity_2017_2018.ipynb](notebooks/language_popularity_2017_2018.ipynb)
corresponds to question 4.

The Stackoverflow from 2017 and 2018 data used for the notebooks can be downloaded
[here](https://insights.stackoverflow.com/survey).
To use it in the notebooks put the survey result files in the data directory.
The exact names of the required files are present at the beginning of each notebook.


## Results
The main findings of the code can be found at the post available [here]().


## Licensing, Authors, Acknowledgements
Must give credit to Stack Overflow for the data.
You can find the Licensing for the data and other descriptive information in the README.txt file that comes with the download.
Otherwise, feel free to use the code here as you would like!
