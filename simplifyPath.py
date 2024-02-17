class Solution:
    def simplifyPath(self, path: str) -> str:
        path_component = path.split('/')
        result = []
        for component in path_component:
            if component == "..":
                if result:
                    result.pop()
            elif component and component != ".":
                result.append(f"/{component}")
        if not result: return '/'
        return "".join(result)
