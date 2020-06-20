# Custom CMS for ketzu.net

This is a hobby Django project to realise a custom CMS for my webpage [ketzu.net](https://ketzu.net).

## Overview

This project is split into 6 django Apps to represent various different but independent parts:

 * photography: Photo galleries and a gallery overview.
 * science: Simple list of published papers with file storage for the pdfs.
 * medium: A blog like list of medium articles, although it could link to any external source.
 * videography: A list of embedded youtube videos with a title and description.
 * projects: A list of projects with optional github and project links.
 * web: A front page with a personal picture, description and favorites of the previous 5 apps.

The project uses a sqlite database, as the limitation of single writer is easily solved on a personal website.
This has additional advantages for deployment. 

## Deployment

For ease of testing the project, the project contains a dockerfile to build a container image hosting the site.
The project is built into a docker container on [dockerhub](https://hub.docker.com/repository/docker/ketzu/knet) on push and can be pulled from there as ketzu/knet.
The container will run migrations on before starting gunicorn.

Media files will need to be served through a different container.