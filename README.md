# tiernan
python cherrypy ssl scanner using sslscan

- Build alpine sslscan docker container:

  docker build -t sslscan:latest -f Docker/Dockerfile.sslscan .
- Build alpine tiernan docker container:

  docker build -t tiernan:latest -f Docker/Dockerfile.tiernan .
  
- Run sslscan:

  docker run --rm sslscan www.google.com
  
- Run tiernan:

  docker run --rm -it -p 5000:5000 tiernan:latest
  
