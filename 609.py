# https://leetcode.com/problems/find-duplicate-file-in-system/submissions/

from typing import List
from collections import defaultdict

class Directory():
    def __init__(self, path, children):
        self.path = path
        self.children = children
    
    def from_string(s):
        path, *rest = s.split()
        files = [File.from_string(r) for r in rest]
        return Directory(path, files)
    
    def __repr__(self):
        return f'Directory{(self.path, self.children)}'

class File():
    def __init__(self, name, content):
        self.name = name
        self.content = content
    
    def from_string(s):
        name, rest = s.split('(')
        content = rest[:-1]
        return File(name, content)
    
    def __repr__(self):
        return f'File{(self.name, self.content)}'

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directories = [Directory.from_string(p) for p in paths]
        content_to_filename = defaultdict(list)
        for directory in directories:
            for child in directory.children:
                if type(child) is not File:
                    continue
                file: File = child
                fqn = f'{directory.path}/{file.name}'
                content_to_filename[file.content].append(fqn)
        duplicates = [filenames for filenames in content_to_filename.values() if len(filenames) >= 2]
        return duplicates

input = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
r = Solution().findDuplicate(input)
print(f'{list(r) = }')
