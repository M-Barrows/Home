# Code And Coffee Blog
This is the main repo that I use to update my personal blog at [https://codecoffee.org](https://blog.codecoffee.org).

How to build the site
```bash 
docker run --rm -it `
  --volume="${PWD}:/srv/jekyll" `
  --volume="${PWD}/vendor/bundle:/usr/local/bundle" `
  -p 4000:4000 jekyll/jekyll:4 `
  jekyll serve
```
How to create/update docker image
```bash
docker build -t blog:latest .
```

How to publish the docker image
```bash
docker tag blog:latest codecoffee/blog:latest
docker push blog:latest
```

https://plainenglish.io/blog/how-to-create-custom-nginx-docker-image