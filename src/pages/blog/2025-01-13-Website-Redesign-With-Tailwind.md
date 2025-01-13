---
title: Website Redesign - Bootstrap and Bulma and Tailwind, Oh My!
layout: post
date: '2025-01-13'
hidden: false
excerpt: "Bootstrap is okay but Tailwind is better."
excerpt_separator:  <!--more-->
tags: 
    - Blog
    - Tailwind
    - Bootstrap
    - Design
    - Web Development

categories: 
    - Show And Tell
---
> 📝 Key Ideas
> * Bootstrap is a great framework for exactly that, bootstrapping
> * Tailwind gives you great control without sacrificing too much in the translation layer 
> * Tailwind is great for building custom components and standard styles as you go

# Why I Need A Change

I've had my blog for several years now. In that time, it's gone through a few iterations. I actually think I might re-design it more than I author posts. But we don't talk about that here 🙄. When I first created it, I really liked the theme. It was simple, easy to understand and high contrast. However, it was a very common Jekyll template that I've seen elsewhere on the interwebs and has largely remained the same for the last 5-6 years. About a month ago I decided that it was time to not only re-design it, but I also didn't want to use a 3rd party template this time. The question was, how best to accomplish that (for me).

In the past when I wanted to design my own web UI, I would often reach for [Bootstrap](https://getbootstrap.com/). It's a great UI toolkit but didn't feel like the right choice for the new design (even though it totally could have been). For the new site, it was most important that I create a site that doesn't look like YABS (Yet Another Bootstrap Site). But, I still wanted to easily create/utilize some basic component libraries to speed things along because I'm definitely more of a utilitarian designer rather than a beauty-forward designer. I tried both [Bulma](https://bulma.io/) (because it claimed to be open source, responsive, and easy to use) and [TailwindCSS](https://tailwindcss.com/) (because it's an industry standard I wanted to know more about). I ultimately settled on Tailwind (for now) but had a good time trying both.

# What I Still Like About Bootstrap 

Like I said before, I could have totally used Bootstrap for this redesign. It's not like there is anything fancy or super custom about it. However, I wanted the "stock" version of the UI toolkit I chose to look different than bootstrap without fighting against the tide as it were to do so. So, even if it looks like every other Tailwind or Bulma site, I was fine with that. 

That said, Bootstrap is still a great UI toolkit to me for several reasons: 

## 1. It's Really Easy To Get Up And Running

If you're really in a time crunch, using the CDN header links for both `CSS` and `JS` can give you access to the entire library of componnents and functionality without any fuss. This benefit compounds for new developers or developers working on very lightweight proof of concepts. There are no build steps to mess around with, no directory structure to be forced into, just plain and simple HTML with very helpfull classes sprinkled in. 

## 2. It's Comfortable

Not only is the toolkit so ubiquitous that many developers already know and use it, but the visual design language is comfortable for end-users as well. There is something to be said for this level of comfort. Will it knock anyone's socks off? No, of course not. But will your great aunt Meriam be able to navigate your site in the dark? You bet your fruit poundcake she will! 

## 3. It's Uncluttered

When you're able to build a website with pure bootstrap components, the visual code bloat is actually really minimal compared to something like Tailwind (which is why I avoided Tailwind at first). This allows you and anyone you're collaborating with to just focus on creating content rather than decyphering your HTML class hyroglyphics. 

It's these three reasons why I still plan to use bootstrap on 90% of my proof of concept designs. However, when you try to branch out from the "normal" is when bootstrap starts to lose its luster. 

# Why Bulma didn't work 

In my first attempt at a redesign, I was looking for light weight open source solutions that were mobile-first. This lead me to Bulma. At first, I was smitten. Everything about this toolkit matched my understanding of how a toolkit should function. The install was easy, the syntax was straight forward, and the components were useful. However, this all started to change when I wanted to deviate from the norm. 

Admittedly, I was trying to create a design that didn't strictly match the components that were available, so I expected some challenges. That said, what I did not expect was the responsive design tools fall on their face when displaying on mobile. Often, when building out pages, the `is-n-mobile` sizing wouldn't work. Instead, the smallest breakpoint would often default to `tablet`. I packed up and ran to Tailwind before I ever figured out exactly why this was. I'm sure there was some user error there, but if this core techniques was not obviously fixable, I'm happy to move on before wasting more of my time. 

Another more core issue was how overlapping style priority was handled. I never felt like I could predict how and when the traits of a basic HTML element (i.e. `h2`) would change in response to styling via Bulma. While I understand how this happens, I want my toolkit to be predictable. I don't suddenly want my hammer to become a staple gun. 

# Why I'm Sticking With Tailwind (For Now)

## No Assumed Style

At first, the fact that my `<h1></h1>` tags were exactly the same size as my `<p></p>` tags kept throwing me for a loop. But, after I adjusted to this new, totally unstyled default it became way easier to set **intentional** styles without worry of overlapping styles with unpredictable behavior. While this is definitely a negative for someone that wants to get up and running quickly, it's a really great migraine prevention pattern for anyone else. 

## Documentation Is Great

As with all 3rd party tools, the documentation is critical to ~~your~~ my ability to use it effectively. For me documentation must have: 

* Clear, repeatable examples
* Complete nuts and bolts (All parameter values options, funtion overloads, configuration options, etc.)
* Philisophical ideology explaination for *why* I should make certain choices 

I often find that many open source projects (my projects are 100% included in this) are often only good at one or two of the previous requirements. Thankfully for Tailwind, it accomplishes all three. This means that if I run into a roadblock, I can usually find a passable solution by spending 5 minutes reading the docs. 

## Classes Are Lightweight

At first glance, I thought Tailwind was pretty messy since there were so many classes needed to achieve a desired style. But, it wasn't until I started using it until I understood why and what's so great about that. 

The naming of each class in `Tailwind` is effectively the same as (or only slightly diverged from ) the true CSS names. This means that if you know CSS you can quickly pick up Tailwind. It also means if you don't fully know CSS, learning Tailwind isn't like learning a whole new proprietary abstracted language (even though it technically is), which means if you ever need to use vanilla CSS, it would be easy to pick up. I call this a win:win!

## Trying Something New Is Refreshing

Let's face it - everyone likes a little *shiny* in their life once in a while. Is Tailwind perfect? I'm not qualified to say. Was it a tool that fixed my problem? Yes. Is it fun to use? For me, also yes! Is that enough to qualify it as the "right tool" right now? You betcha! 

# Conclusion

Re-designing my blog is always fun because it often mirrors a my technical interests at the time. This iteration highlights my desire for controlled predictability with a focus on simplicity and reliability. Tailwind has helped me achieve most, if not all of these goals in a CSS toolkit and been a lot of fun to use along the way. 