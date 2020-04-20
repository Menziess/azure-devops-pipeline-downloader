# devops-exporter

## Introduction

This script can be used to export Azure DevOps pipelines.

## 1. Usage

1. Create a Personal Access Token with read access on the `Build` and `Release` scopes:
  ![](res/pat.png)
2. Copy the `.env.example` file to `.env`, and replace the token and organization url placeholders.
3. Run the main script.
