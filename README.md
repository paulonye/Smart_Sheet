# Smart_Sheet
>In this project, a google service account will act as an enabler and connector in building a simple Extract, Transform, and Load Pipeline.
>
>The project involves scraping and transforming the data from yahoo finance using `Python`, storing the data on `Google Sheets`, and then visualizing the data using `Google Data Studio`.
>
>The Project is part of my "Building your first Google Cloud Analytics Project"
>
>[Link to the Yahoo Finance Website](https://finance.yahoo.com/crypto/?.tsrc=fin-srch&offset=0&count=15)
>
>[Link to the Medium Article](https://medium.com/@nwosupaul141/building-an-etl-pipeline-using-google-service-accounts-85e2a6cfd94d) 

## Project Structure

- Set up of Compute Engine Instance
- Installation of Anaconda
- Installation of Google Chrome and the Chrome Driver
- Installation of D
- Undestanding the Components of the Scripts
- Installing Required Libraries
- Running the Python script
- Running the Cronjob

![Cover_Image](https://storage.googleapis.com/images-xlr1001/cover.png)
 
## Set up of Compute Engine Instance
The project was built using a virtual machine, for set up; please refer to: 

## Installation of Anaconda
Go to the anaconda’s download page, look for the linux version, and then copy the link address. On the terminal of the instance, you can then use wget ‘the link address’ to download anaconda just as seen in the command below. The installation of anaconda would automatically lead to the installation of python 3 as well as jupyter notebook.

```bash
    wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```
The above command installs anaconda on the virtual machine; the ff command is then used to install it:
```bash
   bash Anaconda3-2022.10-Linux-x86_64.sh
```
You might need to restart the instance before. To test that anaconda was installed properly.
```bash
   conda --version
```
You can then launch jupyter notebook
```bash
   jupyter notebook
```
To close down the jupyter notebook, press Ctrl+D on windows, CMD+D on mac

## Installation of Google Chrome and the Chrome Driver

## Installation of Docker
Docker will help us package your application and all it dependencies into a container in which we can then deploy. To install docker use
```bash
   sudo apt-get install docker.io
```
Check the version you installed using `docker —version`

In other to ensure that docker runs without sudo;check the [link](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md)

Now try; `docker run hello-world`	
In this case; hello-world is a docker image. In the case you don’t have the docker image locally, docker pulls the image from the docker registry and builds the container on your local machine.

## Understand the Python Scripts
```
main.py: This python script is used to extract the data from Yahoo Finance. It uses selenium and beautiful soup which are bith web scraping tools to pull the data from the website and save it as a python dataframe
```
```
sheet_connect.py: This python script contains the functionality that sets up the connection from Python to Google Sheet. 
```
```
send_mail.py: This python script was set up for logging and error management.It contains funtionalities that informs us when the pipeline breaks, and what caused the break.
```
```
push.py: This python script was used to push the first batch of data from yahoo finance to google sheet. It is mainly used to test if the connection between python and the google sheet actually works.
```
```
push_append.py: This is the python script that combines the functionality of all the other scripts. The other scripts are imported as modules, and their various functionalities are combined towards ensuring that the data is scraped, transformed, and transfered to google sheet.
```

## Installing Required Libraries
The requirements.txt file contains all the libraries that are used for the project. It was generated after the completion of the projects using `pipreqs`. 
```bash
   pip install -r requirements.txt
```

## Running the Python script
From your working directory; use the command below 
```bash
   python3 push_append.py
```
## Setting up the CronJob
This is one of the major reasons, we are using a google cloud virtual image, we want to be able to run the pipeline every minute.
To set the cronjob, open the crontab using the command below:
```bash
   crontab -e
```
Scroll down and then input this command as seen below:
```bash
   * * * * * export key_file=/home/macbook/.service_accounts_keys/name_of_service_account_key.json; /home/macbook/anaconda3/bin/python3 ~/Smart_Sheet/push_append.py
```
The command above instructs our machine to run the append.py using the python from the anaconda installation directory. An environmental variable is also passed as this is a dependency for the python script to run successfully.

When running cronjobs, it is very important to use the absolute path of all files and resources involved. There are some exceptions.

