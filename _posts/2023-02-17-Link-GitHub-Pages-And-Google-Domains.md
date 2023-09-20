---
title: I Linked My GitHub Pages Website To My Google Domain
layout: post
date: '2023-02-17'
excerpt: "Want to ditch the .github.io domain and publish websites to your own domain? I figured out how to do it and so can you!"
excerpt_separator:  <!--more-->
tags: 
    - Web Development
    - GitHub
    - Quick Reads

categories: 
    - Tutorial
---
> 📝 Key Ideas
> * Update: Google Domains is now owned by Squarespace
> * If you can acquire a domain, you easily make your GitHub pages site look more professional

I've long pined over the idea of owning my own domain, starting a home lab filled with services that I develop, and making them available to the public. Not because I think I can create the next Mastodon, Python, or Docker, but because tinkering with this stuff and sharing my results (even if it's to 0 people) makes me happy.

Rather than try to build a complex software product with a complex hosting paradigm, I decided to keep my first step into the world of public domains simple - host this blog (a Github pages site) at my shiny new domain: [https://blog.codecoffee.org]()! Below is my quick walk through of how to complete this for yourself.

<hr>

To do this we really only need a few things: 

🔗 A domain (I got my via [Google Domains](https://domains.google.com/registrar/))

📄 A [Github pages](https://pages.github.com/) site

🕧 15 minutes

☕ A hot beverage

Unfortunately, with many things these days turning to a subscription model, there aren't as many options for obtaining free domains. That said, if you're willing to get creative with your name, you can often get domains at Google Domains for $12USD/yr (sometimes $8 when they are on sale). It's definitely far from free but if you _need_ a domain, $1/month is probably attainable. You can also get a domain from other registrars but Google makes this process easy. 

Once you've paid for your domain, head on over to the DNS page {https://domains.google.com/registrar/<< yourdomain >>/dns}. From here, click "Manage Custom Records" and enter values like the ones below: 

|Host Name|Type|TTL|Data|
|:--|:--:|--:|:--|
|<< your-subdomain >>|CNAME|300|<< your github user name>>.github.io.|

* __"Host Name"__ is the subdomain you want to publish under. If your domain is coolperson.com and you want to start a blog, you might choose "blog" so that the end result is blog.coolperson.com.
* __TTL__ = Time To Live. This is how long (in seconds) DNS entries are cached. This means that when sites are accessed within this amount of time, the response is faster. It also means that if you make changes to your site, you most likely won't see them reflected for this amount of time. I set this to 60 during setup and then something longer later. 

Once you've done this head back to your gh-pages site and go to the "pages" section of the repository's settings. Under the "Custom domain" section enter the full domain you want this site to be published under. This should be the host name from above and your domain (i.e. blog.coolperson.com). Once you click save, you'll need to wait for Github to validate some DNS things and create SSL certificates (about 5 minutes). 

<blockquote>⚠️ Take Note: if you are performing this step on a mobile device, you may be redirected to the mobile app or an embedded webpage once you click "save". This will prevent the process from completing. Force your browser into desktop mode or do this at a computer to avoid this issue. This happens because Github actually attempts to add a <code>CNAME</code> file to your repository's root directory which it can't do on mobile. </blockquote>

If you get the green light from Github then your website should be published!🥳 Head on over to the shiny new website and take a look! 

A couple additional notes: 
* If you are using absolute links anywhere in your site, you'll want to rewrite them to use your new domain. This isn't usually necessary but it can avoid some headaches in the future.
* If you're using a custom theme for your page like I was, you might want to re-build your site and re-deploy to Github. I had some odd formatting errors that were fixed after the re-deploy. 
* This method above does not talk about any security you may want to invoke on your site. I recommend reading up on DNS validation as a next step if that interests you. 

This is just the first step in my journey of public publication. I'm not sure what my next step will be but stay tuned here as I'll be posting any updates/learned lessons here or on [Mastodon](https://hachyderm.io/@CodeAndCoffee)! 

Until next time! 🙋‍♂️📈

[GitHub](https://github.com/M-Barrows) | [Mastodon](https://hachyderm.io/@CodeAndCoffee) | [LinkedIn](www.linkedin.com/in/michaelabarrows)
<hr>

Sources I used to understand this process: 
* [Github docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
* [Medium Article by Steve Jones](https://medium.com/@steve_jones/4-how-to-point-a-domain-on-google-domains-to-github-pages-1d4c24f01382)


