# eos2ta5 Model Validation

Ersilia Model Hub is an open source repository of AI/ML models used for biomedical research. This project aims to look at one of the models from the Hub to check if the model is accurate and reproducible. This will be done through running a series of tasks


### [Project Task 1](#task1)

* Run predictions of 1000 molecules and evaluate results

* You can get molecules from public databases such as [PubChem](https://pubchem.ncbi.nlm.nih.gov/), [ChEMBL](https://www.ebi.ac.uk/chembl/), [DrugBank](https://go.drugbank.com/) and [ZINC](https://zinc20.docking.org/)


### [Project Task 2](#task2)
* Identify a result that can be produced from the authors publication, after producing the result check if they are the same as the result the authors obtained in their publication.

* The author's publication can be found [here](https://drive.google.com/file/d/18ul4T1nYLA8z1bHCVe4nK-IcNpIx58nv/view?usp=sharing), the model whose results we are trying to reproduce is known as cardiotox net

* The datasets that were used to train the model can be found [here](https://github.com/Abdulk084/CardioTox/tree/master/data)

* Three test sets were used to train the model, train set 1 had a total of 12,620 molecules with 6643 labelled as hERG blockers and 5977 as hERG non-blockers, train set 2 had 11 blockers and 30 non-blockers and train set 3 had 53 blockers and 786 non-blockers

* The model was tested on Ubuntu 20.04 Python 3.8

* To run the cardiotox net model follow the steps below :

1. install miniconda 

2. download environment.yml file from [here](https://github.com/Abdulk084/CardioTox/blob/master/environment.yml)

3. restore environment.yml

```conda env create -f environment.yml```

4. activate the environment

```conda activate cardiotox```

5. install pyBioMed

```cd PyBioMed```

```python setup.py install```

```cd ..```

6. test the model

```python test.py```

You should get the below output :

![alt text](figures/cardiotoxevalmetrics.jpg)

You might encounter the error ```ModuleNotFoundError: No module named 'numpy.random.bit_generator'``` while running ```python test.py```, you can solve this by running the following codes in your Ubuntu command line interface

```pip install protobuf==3.20.0```

```pip install numpy==1.19.5```

now you should be able to run ```python test.py``` without generating any error.

To generate the results the authors got (i.e NPV, SPE, SEN etc) you will need to get the predicted values. To do that you need to run the cardiotox model and store the predictions. You can get cardiotox model implementation [here](https://github.com/atienosonia/ersilia_machine_learning/blob/master/cardiotex_implementation.py), download the file and store it in your Cardiotox folder, right after running ```python test.py```. go ahead and run ```python cardiotex_implementation.py```, this should store the predictions in your data folder, after which you can now proceed to producing the publication evaluation results. 


### [Project Task 3](#task3)

Validate a model in the wild, the dataset used was obtained from [DrugBank Data Library](https://weilab.math.msu.edu/DataLibrary/2D/)

### [License](#license)

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE.md) file for details

### [Resources](#resources)

* Read Ersilia's [documentation](https://ersilia.gitbook.io/ersilia-book)

### [Technologies Used](#technologies-used) 

- [ersilia](https://www.ersilia.io/) for creating the models.
- [RDKit](https://www.rdkit.org/) for preparation of chemical data.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) for visulizations.


