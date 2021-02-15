
docker build -t the_might_nginx -f nginx.Dockerfile .

docker build -t the_might_flask -f flask.Dockerfile .


docker network create the_mighty_network

docker run --name app --network=the_mighty_network the_might_flask
docker run --network=the_mighty_network -p 8888:8888 the_might_nginx