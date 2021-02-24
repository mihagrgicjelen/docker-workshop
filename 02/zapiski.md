
# 02

- snemat!!!
- quick sum up, dockerfiles, docker build, docker run, docker-compose, volume mounts, exposing ports
- docker system prune
- security overview
- flask docker-compose
- split to DEV
- docker stats
- test dockprom to monitor it
- security overview exposed ports
	- nginx basic auth bypass then 8000 exposed
	- redis highjack publicly available to the internet

A Docker Swarm is a group of either physical or virtual machines that are running the Docker application and that have been configured to join together in a cluster. ... The activities of the cluster are controlled by a swarm manager, and machines that have joined the cluster are referred to as nodes. 


- swarm init
- swarm join
- swarm node ls
- docker stack deploy -c <compose_file> <stack_name>
- docker stack ls
- docker service ls
- docker service ps <service_name>
- play with healthchecks
- resources
- pass environs
- docker node update --label-add bar=baz node-1
- deploy on the two servers to see in prod!
- use swarmprom



## Security best practices

[https://snyk.io/blog/10-docker-image-security-best-practices/](https://snyk.io/blog/10-docker-image-security-best-practices/)  

[https://phoenixnap.com/kb/docker-security-best-practices](https://phoenixnap.com/kb/docker-security-best-practices)  

[https://docs.docker.com/engine/security/](https://docs.docker.com/engine/security/)

1. Prefer minimal base images (use multistage builds)
2. Least privileged user (default is root!)
3. Sign and verify images (*export DOCKER_CONTENT_TRUST=1*)
4. Find, fix and monitor for open source vulnerabilities
5. Don’t leak sensitive information to Docker images
6. Use fixed tags for immutability
7. Use COPY instead of ADD
8. Update Docker and Host Regularly
9. Configure Resource Quotas
10. Secure Registries
11. Don't Expose the Docker Daemon Socket
12. Expose only required ports (mention IP tables)


