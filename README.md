# Sale Manager
An online bookstore project.

### Prerequisites
- Local deployment/development:
  - make (if you're using Linux)
  - Docker 18.09
  - docker-compose 1.22

If you don't have `Docker` and `docker-compose` installed on your machine then you have to manually install the following tools on your machine:
- Database: Postgres 11.4
- Backend service: 
  - Python 3
  - pip3, venv
- Frontend service: 
  - NodeJS: 10.6
  - yarn

### Development
If you have `Docker` and `docker-compose` installed on your machine then just have to run the below commands.  
`docker-compose` will start all required services for local development with live reloading for both `frontend` and `backend` services.
```sh
$ cd deployment/
$ docker-compose up

or just have to run `make docker-compose` if you're using Linux and have make tool installed.
```

Services will be started and exposed at address:
  - Database: `postgres:5432` (+pgAdmin: `0.0.0.0:10000`)
  - Backend: `backend:9090`
  - Frontend: `frontend:8080`
  - NGINX proxy: `0.0.0.0:80`  
  
After that, you can open your browser and head to `http://localhost` to see the webpage.

*Note: In case, you're using Windows or don't have `Docker` and `docker-compose` installed, then you will have to manually install all the tools in the `Prerequisites` section above and start each service by yourself.*  
*You can reference to the `setup-env`, `fe-start-dev` and `be-start-dev` profiles in the `Makefile` to know which commands must be run in order to manually setup the local development environment.*


### Database management
- After start the local environment by `docker-compose`, you can access `pgAdmin` at `http://localhost:10000`.
- Email/Password: `admin@local.dev` / `123456x@X`
- Create new connection to Postgres database with details below:
  - Hostname/Address: `postgres`
  - Port: `5432`
  - Username: `postgres`
  - Password: `123456x@X`

### LICENSE
This project is under the MIT License.
