Title:  UpWork Client - What server nodes are closest to our customer?
slug: geospatial-distance-distribution-centers
Date: 2017-09-22 08:22
Category: Upwork
Tags: geospatial, python;
Author: Larry Gray

As a way to keep my skills fresh, I look for small jobs on [Upwork](https://www.upwork.com) that require python .  For today`s challenge, a client wanted to determine which two servers within a regional zone are closest to their customer.  The client provided a dictionary(see partial dict below, full provided in PLACES.py) with information about each server; the city, ip address, the location, and zone.


    :::python
    PLACES = {
      "Amsterdam": {
        "IP": '208.65.255.10',
        "latitude": 52.370216,
        "longitude": 4.895168,  
        "zone": ['1','2']
      }, 
      "Brussels": {
        "IP": '208.65.255.10',  
        "latitude": 50.850346,
        "longitude": 4.351721,  
        "zone": ['1','2','3']
      }}

The input arguments for this function(fxn) would be the customer`s location(latitude and longitude) and the regional zone.

Let`s look at an example before we code anything to decide what tasks we need to tackle to accomplish this job request.
I live in Baltimore, MD.  My coordiantes are (39.290385, -76.612189).  How would I determine which server node I am closest to in Zone 1. To solve this problem, I would follow the steps below.


{% notebook geospatial_blog.ipynb %}

