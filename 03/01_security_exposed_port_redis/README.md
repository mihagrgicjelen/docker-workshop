# FLASK BEHIND PROXY WITH COMPOSE

The goal is to display a dangerous docker-compose file. Can you spot the publicly exposed services? Run with

`docker-compose up`

Files docker-compose-FIXED.yml and docker-compose-FIXED-DEV.yml  will fix those problems.

For DEV:
`docker-compose -f docker-compose-FIXED.yml -f docker-compose-FIXED-DEV.yml up`

For PROD:
`docker-compose -f docker-compose-FIXED.yml up`

