# HDP repository, objects list

##  HDP Repositories

- http://s3.amazonaws.com/public-repo-1.hortonworks.com/

## How to use

```sh
$ ./hdp-repo.py -h
Usage: hdp-repo.py [options]

Options:
  -h, --help            show this help message and exit
  -r REPO_URL, --repo-url=REPO_URL
                        URL to HDP repository
  -l, --list            return list of objects in HDP Amazon S3 bucket
  -f FILTER, --filter=FILTER
                        filter the list of objects in HDP Amazon S3 bucket
```

## The sample output for listing HDP repository

```json
{"LastModified": "2012-04-24T02:03:52.000Z", "ETag": "\"bcab5263db7f547ddb9a506aeb073f13\"", "StorageClass": "STANDARD", "Key": "HDP-1.0.7/repos/centos6/ganglia/ganglia-debuginfo-3.2.0-99.x86_64.rpm", "Size": "367124"}
{"LastModified": "2012-04-24T02:03:53.000Z", "ETag": "\"4cec16134fe53b641c4927222c276656\"", "StorageClass": "STANDARD", "Key": "HDP-1.0.7/repos/centos6/ganglia/ganglia-devel-3.2.0-99.x86_64.rpm", "Size": "48660"}
{"LastModified": "2012-04-24T02:03:54.000Z", "ETag": "\"9bbaa23e20057fd3f7d2019c55b7c015\"", "StorageClass": "STANDARD", "Key": "HDP-1.0.7/repos/centos6/ganglia/ganglia-gmetad-3.2.0-99.x86_64.rpm", "Size": "36976"}
{"LastModified": "2012-04-24T02:03:54.000Z", "ETag": "\"5b803bfe730dfc38c8aa2e63e5423d6e\"", "StorageClass": "STANDARD", "Key": "HDP-1.0.7/repos/centos6/ganglia/ganglia-gmetad-python-3.2.0-99.x86_64.rpm", "Size": "57436"}
{"LastModified": "2012-04-24T02:03:54.000Z", "ETag": "\"db9856e3f4ae2a26470d2367782412c4\"", "StorageClass": "STANDARD", "Key": "HDP-1.0.7/repos/centos6/ganglia/ganglia-gmond-3.2.0-99.x86_64.rpm", "Size": "103468"}
```

