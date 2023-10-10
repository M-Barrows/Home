---
title: It's Always DNS
layout: post
date: '2023-10-03'
hidden: true
excerpt: "I configured Pi-hole on Portainer using Macvlan. Here's what I did wrong so you don't make the same mistakes."
excerpt_separator:  <!--more-->
tags: 
    - Docker
    - Containers
    - Portainer
    - Home Lab
    - Pi-hole
    - Networking

categories: 
    - Lessons Learned
---
> 📝 Key Ideas
> * The Macvlan driver makes Docker containers look like standalone devices
> * Make sure to double check your Docker network configuration before moving this setup to production
> * DHCP leases may not expire for a while. Force them to refresh or be ready for random service outages later. 

## Why I Love Pi-hole 

I love [Pi-hole](https://pi-hole.net/)! I've been running it on a Raspberry Pi for almost 7 years now (the last 5 were on a [Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)). It was the perfect gateway into networking and Raspberry Pis for me. In fact, I loved it so much, I [wrote my own dark theme](https://github.com/M-Barrows/pi-hole-material-dark) for the UI before there was official support for it. 

I think the best part of Pi-hole is that it has always grown with my needs and interests. And, while I was not lacking for anything with my previous setup, I'm currently excited about containerized applications and thus used this as an excuse to migrate my current setup to Pi-hole's [official docker image](https://github.com/pi-hole/docker-pi-hole/#docker-pi-hole). 

## Current State

Lately I've been testing a lot of services out in my home lab. 
Usually, when I want to try out a new service, I add it to my development environment and tweak it until it's ready for production. However, with Pi-hole I had previously set it up not only as my network wide ad blocker but also as DHCP server. This allowed me to easily set up custom rules for specific clients (gaining me spouse approval 👍) among other quality of life improvements. 

Unfortunately, this means that migrating my Pi-hole instance is essentially an all-or-nothing event. There are some iterative steps I can take but they aren't comparable to the desired configuration. 

## Trial And Error

When starting this upgrade, I turned to the official docs<sup>[1](#sources)</sup> to help me decide which networking setup I would need to run Pi-hole as my DHCP server. Then, following their recommendation, I drew heavy influence from Tony Lawrence's post<sup>[2](#sources)</sup> when getting started with docker-compose. However, knowing next to nothing about networking (especially subnet masks and CIDR), I was unsure how to adapt the code for my environment. For reference, here is the original code from Tony Lawrence: 

```yaml
# Note: 192.168.123.xxx is an example network, you must update all these to match your own.

version: '2'

services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    hostname: pihole
    domainname: example.com             # <-- Update
    mac_address: d0:ca:ab:cd:ef:01
    cap_add:
      - NET_ADMIN
    networks:
      pihole_network:
        ipv4_address: 192.168.123.199   # <-- Update
    dns:
      - 127.0.0.1
      - 8.8.8.8
    ports:
      - 443/tcp
      - 53/tcp
      - 53/udp
      - 67/udp
      - 80/tcp
    environment:
      ServerIP: 192.168.123.199         # <-- Update (match ipv4_address)
      VIRTUAL_HOST: pihole.example.com  # <-- Update (match hostname + domainname)
      WEBPASSWORD: ""                   # <-- Add password (if required)
    restart: unless-stopped

networks:
  pihole_network:
    driver: macvlan
    driver_opts:
      parent: ovs_eth0
    ipam:
      config:
        - subnet: 192.168.123.0/24            # <-- Update
          gateway: 192.168.123.1              # <-- Update
          ip_range: 192.168.123.192/28        # <-- Update

```

Since I have some proxmox servers hardwired to my router and setup as static IPs in my environment, I thought I would be fancy and have my router assign IPs like 192.168.0.0 - 192.168.0.100 and then have Pi-hole assign IPs like 92.168.0.0 - 192.168.0.255. 

At first, I had trouble getting the container to even deploy. This ended up being a two-fold problem: 

1. My `parent` driver option needed to be set to `eth0`. I think this is just a difference in virtualization software between synology and Proxmox and how they label the network interface
2. My `gateway` value wasn't correct - it needed to be set to my router's IP since I wanted all traffic from Pi-hole to go through the router before exiting to the WAN.

Once I had the container up, it became much easier to troubleshoot issues. The next thing I ran into was the combination of my `ip_range` and `subnet` values. I mentioned that I wanted to be fancy and stagger the IPs of my Router and Pi-hole. However, I forgot that when I turn off DHCP on the router, it doesn't matter because the router won't be assigning IPs. 

Before I figured this out, everything seemed to work at first. New devices would get an appropriate IP and existing devices would retain their original IP. However, many hours later I started to notice some services that were unavailable. The unavailable services all had IPs that were assigned by the router. This was weird since everything worked last night. 

Because this started to happen during the middle of the day (and my spouse deserves at least 3 nines of uptime), I immediately turned off DHCP on Pi-hole, turned it back on in my router's settings, and set my router's DNS server to the Pi-hole's IP address. This at least got me add blocking even if I didn't have good visibility into client names. 

After some pondering, it hit me! The DHCP reservations had recycled and the machines with static IPs were no longer able to get a good IP because those IPs were no longer being assigned. 🤦 Once I realized this, I updated the `ip_range` and `subnet` mask values to mirror that of my original router. After a redeploy the issue was immediately fixed. Thank goodness! 

I've now been happily enjoying network-wide add blocking and custom DNS entries for easy access to my local services for several hours now. Huzzah 🙌! 

## Takeaway

Pi-hole is still great, Docker containers are still awesome, and I'm still [cosplaying as a sysadmin](https://www.jeffgeerling.com/blog/2022/cosplaying-sysadmin_). 

If I were to do it all over again, I'd recommend that you start by mirroring your router's main network settings one-for-one. After all, why reinvent the wheel when you can always stop the docker container and turn the router's DHCP back on if it doesn't work. That said, I don't regret making my mistakes because they have tought me a lot about Docker netowrking. Now, I'm excited to switch some of my other services to Macvlan as well! 


<hr>

## Sources
1. [Pi-hole DHCP Docs](https://docs.pi-hole.net/docker/dhcp/#docker-pi-hole-with-a-macvlan-network)
2. [Tony Lawrence](https://tonylawrence.com/posts/unix/synology/free-your-synology-ports/)
