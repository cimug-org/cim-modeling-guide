# CIM Modeling Guide

![image](docs/images/media/image-header-1.png)

UCAIug CIM Modeling Guide, © 2019 - 2024. All rights reserved by the UCA International CIM Users Group

This repository hosts the publically available **CIM Modeling Guide** made available by the UCA International CIM Users Group. This official guide is managed and maintained by the CIM Model Management Team and can be viewed online [here](https://cim-mg.ucaiug.io/).

The final documentation published online is generated using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material).

## CIM Modeling Guide Discussion Forums

For general questions or discussions related to this UCAIug publication or specific rules therein please post directly to the [CIM Modeling Guide Discussion](https://github.com/cimug-org/cim-modeling-guide/discussions) forums for this repository.

## Submitting Issues
For any identified issues with this **CIM Modeling Guide** please submit them via the [CIM Modeling Guide Issues](https://github.com/cimug-org/cim-modeling-guide/issues) tracker. Be sure to add an appropriate "version" label on your issue (e.g. v1.1) corresponding to the publication version of the modeling guide.

To run the site locally use [Python](https://www.python.org/). This is cleanest if you use a Python virtual envirnment as shown below to install the dependencies.
```cmd
python -m venv venv
venv\Scripts\activate
pip install mkdocs-material mkdocs-pdf-export-plugin mike mkdocs-enumerate-headings-plugin
```

Once installed, you can then run the documentation site locally with `mkdocs serve`
```cmd
mkdocs serve
```
You can view the site by navigating to http://localhost:8000 in your browser.

### Publishing
This project uses the [mike](https://github.com/jimporter/mike) plugin to publish multiple versions of the documentation to the https://cim-mg.ucaiug.io site. Under the hood it is using [GitHub Pages](https://pages.github.com/) to host the site which effecitvely just stores the site content in a dedicated git branch called `gh-pages`. 

You deploy using the `mike deploy [version]` command. This will replace the existing version of the documentation on the site with whever the currently checkout version is. So for example to publish a new version of the documentation to the https://cim-mg.ucaiug.io site you first want to pull the latest published changes down from the remote site
```cmd
git remote add origin https://github.com/cimug-org/cim-modeling-guide
git fetch origin
git switch gh-pages
git pull origin gh-pages
```
Then switch to the branch you want to publisha and run the deploy command giving it the name you want, for example let's say we're going to publish version "1.0" which is in branch "v1.0".
```cmd
git checkout v1.0
mike deploy 1.0
```

When you need to update which version is considered the "latest" (e.g. when going from 1.0 to 2.0) run the following
```cmd
mike deploy -u 2.0 latest
```
Note that mike will always update the version and any aliases (latest) when you run a `mike deploy [version]` command. So you only need to do the `mike deploy -u [version] latest` when the latest version is changed.

To view the site before publishing it to https://cim-mg.ucaiug.io, run to view it locally
```cmd
mike serve
```
Then to publish it to https://cim-mg.ucaiug.io, you will want to push your local `gh-pages` branch to the remote https://github.com/cimug-org/cim-modeling-guide repo (or push it to a fork and submit a pull request to the upstream repo)
```cmd
git push origin gh-pages
```

Refer to [mike documentation](https://github.com/jimporter/mike) for more information.