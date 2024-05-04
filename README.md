# TRS-CORE

TRS-CORE is a monorepo, which currently includes only a single project `icd`, 
combining apps - `inventories`, `companies`, `documents`. 

### Software versions
 - Python version used is **3.12.1**
 - Django version used is **5.0.x**


### Package Manager

The package manager we use is **PIP**
While currently we're only have a single project, 
`requirements.txt` is a single file located at the root of `TRS-CORE` project, 
that can be used to install dependencies using `PIP` package manager.


### Docstrings

```
"""
Text here.

:param something: Explanation of param.
:return: What it returns.

:raises SomeException: Explanation of exception. 
"""
```

Note that `param`, `return` and `raises` are optional and should be present only if applicable.

# Local setup

## Prerequisites

### Required Software

The only requirement for current stage is to have corresponding Python version installed on your local machine.

## IDE Setup

We use Pycharm, as it supports well tools we need to integrate for our IDE.

### Configuration examples for Pycharm Watchers

  Ruff
    - Arguments: `$FileDir$ --fix`
  
  Black
    - Arguments: `$FilePath$ --line-length=159`
  
## Build and run the app

Install `requirements.txt` and run `python manage.py runserver`,
Or configure IDE to run project from IDE runner.

# Functions naming rules

- Service functions that returns entities must start with `fetch_`
- Repository functions that returns entities must start with `get_`
- Repository functions that create entity must start with `create_`
- Repository functions that update entity must start with `update_`
- Repository functions that delete entity must start with `delete_`
- Functions that transform one type to another must start with `generate_`

