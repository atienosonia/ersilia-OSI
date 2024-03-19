# Prediction of hERG Channel Blockage

> This project aims to use Ersilia's cardiotoxnet-herg(eos2ta5) model to predict the probability of chemical compounds   toxicity to the hERG gene. The hERG gene is crucial to heart action, small molecules blocking the gene could lead to potential heart dsyfunction, due to this, the hERG gene is a big concern for pharmaceutical companies and has lead to drugs that cause hERG-related cardiotoxicity being withdrawn from the market.

![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)  ![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)   ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)    ![ersilia](https://img.shields.io/badge/ersilia-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)    ![rdkit](https://img.shields.io/badge/RDKit-209117?style=for-the-badge&logo=nlp&logoColor=white)

## Table Of Contents
- [Prediction of hERG Channel Blockage](#Prediction-of-hERG-Channel-Blockage)
  - [Table Of Contents](#table-of-contents)
    - [Objective](#objective)
    - [Data](#data)
    - [Installation](#installation)
    - [Usage](#usage)
    - [License](#license)
    - [Acknowledgements](#acknowledgements)
      - [Technologies Used](#technologies-used)

### Objective
> * To predict the probability of toxicity in the chemical compounds of drugs

### [Data](#data)
> The dataset used for this project can be found in the zipped data folder. The dataset contains 1000 entries of SMILES

### [Installation](#installation)
The project was tested on Ubuntu 22.04.3 with Python 3.7.0
> To Reproduce the project, follow these steps:
1. Clone the repository
2. Install conda dependency manager from [here](https://docs.conda.io/en/latest/)
3. Create conda environment ( `conda create -n myenv` )
4. Activate conda environment ( `conda activate myenv` )
3. Install the requirements.txt file ( `conda install --file requirements.txt` )

### [Usage](#usage)

Single SMILE string

 ```from ersilia import ErsiliaModel```

 ```smile = "CC(=O)SC1CC2=CC(=O)CCC2(C)C2CCC3C(CCC34CCC(=O)O4)C12"```

 ```model = ErsiliaModel("eos2ta5") # pick preferred model```

 ```model.serve()```

 ```model.run(smile)```

 Multiple SMILES string

 ```from ersilia import ErsiliaModel```

 ```smiles = ["CC(=O)SC1CC2=CC(=O)CCC2(C)C2CCC3C(CCC34CCC(=O)O4)C12","CCCCCCCCCC[N+](CC)(CC)CC"]```

 ```model = ErsiliaModel("eos2ta5") # pick preferred model```

 ```model.serve()```

 ```model.run(smiles)```

### [License](#license)
> This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE.md) file for details

#### Technologies Used

- [ersilia](https://scikit-learn.org/) for creating the models.
- [RDKit](https://www.rdkit.org/) for preparation of chemical data.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) for visulizations.


