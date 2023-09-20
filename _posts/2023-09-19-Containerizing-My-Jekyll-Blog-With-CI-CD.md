---
title: Containerizing My Jekyll Blog
layout: post
date: '2023-09-18'
excerpt: "Tired of manually moving your Jekyll website's files to your production server? Try making it a Docker image!"
excerpt_separator:  <!--more-->
tags: 
    - Web Development
    - GitHub
    - Docker
    - CI/CD
    - Containers
    - Jekyll
    - Portainer
    - Watchtower
    - Home Lab

categories: 
    - Show And Tell
---

Recently I've been diving into the world of building a home lab. As someone who primarily writes application code, it's humbling to be working with hardware, networking, and other infrastructure. While I began my home lab journey hoping to build a perfect little production environment for all of my pet projects - I've quickly pivoted to a more true "_lab_" where I can experiment with new (to me) technology in a stress free place. 

One piece of tech that I've loved recently is Portainer. I've always liked the idea of Docker but never had the use case or environment available to explore its true benefits. That all changed with Portainer. Portainer provides you with a simple UI for creating/managing multiple docker containers and environments. This means that you can try out new products and destroy them when you're done without fear of altering your base environment. 

Additionally, I decided to take environment encapsulation to a level higher than Docker or Portainer alone by running Portainer on an Ubuntu VM that is itself running on a Proxmox node. The good thing about all these technologies is it makes the final environment (wherever in the ladder you land) largely very predictable. The downside is that networking, moving files, and ssh-ing into the correct "machine" is nothing short of a game of technological and mental twister for someone of my experience. 

And now, we get to the real reason for today's article. In my quest to host my website as "free" as I can (right now I pay $12/year for the domain and electricity costs for the host server) while also having as much control as I can over the technology stack underneath, I've been self-hosting my blog on my home lab. Once I made the switch from GitHub Pages to self-hosting however, pushing new updates to my blog was a nightmare! 

For instance, here are most of my steps needed to update my blog before Docker: 

1. Write new content 
2. Build Jekyll site
3. Test new site
4. Look up target server's IP, Username and Password
5. Look up where Nginx reads site files from __*again*__
6. rsync the site files over to the target server
7. commit changes to Github

However, now my steps look like this:
1. Write new content
2. Commit changes to Github
3. Relax

While the first way was fine (I'm just one person in their basement after all, not a $1B company) I knew there was a better way. This is where Docker, GitHub actions, Watchtower, and Portainer all come in! 

The basics of this improved workflow are as follows. Each time I make a commit to GitHub, I have a GitHub Action that 

1. Builds the Jekyll Site
2. Builds a Docker Image (Jekyll + Nginx)
3. Publishes the Docker Image to Docker hub

Then, on my server I have a Watchtower container (running on Portainer) listening for changes in that Docker Image. Each time it detects a change, it pulls the new image, starts it, and gracefully transitions between the new and old image. To me, this is mind-blowing 🤯. The fact that I can just make code changes, push them to a free version control system and have my self-hosted website update is just so cool! 

The best part (for you) is that all of this is open-source! You can find my blog's repo [here](https://github.com/M-Barrows/Home), the `yaml` file for the GitHub action [here](https://github.com/M-Barrows/Home/blob/a5f801c62f06b2b8028c8d54cd7ea71522d2e307/.github/workflows/docker-hub-deploy.yml), and the resulting Docker image [here](https://hub.docker.com/repository/docker/codecoffee/blog/general). I may do a more thorough write-up in the future for each individual step (let me know over on [Mastodon](https://hachyderm.io/@CodeAndCoffee) if you're interested in this!) but for now I'm going to marvel in just knowing how to connect all the pieces. 

For those of you that skimmed the post looking for the tl;dr or for those that want a recap, you can self-host your blog and still use GitHub Actions for CICD without self-hosting a runner. The high-level architecture of my solution is as follows: 

IDE -- _Commit_ --> GitHub -- _GH Actions_ --> Docker Hub -- _Watchtower_ --> Portainer

Let me know what you think of this solution. Is there a cleaner way to do it? Are there big security flaws that I'm overlooking? What methods are you using for "free" hosting? I'm always looking to connect on [GitHub](https://github.com/M-Barrows), [Mastodon](https://hachyderm.io/@CodeAndCoffee), and/or [LinkedIn](www.linkedin.com/in/michaelabarrows)! 


Until next time! 🙋‍♂️📈
