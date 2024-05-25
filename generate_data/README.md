# DUMMY DATA

### Contents:

The DUMMY DATA required for this project where generated using the [Jupyter Notebook](https://jupyter.org/) app through [Anaconda Prompt](https://docs.anaconda.com/free/anaconda/getting-started/index.html), using [Python](https://www.python.org/) programming language.

### Installation:

```bash
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
curl -O https://repo.anaconda.com/archive/Anaconda3-https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh-Linux-x86_64.sh
source <PATH_TO_CONDA>/bin/activate
conda init
```

Having installed conda, open the anaconda prompt and run the following command in order to install all the necessary libraries:

```bash
pip install --lib_name
```
where lib_name is the name of the library, e.g. lib_name = numpy.
All the necessary libraries are included in the header of files create_dummy_data.py and dummy_data.py.

### Usage:
In order to fill `mydb` with data, you can create new data by running script [create_dummy_data.py]. There are already generated .csvcsv files in the generated_data folder.
Whether new files are generated, or the existing ones are used, the .csv files should be placed in directory [C://xampp/mysql/data/mydb].
Afterwards, run script [dummy_data.py]. The data should be successfully inserted into the DB.