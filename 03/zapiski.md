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

https://stackoverflow.com/questions/21889053/what-is-the-runtime-performance-cost-of-a-docker-container

https://stackify.com/docker-performance-improvement-tips-and-tricks/

## CI/CD

CI/CD = Continuous integration and continuous delivery

**Continuous Integration (CI)** is a development practice that requires developers to **integrate code into a shared repository several times a day**. Each check-in is then **verified by an automated build**, allowing teams to detect problems early.

**Continuous Delivery (CD)** is the natural extension of Continuous Integration: an approach in which teams ensure that **every change to the system is releasable**, and that we can **release any version at the push of a button**. Continuous Delivery aims to make releases boring, so we can deliver frequently and get fast feedback on what users care about.

Once you have CI and CD in place, the **deployable unit path is called a pipeline**. 
A pipeline procedure **is triggered when code is committed** to a repository hosted somewhere like GitHub. Next comes notification to a **build system**. The build system compiles the code and **runs unit tests**.
Some pipelines also include automatic deployment (which is sometimes called Continuous Deployment) to a test/prod environment.


- Start a Gitlab Repository
- Copy from 01 - django app
- push to repo
- SSH to prepared server
- install gitlab runner
- rm .bash_logout
- add gitlabrunner to docker group
- install git
- expect postgress first fail



