# 03

## Security best practices
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
12. Expose only required ports (mention docker IP tables)

Sum up:
- use images you trust!
- read image instructions and manuals!
- protect the host!
- dont expose ports!

[https://snyk.io/blog/10-docker-image-security-best-practices/](https://snyk.io/blog/10-docker-image-security-best-practices/)  

[https://phoenixnap.com/kb/docker-security-best-practices](https://phoenixnap.com/kb/docker-security-best-practices)  

[https://docs.docker.com/engine/security/](https://docs.docker.com/engine/security/)


## Performance
- Docker is nearly identical to native performance and faster than KVM in every category
- The exception to this is Docker’s NAT (port mapping!)

**Docker isn't virtualization**, as such -- instead, **it's an abstraction on top of the kernel's** support for different process namespaces, device namespaces, etc.; one namespace isn't inherently more expensive or inefficient than another, so what actually makes Docker have a **performance impact is a matter of what's actually in those namespaces**.

![https://i.stack.imgur.com/4yRh1m.png](https://i.stack.imgur.com/4yRh1m.png)

![https://i.stack.imgur.com/2Ftytm.png](https://i.stack.imgur.com/2Ftytm.png)

![https://i.stack.imgur.com/wZZH6m.png](https://i.stack.imgur.com/wZZH6m.png)

https://stackoverflow.com/questions/21889053/what-is-the-runtime-performance-cost-of-a-docker-container

https://stackify.com/docker-performance-improvement-tips-and-tricks/

## CI/CD

CI/CD = Continuous integration and continuous delivery

**Continuous Integration (CI)** is a development practice that requires developers to **integrate code into a shared repository several times a day**. Each check-in is then **verified by an automated build**, allowing teams to detect problems early.

**Continuous Delivery (CD)** is the natural extension of Continuous Integration: an approach in which teams ensure that **every change to the system is releasable**, and that we can **release any version at the push of a button**. Continuous Delivery aims to make releases boring, so we can deliver frequently and get fast feedback on what users care about.

Once you have CI and CD in place, the **deployable unit path is called a pipeline**. 
A pipeline procedure **is triggered when code is committed** to a repository hosted somewhere like GitHub. Next comes notification to a **build system**. The build system compiles the code and **runs unit tests**.
Some pipelines also include automatic deployment (which is sometimes called Continuous Deployment) to a test/prod environment.

See examples...

# Secrets management

- [https://www.envkey.com/](https://www.envkey.com/)  
- [https://github.com/envkey/envkey-source](https://github.com/envkey/envkey-source)
- `envkey-source $ENVKEY_MASTERKEY --dot-env-compatible | sed "s/'//g" > .env`

# Logging

Local:

```
docker logs <container_id>
docker-compose logs <optional_container_id>
docker service logs <service_name> (from all nodes!)
```

JSON file with rotation:

```
logging:
  driver: json-file
  options:
    max-size: "10m",
    max-file: "3" 
  }
}
```

AWS logging:

```
logging:
  driver: awslogs
  options:
    awslogs-region: "eu-central-1"
    awslogs-stream: 'app'
```
Graylog

```
logging:
  driver: gelf
  options:
    gelf-address=udp://<some_host:12201
```


Applies to all docker concepts (not only swarm or docker-compose):

```
docker run -dit \
    --log-driver=gelf \
    --log-opt gelf-address=udp://<some_host:12201 \
    alpine sh
```

# GPU suppport

The NVIDIA Container Toolkit allows users to **build and run GPU accelerated Docker containers**. The toolkit **includes a container runtime library** and utilities to automatically configure containers to leverage NVIDIA GPUs.

- [https://github.com/NVIDIA/nvidia-docker](https://github.com/NVIDIA/nvidia-docker)


![https://cloud.githubusercontent.com/assets/3028125/12213714/5b208976-b632-11e5-8406-38d379ec46aa.png](https://cloud.githubusercontent.com/assets/3028125/12213714/5b208976-b632-11e5-8406-38d379ec46aa.png)
