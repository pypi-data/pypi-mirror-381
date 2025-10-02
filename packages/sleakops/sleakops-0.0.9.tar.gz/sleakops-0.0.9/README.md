# How to install

Generate environment file

`
cp local.env .env
`

## Run a build

`
docker compose run cli python sleakops.py build --project core --branch qa --wait
`

### Build with environment specification

When you have multiple projects with the same branch, you can specify the environment to differentiate between them:

`
docker compose run cli python sleakops.py build --project core --branch qa --environment production --wait
`

## Run a deployment

`
docker compose run cli python sleakops.py deployment --project core --branch qa --wait
`

### Run help

`
docker compose run cli python sleakops.py --help 
`