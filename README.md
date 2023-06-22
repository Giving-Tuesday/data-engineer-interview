# data-engineer-interview
## Giving Tuesday Data Engineer Technical Interview Exercise

The goal of this exercise is to aggregate some raw volunteering data from 3 different providers into a single dataset by implementing an ETL pipeline.

You have been given a Jupyter notebook `notebooks/Volunteer Data Cleaning.ipynb` which already implements a pipeline but you should find ways to improve upon that implementation by refactoring the code into Python modules.

Here are the requirements:
* The source data for your pipeline are the CSV files in `data_lake/raw/2023/05`
* The destination for your aggregated data should be `data_lake/curated/2023/05/aggregated_volunteering_data.csv`
* The following command must be able to run the pipeline:
```
poetry run python -m etl.volunteering.aggregate_volunteering_data
```
* You must implement the `entrypoint` function in `etl.volunteering.aggregate_volunteering_data`
* You must use the `Task` class in `etl.common` at least once
* You cannot make changes to the `Task` class in `etl.common` 
* You should include at least one test for your pipeline in `tests`

### Poetry and Useful Commands

This repo uses [Poetry](https://python-poetry.org/) for dependency management. 

Here are some commands you may need to know:

``poetry install``: Installs project dependencies (defined in `pyproject.toml`)


``poetry add <package name>``: Adds package to project dependencies and installs it into the project's virtual environment


``poetry run python <path to your script>``
or
``poetry run python -m <module name>``: Runs your script in the virtual environment


``poetry run python -m pytest``: Runs tests in the virtual environment


``poetry shell`` and ``exit``: Activates virtual environment in a new shell