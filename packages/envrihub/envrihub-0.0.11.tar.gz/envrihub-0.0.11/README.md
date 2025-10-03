# ENVRI Hub's VRE Library
This is the official ENVRI-Hub Python library, its purpose is to streamline interaction with the ENVRI-Hub APIs, providing a pythonic facade to data and service access.

# Quickstart
After installing the package with a quick
```
pip install envrihub
```
You can start using the ENVRI-HUB resorces right away through the *Hub* object:
```
from envrihub import Hub

hub = Hub()
```
You can query it to retrieve resources that match your needs:

```
for res in hub.search_catalogue('bacon'):
    print(res.title)
```
You can specify free text queries, time boundaries, geographic boundaries, dara providers and/or variables you expect in your data.
Here is an example of geographical search with a [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) polygon:

```
geography = 'POLYGON((10.70 48.34,
                28.98 48.34
                28.98 36.17,
                10.70 36.17,
                10.70 48.34))'

for i in hub.search_catalogue(geography = geography):
    print(i.title)
```

Just type `help(hub.seach_catalogue)` for the full details.

You can also access a resurce directly if you know its unique *identifier* in the Catalogue of Services:
```
res = hub.fetch_from_catalogue('b646c445-57b8-4553-bf2f-12448ee16b55')
```
Retrieved resources have the following properties:
+ `title`: a human readable title for the resource;
+ `id`: the resource's identifier in the Catalogue of Services;
+ `description`: a human readable description of the resource;
+ `metadata`: the whole EPOS-DCAT-AP metadata of the resource;
+ `dao`: the *data access object* that allows you to get the actual data. All DAOs have an `access` method.


DAO objects are auto-generated according to the resource's metadata and can have additional methods to access data, when in doubt check them out with the `help` function:
```
help(res.dao)
```
If the resource is a Web Service, the DAO object allows to query such a service with all due parameters:
```
res = hub.fetch_from_catalogue('16c3ae2f-ba39-4239-964d-12e67c378fef')
res.dao.access(id='138228')
```
Or if the resource is a static file it lets you download it either as a bytes object or directly to your file system.
```
res = hub.fetch_from_catalogue('b646c445-57b8-4553-bf2f-12448ee16b55')
byte_stream = res.dao.access() # bytes object
res.dao.download('path-to.file') # local file download
```
Digital kleptomaniacs rejoice! This means that with a handful of lines you can now scrape the whole ENVRI-HUB!
```
for res in hub.search_catalogue():
    if res.is_downloadable():
        res.dao.download(res.id)
```

# Contributing
To contribute, you have to attend *ENVRI-Hub Next*'s WP13 monthly meetings. For now, if we never saw you, your pull requests will be rejected.

# Acknowledgements
This project is funded by the [ENVRI-Hub Next project](https://envri.eu/envri-hub-next/). The project received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101131141.