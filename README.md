<h1 align="center">wordle-collab</h1>
</p>
<p align="center">
<a href="https://github.com/douglasedurocha"><img title="Author" src="https://img.shields.io/badge/Author-douglasedurocha-blue.svg?style=for-the-badge&logo=github"></a>
</p>

<p align="center">API for Online Collaborative Wordle<br>using <em>Django Rest Framework</em> and <em>WebSockets</em></p>

Looking for front-end? https://github.com/douglasedurocha/wordle-collab-Frontend

## Clone this project

```bash
> git clone https://github.com/douglasedurocha/wordle-collab.git
> cd wordle-collab
```

## Dependencies:

+ [Poetry](https://python-poetry.org) : a tool for dependency management and packaging in Python.
+ [Docker](https://www.docker.com/) : a containerization platform for building, packaging, and distributing applications.
+ [Docker Compose](https://docs.docker.com/compose/) : a tool for defining and running multi-container Docker applications.

## Usage (development)

Copy .env file

```bash
> cp .env.example .env
```


Start Postgres and Redis service

```bash
> make up-dependencies-only
```

Install the projects requirements, apply the migrations and set up the git hook scripts
```bash
> make update
```

Start server

```bash
> make runserver
```


## API

### Auth Endpoints

<code style="color: green">POST</code>&nbsp; `/api/v1/accounts/register`
<br>
<code style="color: green">POST</code>&nbsp; `/api/v1/accounts/login`
<br>
<code style="color: green">POST</code>&nbsp; `/api/v1/accounts/logout`
<br>
<code style="color: aqua">GET</code> &nbsp; `/api/v1/accounts/user`

### Wordle Endpoints


<code style="color: aqua">GET</code> &nbsp; `/api/v1/games`
<br>
<code style="color: green">POST</code>&nbsp; `/api/v1/games`
<br>
<code style="color: aqua">GET</code> &nbsp; `/api/v1/games/<int:game_id>`
<br>
<code style="color: aqua">GET</code> &nbsp; `/api/v1/games/<int:game_id>/attempts`


Full API docs https://app.swaggerhub.com/templates-docs/DOUGLASEDUROCHA/wordlecollab/1.0.0


## Copyright Notice

This work incorporates words_dictionary.json in <em>words_list.json</em> file, obtained from https://github.com/dwyl/english-words/blob/master/words_dictionary.json.

Copyright (c) 2017-2023, Do What You Love
https://github.com/dwyl



