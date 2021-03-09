# 02 ADVANCING DOCKER-COMPOSE, DOCKER SWARM


## Advancing docker compose

### Chaining compose files
```
docker-compose <command>  (defaults to -f docker-compose.yml)`
```

Usually we write 'production ready' compose files and we place development specifics to a separate compose file. Then we chain the 'base' file with 'overides' file.

```
docker-compose -f <docker-compose.yml> <command>
docker-compose -f docker-compose.yml -f <docker-compose-DEV.yml <command>
```

Inspect the 'resulting' docker-compose definitions with

```
docker-compose -f docker-compose.yml -f <docker-compose-DEV.yml config
```

### SWARM

A Docker Swarm is a group of either physical or virtual machines that are running the Docker application and that have been **configured to join together in a cluster**. ... The **activities** of the cluster **are controlled by a swarm manager**, and machines that have **joined** the cluster are referred to as **nodes**. 

(prepare at least two servers/virtual machines with basic docker and docker-compose install)

Following command creates a new swarm with 'self' as the manager node:   
`docker swarm init`

'Slave' nodes can join the swarm with the following command:   
`docker swarm join --token <token> <host>`   

From now on, all the commands should be executed from the manager node. We never interact directly with the 'slave' nodes (unless for debugging)

Check list of nodes in the swarm   
`swarm node ls`

Let's meet the new entities and commands   
- **docker service** is used when managing individual service on a docker swarm cluster   
- **docker stack** can be used to manage a multi-service application on a swarm cluster

When we have a ready docker-compose file, the deployment to Swarm is short.   

- make sure to use images (pre-build, upload to container registry) and not build definitions

Deploy the application using   
- `docker stack deploy -c <compose_file> <your_whatever_stack_name>`

Then observe the situation using:

- `docker stack ls`  
- `docker service ls`  
- `docker service ps <service_name>`
- `docker ps`  

You can also 'sneak' to one of the slave nodes and exec. `docker ps`. You should see running containers - orchestrated by the swarm manager. You can try to kill the container (`docker stop <container_id>`). The manager will try to restart it.
  
In order for swarm manager to successfully orchestrate all the required containers, you should get familiar with:
_________________
**Healthchecks test if the process running inside the container is healthy**. Inmagine a single-threaded web server stuck in a 'while True' loop for ever. From docker's perspective, everyting looks fine, but  the web server is actually not able to serve requests. With healthchecks, we can address that kind of issues (memory leaks, network problems...). Swarm manager will try to fix the situation automatically (restart the container, run the container on a different node, etc...)
 
```
healthcheck:
    test: curl http://localhost:8000  # docker assumes 'healty' if command exit code is 0!
    interval: 5s
    timeout: 2s
    retries: 1
    start_period: 1s  
```

_________________
We can easily **replicate** services inside a stack and leave load-balancing to the Swarm manager.
Inmagine a web scraping app. There is a master service with the UI, database etc. There is also a 'worker' service which is designed to scrape some web content every hour, which takes a long time. Typically with Django we use Celery as the worker and Celery Beat as the scheduller. With replicas is easy to 'spawn' more workers when needed, to acquire the results faster.

```
celery-worker:
  ...
  deploy:
    replicas: 4

docker stack deploy -c docker-compose.yml my_scraper
```

When we need more resources, we would.
- Create new virtual machines (AWS, Scaleway...easy to do programatically)
- Execute swarm join commands (AWS, Scaleway...easy to do programatically)

```
celery-worker:
  ...
  deploy:
    replicas: 25

docker stack deploy -c docker-compose.yml my_scraper  # will update the curren stack (scale-up)
```
_________________
**Resource limits are a robust method to prevent a container to 'eat up' all the available resources** Let's inmagine a process (in a container) with a memory leak, running on a server alongside multiple other services. Eventually the rogue process will consume all available resources (typically memory) and put all services on the given host offline.   
With *resorce limits* section, we limit maximum allowed resources per service. The rogue processes with memory leaks will eventually be restarted by swarm orchestrator (and the leaked resources are freed).

```
deploy:
  resources:
    limits:         # for a short time (spikes) allow up to this limit
      cpus: '0.50'
      memory: 150M
    reservations:   # generally allow up to this limit
      cpus: '0.25'
      memory: 130M
```
_________________
In swarm mode, its easy to control where a given service should be **placed**. Maybe the database should be at a strictly defined server. Maybe some part of the application is GPU based and requires a server with a GPU.

```
deploy:
  placement:
    constraints:
      - "node.role==manager"
      - "engine.labels.operatingsystem==ubuntu 18.04"
      - "node.labels.region==EU"  # see the following command in order to use
```
(`docker node update --label-add region=EU <node_id>`)
_________________



