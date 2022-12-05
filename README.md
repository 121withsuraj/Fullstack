
# CT SCAN IMAGE CLASSIFICATION

The given Dataset contains 1251 CT Scan of SARS-CoV2 infection (Covid19)
And 1229 CT Scan Non-Infected by SRAS-CoV2. Collected from real patients in hospitals .



## Deployment

The deep neural model is build in google colab , and the front end and Deployment is done in vs code studio.
It is deployed and tested in local server , also can be deployed on AWS or AZURE or any other cloud platform.  




## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Capstone Project
```

Install dependencies


FIRST METHOD: Run under a Virtual Environment

Open windows Powershell or Anaconda Prompt
```bash
  1. python -m venv venv(any name can be given).
```
```bash
  2. .\venv\Scripts\activate
```
```bash
  3. pip install -r requirements.txt
```


SECOND METHOD: Run in a Local Machine

 Open windows Powershell or Anaconda Prompt
 or from the terminal of the code editor. (in my case VS code)

```bash
  pip install -r requirements.txt
```

Start the server

Open windows Powershell or Anaconda Prompt
 or from the terminal of the code editor. (in my case VS code)
```bash
  python app.py
```

or can run from the inbuild program run button in code editor.
## Demo

Demo video is attached within the directory.


## Remarks

If got any error while running in local machine instead of in a virtual environment, make sure the all the libraries installed with the mentioned version.
In that case just uninstall the module

```bash
  pip uninstall (modulename)
  Ex:pip uninstall numpy
```
Again install the module with mentioned version

```bash
  pip install (modulename + version)
  Ex:pip install numpy==1.23.5
```


---------------------------THANK YOU-------------------------------