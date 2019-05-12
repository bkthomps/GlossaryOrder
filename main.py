# Copyright (c) 2019 Bailey Thompson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import sys

words = set()
definitions = []


class Entry:
    def __init__(self, key, line):
        self.key = key
        self.line = line


def add_item(line):
    item = line.partition(':')[0]
    key = re.sub(r'[^a-zA-Z0-9]+', '', item).lower()
    if key in words:
        print("Warning: " + key + " redefined; using first instance")
        return
    words.add(key)
    entry = Entry(key, line.strip('\n'))
    definitions.append(entry)


def load_file(name):
    with open(name, "r") as file:
        for line in file:
            add_item(line)


def write_file(name):
    file = open(name, "w")
    for line in definitions:
        file.write(line.line + '\n')
    file.close()


def sort_file(name):
    load_file(name)
    definitions.sort(key=lambda x: x.key)
    write_file(name)


for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    if file_name[-4:] != ".txt":
        print("Error: cannot sort " + file_name + " because it must be .txt")
        continue
    print("Sorting file " + file_name)
    sort_file(file_name)
    words.clear()
    definitions.clear()
    print("Done sorting file " + file_name)
