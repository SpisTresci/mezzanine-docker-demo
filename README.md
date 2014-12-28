mezzanine-docker-demo
=====================
[![nodesource/node](http://dockeri.co/image/noisy/mezzanine-docker-demo)](https://registry.hub.docker.com/u/noisy/mezzanine-docker-demo/)


     virtualenv mezzanine-docker-demo
     source mezzanine-docker-demo/bin/activate
     
     #pip install Mezzanine after merging PR, for now:
     pip install git+https://github.com/SpisTresci/mezzanine.git@docker_support
     pip install fig
     
     mezzanine-project example-project
     cd example-project/
     fig up

Your dockerized mezzanine instance should be available on [http://localhost/](http://localhost/) :tada:
