# README

访问Docker容器内部的Flask

## 参考文档

* [Build your Python image](https://docs.docker.com/language/python/build-images/)

## BuildKit

* DOCKER_BUILDKIT=1 docker build .
* docker build -t networkips:1.0 . -f Dockerfile
  * 省略点的写法
    * docker build -t networkips:1.0 .

## port

* 5000
