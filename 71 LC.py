# https://leetcode.com/problems/simplify-path/description


class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path

        pathStack = []

        for directory in path.split("/"):
            if directory == "..":
                if pathStack:
                    pathStack.pop()

            elif directory == "." or not directory:
                continue

            else:
                pathStack.append(directory)

        return "/" + "/".join(pathStack)
