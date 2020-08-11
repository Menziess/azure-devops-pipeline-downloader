# devops-exporter

[![Build Status](https://dev.azure.com/Menziess/azure-devops-pipeline-downloader/_apis/build/status/Menziess.azure-devops-pipeline-downloader?branchName=master)](https://dev.azure.com/Menziess/azure-devops-pipeline-downloader/_build/latest?definitionId=16&branchName=master)

## 1. Introduction

This script can be used to export Azure DevOps pipelines.

## 2. Usage

1. Create a Personal Access Token with read access on the `Build` and `Release` scopes:
   ![](res/pat.png)
2. Copy the `.env.example` file to `.env`, and replace the token and organization url placeholders.
3. Download the [.whl](https://dev.azure.com/Menziess/d290f987-6082-4a6e-bffd-29c716197025/_apis/build/builds/239/artifacts?artifactName=devops-exporter.whl&api-version=5.1&%24format=zip)
4. Install the `.whl` file in a virtual environment (or globally if you prefer)
   ```zsh
   pip install *.whl
   ```
5. Run the main `.whl` as:
   ```zsh
   # download build pipelines using installed .whl console script
   devops_exporter 'projectname' --build
   # download build pipelines using .whl
   python -m devops_exporter.main 'projectname' --build
   ```
6. (Alternatively) run code directly as:
   ```zsh
   # download release pipelines using python code directly from repo
   python main.py 'projectname' --release
   # download build pipelines
   python main.py 'projectname' --build
   # download build pipelines 1 and 2
   python main.py 'projectname' --build --ids 1 2
   ```
