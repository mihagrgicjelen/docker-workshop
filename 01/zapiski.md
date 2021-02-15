# #1 - WRITING AND RUNNING SIMPLE DOCKER FILES

**Docker is a tool designed to make it easier to create, deploy, and run applications by using containers.** Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.
 
**In a way, Docker is a bit like a virtual machine. But unlike a virtual machine, rather than creating a whole virtual operating system, Docker allows applications to use the same Linux kernel** as the system that they're running on and only requires applications be shipped with things not already running on the host computer. This gives a **significant performance boost and reduces the size of the application**.

![https://docs.docker.com/engine/images/architecture.svg](https://docs.docker.com/engine/images/architecture.svg)


![https://miro.medium.com/max/492/1*MYX0ClbWoitxS0RNUVvj8A.png](https://miro.medium.com/max/492/1*MYX0ClbWoitxS0RNUVvj8A.png)


## Install

* [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)
* [https://docs.docker.com/engine/install/linux-postinstall/](https://docs.docker.com/engine/install/linux-postinstall/)

## Running first docker files

`docker run hello-world`
	
`docker build .`  
`docker run ?`  *running what?*  
`docker build -t nginx .  `  
`docker run nginx`  

`docker run python:3.7 python -c "import sys; print(sys.version)"`

`docker run python:2.7 bash -c "ls"`  

`docker run  jjanzic/docker-python3-opencv python -c "import cv2; print(cv2.__version__)"
4.5.0`

 *Se` vedno ne moremo dostopat*.  
`docker build -t nginx .; docker run nginx`


## Exposing ports
https://docs.docker.com/engine/reference/builder/#expose  

Dodamo EXPOSE 8000 v dockerfile  
`docker build -t nginx .; docker run nginx`

*Ugotovimo da se vedno ne moramo dostopat*  
`docker ps`

*Publish ports with -P (hmm...)*  
`docker build -t nginx .; docker run -P nginx`  
`docker ps`  

*Properly explicitely publish ports*
`docker build -t nginx .; docker run -p 8000:8000 nginx` 

## Mounting volumes
*Mount volumes for real time code updates*  
`docker run -v $(pwd)/templates:/usr/share/nginx/html:ro -p 8000:8000 nginx` 

*Bug mount napacnega voluma*  
`docker run -v /NONEXISTING:/usr/share/nginx/html:ro -p 8000:8000 nginx # ERROR`  
`docker run -v $(pwd)/templaTTTTTes:/usr/share/nginx/html:ro -p 8000:8000 nginx  # will not fail`


*open() "/usr/share/nginx/html/index.html" failed (2: No such file or directory)  
Kako debugiramo? Pogledamo 'v container' ali mount pravilno deluje*  

`docker ps`	
`docker exec -it <CONTAINERID> bash`	
`docker exec -it <CONTAINERID> ls /usr/share/nginx/html`
	
## Built image sizes
Spremeni base image v nginx:1.17.3-**alpine** in rebuild

```
docker image ls | grep nginx
nginx-alpine		21.2MB   
nginx				126MB
```

####Uporaba .dockerignore 

V ./templates odvrzi nakjucno veliko datoteko in znova pozeni build

```
cp <some_big_file_on_my_FS> ./templates
docker build -t nginx .  
# => transferring context: 136.42MB
docker image ls | grep nginx
```
	
* build time se poveca
* image size se poveca.
* ("*CI repo fetch*" time se poveca)
* mimogrede v sliko skopiras nezeljene stvari (`"COPY . . "` npr .env )

Tipicno se to zgodi, ko se v sliki znajdejo direktoriji .git, node_modules...  
Zato bodi natancen in ekspliciten pri uporabi `COPY` ukazov. V sliko skopiraj minilalno kar je potrebno!
Za 'excludanje' izjem, upodabi .dockerignore

```
echo "templates/<some_big_file_on_my_FS>" >> .dockerignore
docker build -t nginx .  
docker image ls | grep nginx
```
V branje:

* [Nekaj razlage o .dockerignore](https://codefresh.io/docker-tutorial/not-ignore-.dockerignore -2/)
* [.dockerignore  syntax & docs](https://docs.docker.com/engine/reference/builder/### -file)

## Using container registries
[https://docs.docker.com/registry/](https://docs.docker.com/registry/)

Gitlab > Start Project > Packages & Registries > copy CLI commands

```
docker login registry.gitlab.com

docker build -t <repository>/<tag>:<version>
docker build -t registry.gitlab.com/mihagrgicjelen/docker-workshop-test-registry/my-nginx:v1 .

docker push <repository>/<tag>:<version>
docker push registry.gitlab.com/mihagrgicjelen/docker-workshop-test-registry/my-nginx:v1
```
Always define image tags, dont use null or 'latest'


## Restart policies

[https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

```
no
on-failure
always
unless-stopped
```

```
docker run --restart on-failure redis /bin/bash -c "sleep 5; exit 0"
watch docker ps  # to monitor whats going on
```

## Commands

### Docker CLI
```
docker build -t <tag> -f <dockerfile> <context>
docker build -t the_might_nginx -f nginx.Dockerfile .

docker run <the_image> <command>
docker run --name <container_name> --network=<network_name> -p <external_port>:<internal_port> <image_name>

docker pull <public_image_name>:<version>
docker push <repository>/<tag>:<version>

docker exec <container_id> <command>
docker run <container_id> <command>

docker ps  # list running containers
watch docker ps
docker stop $(docker ps -q)  # stop all running containers
docker image ls
docker volume ls
docker network ls
docker stats
```


### .Dockerfile

- FROM
- ADD
- WORKDIR
- CMD
- COPY
- EXPOSE
- CMD
- ENTRYPOINT
- ARG
- ENV


# Docker-compose
[https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)  
[https://docs.docker.com/compose/](https://docs.docker.com/compose/)

```
alias stopall='docker stop $(docker ps -q)'  
alias dc='docker-compose'  
alias d='docker'  
alias dcdev='docker-compose -f docker-compose.yml -f docker-compose-DEV.yml'  
alias dcdevb='docker-compose -f docker-compose.yml -f docker-compose-DEV.yml -f docker-compose-BUILD.yml'  
```