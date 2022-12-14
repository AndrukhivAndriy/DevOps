# Script to convert nginx.log to csv and store it on GitHub

## INSTALL

We are using Python v3.9 or v3.10. Install it. See - [How to install Python](https://realpython.com/installing-python/)

First of all you must install PyGithub and PyYAML libraries. The best to do this is using *pip*. How to install see [how to install pip](https://pip.pypa.io/en/stable/installation/)

After *pip* installation type in command line commands to install libraries:

    pip install PyGithub
    pip install PyYAML
    
## Config script

Find file *config.yaml*. Type your parameters:

  **full_path_to_nginx_log: "nginx.log"**  -- instead **"nging.log"** type path to log file. Live it, if nging.log is in the same directory as script main.py
  
  **full_path_to_export_csv_file: "converted.csv"**  -- instead **"converted.csv"** type path to csv file. It will be created. Live it, file will be created in the same directory as script main.py
  
  **access_token: "ghp_b11111111111111111111111111"** -- token to access GitHub. How to create it see - [Create personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
  
  **repository_name: "USERNAME/REPO"**  --  repository name in GitHub
  
  **branch: "main"**  --  branch name
  
  ## Run script
  
  Type in command line:
  
      python main.py
      
  or
  
      python3 main.py

## Run via Docker

The easiest way is to put files: *main.py, nginx.log, config.yaml, Dockerfile* into one folder on server, where Docker installed. 

1. Build image: **docker build -t log_convert_csv .** (about 520MB)
2. Run: **docker run -t -i --volume /path/where/folder/is/located/:/data/ log_convert_csv**

## P.S.

You can find also nginx.log (as an example) and it's convertation to converted.csv. Nice viewer to see converted.csv you can find here [CSV viewer](https://www.convertcsv.com/csv-viewer-editor.htm)
