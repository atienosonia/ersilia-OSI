# Prediction of hERG Channel Blockage

> This project aims to use Ersilia's cardiotoxnet-herg(eos2ta5) model to predict the probability of chemical compounds   toxicity to the hERG gene. The hERG gene is crucial to heart action, small molecules blocking the gene could lead to potential heart dsyfunction, due to this, the hERG gene is a big concern for pharmaceutical companies and has lead to drugs that cause hERG-related cardiotoxicity being withdrawn from the market.
---
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)  ![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)   ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)    ![ersilia](https://img.shields.io/badge/ersilia-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)    ![rdkit](https://img.shields.io/badge/RDKit-209117?style=for-the-badge&logo=nlp&logoColor=white)
---
## Table Of Contents
- [Prediction of hERG Channel Blockage](#Prediction-of-hERG-Channel-Blockage)
  - [Table Of Contents](#table-of-contents)
    - [Objective](#objective)
    - [Data](#data)
    - [Installation](#installation)
    - [Usage](#usage)
    - [License](#license)
    - [Acknowledgements](#acknowledgements)
      - [Institution](#institution)
      - [Technologies Used](#technologies-used)
---
### Objective
---
> * To predict the probability of toxicity in the chemical compounds of drugs
---
### [Data](#data)
---
> The dataset used for this project can be found in the zipped data folder. The dataset contains 1000 entries of SMILES
---
### [Installation](#installation)
---
The project was tested on Ubuntu 22.04.3 with Python 3.7.0
> To Reproduce the project, follow these steps:
1. Clone the repository
2. Install conda dependency manager from [here](https://docs.conda.io/en/latest/)
2. Install the requirements.txt file ( `pip install -r requirements.txt` )
---