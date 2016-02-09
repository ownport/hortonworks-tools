#!/usr/bin/env python
#
#   Hortonworks Repository tool
#

import sys
import json
import requests
import urlparse

from xml.etree import ElementTree


HDP_REPO_URL="http://s3.amazonaws.com/public-repo-1.hortonworks.com/"

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


def list_objects(url, marker=None):

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
        yield obj

    if marker and truncated:
        for obj in list_objects(url, marker):
            yield obj


if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()
    parser.add_option('-l', '--list', action="store_true", help='return list of objects in HDP Amazon S3 bucket')

    (opts, args) = parser.parse_args()

    if opts.list:

        try:
            for obj in list_objects(HDP_REPO_URL):
                print obj
        except KeyboardInterrupt:
            pass
