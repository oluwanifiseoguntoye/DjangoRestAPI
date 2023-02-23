from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name='drf_Product'):
    client = get_client()
    index = client.init_index('drf_Product')
    return index


def perform_search(query, **kwargs):
    index = get_index()
    parasm = {}
    tags = ""
    if tags in kwargs:
        tags = kwargs.pop('tags') or []
        if len(tags) != 0:
            parasm['tagFilers'] = tags
    results = index.search(query)
    return results