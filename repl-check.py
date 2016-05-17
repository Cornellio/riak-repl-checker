#!/usr/bin/env python

import riak

def get_riak_object(host, key, bucket='shoppingcart'):

    client = riak.RiakClient(protocol='http', nodes=[
        {'host': host, 'http_port': 8098}
        ])

    bucket = client.bucket(bucket)
    fetch = bucket.get(key)

    return fetch.data

def put_riak_object(host, key, value, bucket='shoppingcart'):

    client = riak.RiakClient(protocol='http', nodes=[
        {'host': host, 'http_port': 8098}
        ])

    bucket = client.bucket(bucket)

    val1 = value
    key = bucket.new(key, data=val1)
    key.store()


value_to_store = {'veges': '2',
                  'fruits': '4'}


put_riak_object(host='wwwriak01-sc9', key='ops_testkey1', value=value_to_store)
print(get_riak_object('wwwriak01-sc9', key='ops_testkey1'))




# Valid prod keys:
#   49730b73-ecee-4c8a-8fe6-680babca3215
