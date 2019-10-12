# Caching has two advantages:
# 1. you get the web page a lot faster
# 2. your application has to do less work 
# caching is a common way to make things fasster
# all big websites use caching and that data is stored in a hash!

cache = {}

def get_page(url):
    if cache.get(url):
        # returns cached url
        return cache[url]
    else:
        data = get_data_from_server(url)
        # saves this data in your cache first
        cache[url] = data
        return data

# here you make the server do work only if the url isnt in the cache
# before you return the data, you save it in the cache
# the next time someone requests this url, you can send the data from the cache instead of making the server do the work 