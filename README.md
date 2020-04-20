# devops-exporter

[![Build Status](https://dev.azure.com/Menziess/azure-devops-pipeline-downloader/_apis/build/status/Menziess.azure-devops-pipeline-downloader?branchName=master)](https://dev.azure.com/Menziess/azure-devops-pipeline-downloader/_build/latest?definitionId=16&branchName=master)

## Introduction

This script can be used to export Azure DevOps pipelines.

## 1. Usage

1. Create a Personal Access Token with read access on the `Build` and `Release` scopes:
  ![](res/pat.png)
2. Copy the `.env.example` file to `.env`, and replace the token and organization url placeholders.
3. Run the main script as:
    ```sh
    # download release pipelines
    python main.py 'projectname' --release
    # download build pipelines
    python main.py 'projectname' --build
    # download build pipelines 1 and 2
    python main.py 'projectname' --build --ids 1 2
    ```
