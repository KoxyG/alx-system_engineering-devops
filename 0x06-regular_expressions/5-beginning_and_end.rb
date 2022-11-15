#!/usr/bin/env bash
#This is a ruby script exactly match a string that starts with h ends with n and can have any single character in between
puts ARGV[0].scan(/h[a-z]n/).join
