# CIM Modeling Guide
UCAIug CIM Modeling Guide, © 2019 - 2023. All rights reserved by the UCA International CIM Users Group

This repository hosts the publically available **CIM Modeling Guide** made available by the UCA International CIM Users Group. This official guide is managed and maintained by the CIM Model Management Team and can be viewed online [here](https://cim-mg.ucaiug.io/).

## Contributing
CIM Modeling Guide is documented using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material). If you need to do work on the CIM Modeling Guide you can do so by editing the files directly in the `docs` folder of this repo. 

To serve the guide locally as a live-reloading web page, use [Docker](https://www.docker.com/) or [Python](https://www.python.org/).

For Docker, do `docker pull squidfunk/mkdocs-material` then `mkdocs serve` is default command so you can just do the following from repo root to start the site:

    docker run --rm -it -p 127.0.0.1:8000:8000/tcp -v %CD%:/docs squidfunk/mkdocs-material

For Python, do `pip install mkdocs-material` then once installed, the basic commands are:

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site (for deployment).
* `mkdocs -h` - Print help message and exit.

Once you have it running with either Docker or Python, you can view it by navigating to http://localhost:8000 on your browser.