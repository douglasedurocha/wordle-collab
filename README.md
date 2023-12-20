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

Start Postgres and Redis service

```
> make up-dependencies-only
```

Install the projects requirements, apply the migrations and set up the git hook scripts
```bash
> make update
```

Start server

```
> make runserver
```


## API

### Auth Endpoints

* `/api/accounts/register`
* `/api/accounts/login`
* `/api/accounts/logout`
* `/api/accounts/user`

### Wordle Endpoints

* `/api/games/create`
* `/api/games/list-open`
* `/api/games/<int:game_id>`
* `/api/games/<int:game_id>/attempts`

<!-- ## Features

|| Features |
| :-: | - | -->

## Copyright Notice

This work incorporates words_dictionary.json in <em>words_list.json</em> file, obtained from https://github.com/dwyl/english-words/blob/master/words_dictionary.json.

Copyright (c) 2017-2023, Do What You Love
https://github.com/dwyl



