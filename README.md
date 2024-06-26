# CIM Modeling Guide

![image](docs/images/media/image-header-1.png)

UCAIug CIM Modeling Guide, © 2019 - 2024. All rights reserved by the UCA International CIM Users Group

This repository hosts the publically available **CIM Modeling Guide** made available by the UCA International CIM Users Group. This official guide is managed and maintained by the CIM Model Management Team and can be viewed online [here](https://cim-mg.ucaiug.io/).

The final documentation published online is generated using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material).

## CIM Modeling Guide Discussion Forums

For general questions or discussions related to this UCAIug publication or specific rules therein please post directly to the [CIM Modeling Guide Discussion](https://github.com/cimug-org/cim-modeling-guide/discussions) forums for this repository.

## Submitting Issues
For any identified issues with this **CIM Modeling Guide** please submit them via the [CIM Modeling Guide Issues](https://github.com/cimug-org/cim-modeling-guide/issues) tracker. Be sure to add an appropriate "version" label on your issue (e.g. v1.1) corresponding to the publication version of the modeling guide.

## Contributing
To run the site locally use [Python](https://www.python.org/). This is cleanest if you use a Python virtual environment as shown below to install the dependencies.
```cmd
python -m venv venv
venv\Scripts\activate
pip install mkdocs-material mkdocs-with-pdf mike mkdocs-enumerate-headings-plugin
```
For exact (known working) versions of dependencies, run `pip install -r requirements.txt` instead.

Once installed, you can then run the documentation site locally with `mkdocs serve`
```cmd
mkdocs serve
```
You can view the site by navigating to http://localhost:8000 in your browser.

This project also publishes a PDF version of the site. The easiest way to generate the PDF is with the [Generate CIM Modeling Guide PDF](https://github.com/cimug-org/cim-modeling-guide/actions/workflows/generate-pdf.yml) GitHub Action. However, if you need to run it locally, first set the `ENABLE_PDF_EXPORT` environment variable then run the build command.

```cmd
set ENABLE_PDF_EXPORT=1
mkdocs build
```
The output will indicate the PDF file location.

## Publishing
This project gets published to the https://cim-mg.ucaiug.io site. The easieset way update the site is with the [Publish website](https://github.com/cimug-org/cim-modeling-guide/actions/workflows/publish-site.yml) GitHub Action.

You can also publish manually as described below. Under the hood the project is using [GitHub Pages](https://pages.github.com/) to host the site which effecitvely just stores the site content in a dedicated git branch called `gh-pages`. It uses the [mike](https://github.com/jimporter/mike) plugin to publish multiple versions.

Update a version in the `gh-pages` branch using the `mike deploy [version]` command. This will replace the existing version of the documentation on the `gh-pages` branch with whever the currently checkout version is and give it a label of `[version]`. So for example to publish a new version of 1.0 you first want to pull the latest published changes down from the remote
```cmd
git remote add upstream https://github.com/cimug-org/cim-modeling-guide
git fetch upstream
git switch gh-pages
git pull upstream gh-pages
```
Then switch to the branch you want to update and run the deploy command giving it the verion name you want, for example let's say we're going to publish version "1.0" which is in branch "v1.0".
```cmd
git switch v1.0
git pull upstream v1.0
mike deploy 1.0
```

When you need to update which version is considered the "latest" (e.g. when going from 1.0 to 2.0) run the following
```cmd
mike deploy 2.0 latest --update-aliases
```
Note that mike will always update the version and any aliases ("latest") when you run a `mike deploy [version]` command. So you only need to do the `mike deploy [version] latest --update-aliases` when the latest version is changed.

To view the site locally before publishing it to https://cim-mg.ucaiug.io, run
```cmd
mike serve
```
Then to publish it to https://cim-mg.ucaiug.io, you will want to push your local `gh-pages` branch to the remote https://github.com/cimug-org/cim-modeling-guide repo using
```cmd
mike deploy 1.0 --push --branch gh-pages --remote upstream
```

Refer to [mike documentation](https://github.com/jimporter/mike) for more information.