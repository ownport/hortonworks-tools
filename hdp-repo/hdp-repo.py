#!/usr/bin/env python
#
#   Hortonworks Repository tool
#

import re
import sys
import json
import requests
import urlparse

from xml.etree import ElementTree


def remove_namespace(tag):

    if '}' in tag:
        return tag.split('}',1)[1]

    return tag

def get_response(url):

    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise RuntimeError('Status code is not OK')

    return ElementTree.fromstring(resp.content)


def list_objects(url, marker=None, filters=None):

    truncated = False

    if marker:
        url = urlparse.urljoin(url, "?marker=%s" % marker)

    for xml_content in get_response(url):
        
        if remove_namespace(xml_content.tag) == 'IsTruncated' and xml_content.text == 'true':
            truncated = True
        
        if remove_namespace(xml_content.tag) != 'Contents':
            continue

        obj = dict()
        for xml_field in xml_content:
            tag_name = remove_namespace(xml_field.tag) 
            obj[tag_name] = xml_field.text
            if tag_name == 'Key':
                marker = xml_field.text
        if filters == None or filters.search(obj['Key']):
            yield obj

    if marker and truncated:
        for obj in list_objects(url, marker, filters):
            yield obj


if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()

    parser.add_option('-r', '--repo-url', help='URL to HDP repository (Amazon S3 bucket)')    
    parser.add_option('-l', '--list', action="store_true", help='return list of objects in HDP Amazon S3 bucket')
    parser.add_option('-f', '--filter', help='filter the list of objects in HDP Amazon S3 bucket')

    (opts, args) = parser.parse_args()

    if not opts.repo_url:
        print >> sys.stderr, "[ERROR] Please specify HDP repository URL"
        sys.exit(1)

    filters = None
    if opts.filter:
        filters = re.compile(opts.filter)


    if opts.list:

        try:
            for obj in list_objects(opts.repo_url, filters=filters):
                print json.dumps(obj)
        except KeyboardInterrupt:
            pass
