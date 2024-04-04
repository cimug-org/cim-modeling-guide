# CIM Modeling Guide

![image](docs/images/media/image-header-1.png)

UCAIug CIM Modeling Guide, © 2019 - 2024. All rights reserved by the UCA International CIM Users Group

This repository hosts the publically available **CIM Modeling Guide** made available by the UCA International CIM Users Group. This official guide is managed and maintained by the CIM Model Management Team and can be viewed online [here](https://cim-mg.ucaiug.io/).

The final documentation published online is generated using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material).

## CIM Modeling Guide Discussion Forums

For general questions or discussions related to this UCAIug publication or specific rules therein please post directly to the [CIM Modeling Guide Discussion](https://github.com/cimug-org/cim-modeling-guide/discussions) forums for this repository.

## Submitting Issues
For any identified issues with this **CIM Modeling Guide** please submit them via the [CIM Modeling Guide Issues](https://github.com/cimug-org/cim-modeling-guide/issues) tracker. Be sure to add an appropriate "version" label on your issue (e.g. v1.1) corresponding to the publication version of the modeling guide.

## Offline Viewing
There are two options for offline viewing of the latest CIM Modeling Guide. You can download the latest release of the PDF of the CIM Modeling Guide at [releases](https://github.com/cimug-org/cim-modeling-guide/releases). 

Alternatively, to serve the modeling guide locally as a live-reloading web page, use [Docker](https://www.docker.com/) or [Python](https://www.python.org/).

For Docker, do `docker pull squidfunk/mkdocs-material` then `mkdocs serve` is default command so you can just do the following from repo root to start the site:

    docker run --rm -it -p 127.0.0.1:8000:8000/tcp -v %CD%:/docs squidfunk/mkdocs-material

For Python, do `pip install mkdocs-material` then once installed, the basic commands are:

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site (for deployment).
* `mkdocs -h` - Print help message and exit.

Once you have it running with either Docker or Python, you can view it by navigating to http://localhost:8000 on your browser.
