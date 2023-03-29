# Workflow

## cmemc

- example: cmemc -c dinobbio.eccenca.dev graph export http\://www.coconut-kg.aksw.org/data/ --output-dir coconut-kg --mime-type text/turtle

## virtuoso:

- https://hub.docker.com/r/tenforce/virtuoso/ (here you'll finde every information needed)

- example: docker run --name nubbe-virtuoso --restart unless-stopped -p 8892:8890 -p 1112:1111 -e SPARQL_UPDATE=true -e DEFAULT_GRAPH=http://nubbe-kg.aksw.org/data/ -v /home/schmidt/nubbe_docker/data:/data -d tenforce/virtuoso
