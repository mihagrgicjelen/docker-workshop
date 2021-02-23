TODO: resources
for i in 1 2 3 4; do while : ; do : ; done & done <-- for stress

## Security best practices

[https://snyk.io/blog/10-docker-image-security-best-practices/](https://snyk.io/blog/10-docker-image-security-best-practices/)
[https://phoenixnap.com/kb/docker-security-best-practices](https://phoenixnap.com/kb/docker-security-best-practices)
[https://docs.docker.com/engine/security/](https://docs.docker.com/engine/security/)

1. Prefer minimal base images
2. Least privileged user
3. Sign and verify images (*export DOCKER_CONTENT_TRUST=1*)
4. Find, fix and monitor for open source vulnerabilities
5. Don’t leak sensitive information to Docker images
6. Use fixed tags for immutability
7. Use COPY instead of ADD
8. Use metadata labels
9. Use multi-stage build for small and secure docker images
10. Update Docker and Host Regularly
11. Configure Resource Quotas
12. Secure Registries
13. Don't Expose the Docker Daemon Socket


## Monitoring

### stats

### Dockprom

## Swarm

docker swarm init
docker swarm join

TODO:
swarmprom

