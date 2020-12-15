#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re


def is_aws_s3_bucket_name(bucket_name: str) -> bool:
    """returns True if bucket name is well-formed for AWS S3 buckets

    Applying the rules set here:
    https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html
    """

    # Lengthy code which could be written as a single regular expression.
    # However written in this way to provide useful error messages.
    if len(bucket_name) < 3:
        logging.error('Any AWS bucket name has to be at least 3 ' +
                      'characters long.')
        return False
    if len(bucket_name) > 63:
        logging.error('The provided bucket name for AWS exceeds the ' +
                      'maximum length of 63 characters.')
        return False
    if not re.match(r"^[a-z0-9\-\.]*$", bucket_name):
        logging.error('The AWS bucket name contains invalid characters.')
        return False
    if re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",
                bucket_name):
        # Check if the bucket name resembles an IPv4 address.
        # No need to check IPv6 as the colon is not an allowed character.
        logging.error('An AWS must not resemble an IP address.')
        return False
    if re.match(r"([a-z0-9][a-z0-9\-]*[a-z0-9]\.)*[a-z0-9][a-z0-9\-]*[a-z0-9]",
                bucket_name):
        # Must start with a lowercase letter or number
        # Bucket names must be a series of one or more labels.
        # Adjacent labels are separated by a single period (.).
        # Each label must start and end with a lowercase letter or a number.
        # => Adopted the answer provided by Zak (zero or more labels
        # followed by a dot) found here:
        # https://stackoverflow.com/questions/50480924
        return True

    logging.error('Invalid AWS bucket name.')
    return False
