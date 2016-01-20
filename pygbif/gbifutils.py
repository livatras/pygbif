import requests
import pygbif

class NoResultException(Exception):
    pass

def gbif_search_GET(url, args, **kwargs):
  # if args['geometry'] != None:
  #   if args['geometry'].__class__ == list:
  #     b = args['geometry']
  #     args['geometry'] = geometry.box(b[0], b[1], b[2], b[3]).wkt
  out = requests.get(url, params=args, **kwargs)
  out.raise_for_status()
  stopifnot(out.headers['content-type'])
  return out.json()

def gbif_GET(url, args, **kwargs):
  out = requests.get(url, params=args, headers=make_ua(), **kwargs)
  out.raise_for_status()
  stopifnot(out.headers['content-type'])
  return out.json()

def gbif_POST(url, body, **kwargs):
  head = make_ua()
  out = requests.post(url, json=body, headers=head, **kwargs)
  out.raise_for_status()
  stopifnot(out.headers['content-type'])
  return out.json()

def stopifnot(x):
  if x != 'application/json':
    raise NoResultException("content-type did not = application/json")

def stop(x):
  raise ValueError(x)

def make_ua():
  return {'user-agent': 'python-requests/' + requests.__version__ + ',pygbif/' + pygbif.__version__}

gbif_baseurl = "http://api.gbif.org/v1/"
