# HDP repository, objects list

```sh
$ ./hdp-repo.py --help
Usage: hdp-repo.py [options]

Options:
  -h, --help  show this help message and exit
  -l, --list  return list of objects in HDP Amazon S3 bucket
```

```sh
$ ./hdp-repo.py --list 
{'LastModified': '2013-04-03T19:11:12.000Z', 'ETag': '"8e6f4699784a015da4a79ba18ee37d71"', 'StorageClass': 'STANDARD', 'Key': 'AMBARI-1.x/repos/centos5/AMBARI-1.2.0.1-centos5.tar.gz', 'Size': '40470164'}
{'LastModified': '2013-04-03T18:55:11.000Z', 'ETag': '"4736e675191a019e52be4620d32f3b88"', 'StorageClass': 'STANDARD', 'Key': 'AMBARI-1.x/repos/centos5/AMBARI-1.x-1.el5.noarch.rpm', 'Size': '2164'}
{'LastModified': '2013-04-03T18:55:11.000Z', 'ETag': '"e1151532420201fa9bfb509fb1920238"', 'StorageClass': 'STANDARD', 'Key': 'AMBARI-1.x/repos/centos5/RPM-GPG-KEY/RPM-GPG-KEY-Jenkins', 'Size': '1666'}
{'LastModified': '2013-04-03T18:55:11.000Z', 'ETag': '"d3b39e60b9a198423d0a8729d8d59132"', 'StorageClass': 'STANDARD', 'Key': 'AMBARI-1.x/repos/centos5/ambari.repo', 'Size': '539'}
{'LastModified': '2013-04-03T18:55:11.000Z', 'ETag': '"11d3d10000079565c6680724cdb4419c"', 'StorageClass': 'STANDARD', 'Key': 'AMBARI-1.x/repos/centos5/build_metadata.txt', 'Size': '182'}
...
```
