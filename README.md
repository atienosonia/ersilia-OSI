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
> The dataset used for this project can be found in the data folder. The dataset contains 1000 entries of SMILES
> The dataset is called reference_library.csv

### [Installation](#installation)
The project was tested on Ubuntu 22.04.3 with Python 3.7.12
> To Reproduce the project, follow these steps:
> From your Ubuntu Terminal
1. Install miniconda 

`mkdir -p ~/miniconda3` 
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh` 
`bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3` 
`rm -rf ~/miniconda3/miniconda.sh`
`~/miniconda3/bin/conda init bash`
2. Install Git and Github CLI 
Install Git through [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Installing Github CLI 

Use conda to install Github CLI

`conda install gh -c conda-forge`
`gh auth login`

3. Install Git LFS 
`conda install git-lfs -c conda-forge`
`git-lfs install`

4. Create conda environment ( `conda create -n ersilia python=3.7` )
5. Activate conda environment ( `conda activate ersilia` )
6. Install ersilia ( `pip install ersilia`)

This project was run on Visual Studio Code, if you are using WSL Ubuntu you just have to install Visual Studio Code on your Windows operating system, then right on your Ubuntu terminal where you have activate conda ersilia environment run the command `code .` This should open visual studio code. Proceed to install Jupyer Notebook and Python Extension

![alt text](figures/extpython.jpg)
![alt text](figures/jupyterext.jpg)


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

### [Technologies Used](#technologies-used) 

- [ersilia](https://www.ersilia.io/) for creating the models.
- [RDKit](https://www.rdkit.org/) for preparation of chemical data.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) for visulizations.


