---
title: Github Pages + Jekyll + Hydeout
layout: post
date: '2020-08-23'
excerpt: "Quick outline for how I created a Github Pages blog using Jekyll and the Hydeout theme."
excerpt_separator:  <!--more-->
tags: 
    - web development
    - github
    - jekyll
    - hydeout
    - theme

categories: 
    - Tutorial
---

## Why

My previous attempt at a Github Pages website used [Vue.js](https://vuejs.org/) to help simplify the construction process. Since the site was mostly meant to serve as a resume website (past project lists, employment history, education, etc.), it was mostly lists of objects. Using Vue.js meant I could construct my lists in JSON format. However, when I wanted to shift gears from a resume website to a blog, I knew that it would take too much time to continue to develop it in Vue.js. Eventually, after some googling, testing, and head-scratching I determined that the best solution is sometimes the simplest. In this case, that means Jekyll. 

## What

For this project I had a couple of objectives: 

1. The website should be publishable on Github Pages
2. The website should have blogging functionality
3. The website should be easy to update
4. Teh website should have a simple and pleasing theme

In reviewing all of these requirements, I decided that a Jekyll site published to Github Pages would be the appropriate solution. 

## How

While it was not immediately aparent how to implement a Jekyll site (despite [this very sussinct tutorial](https://www.kiltandcode.com/2020/04/30/how-to-create-a-blog-using-jekyll-and-github-pages-on-windows/)), it can actually be done in relatively few steps assuming you are starting from scratch.

### Preparation

While I could feasibly do all of my development work from within Github, I find it better if I can see my changes live. In order to do that, I needed to prepare a few things: 

1. Download and install [Ruby+DevKit](https://rubyinstaller.org/) using the instructions found [here](https://www.kiltandcode.com/2020/04/30/how-to-create-a-blog-using-jekyll-and-github-pages-on-windows/#how-to-install-jekyll-on-windows)

2. Find a Jekyll theme that I liked on GitHub. There are many out there (including officially supported GH-pages themes) but I chose [Hydeout](https://github.com/fongandrew/hydeout) for this blog. Once i had cloned the repository to my local machine (```git clone https://www.github.com/[user]/[repo].git```) I could then rename the containing folder to something more appropriate (in my case, change "hydeout" to "home").

3. Ensure the theme works by running ```jekyll serve``` from within the project directory (./home in this case). After navigating to https://localhost:4000 I could see the theme's website which means that it works.

### Edit

Now for the fun part! After I tested the site to ensure operability, I could start to make the blog my own. I took this time to change all personal information, remove demo blog posts, and update miscellaneous information. Some of the _config.yml and other settings that were changed and not so obvious (to me) were: 

* updating the theme to "jekyll-theme-hydeout"
* updating the budler dependency to version 2.4.1 in jekyll-theme-hydeout.gemspec with the following line: ```spec.add_development_dependency "bundler", "~> 2.1.4"```. For some reason, I was running into an issue where it expected version 1.* and all I had was version 2.*. While this is clearly a shortcut, it seems to work now so I'm going with it. 
* When testing I need to make sure that I'm in the root folder (/Home/ in this case) before I run ```jekyll serve```. Failing to do so will cause your build to fail. The same root folder is the folder that I needed to push to github (not the hydeout folder that is bundled with the repo after cloning). 
* The tagline of the website is hidden in */_includes/sidebar.html*
* Turning off commenting with **Disqus** is done by commenting out the following code in the layout pages (i.e. */_layouts/post.html*) ```{% include comments.html %}```


### Publishing

Moving my site to a public location was fairly straight forward since I'm already familiar with Github Pages. All that was required was to push my home directory (*/Home/\**) to my github repo under a gh-pages branch. Then, in the repo settings, make it public and tell Github to publish the gh-pages branch. 

## Final Thoughts

While I'm clearly late to the party, I think Jekyll will be a great solution to my current need. I know there is tremendous room for growth and many areas where I can expand my learning (Ruby is chief among them), but I'm very happy with my shiny new blog for now. 

