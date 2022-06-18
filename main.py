import os

local_deployment = True


def define_env(env):
    @env.macro
    def script(lang: str, nom: str) -> str:
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""

    @env.macro
    def py(nom: str) -> str:
        return script('python', "scripts/" + nom + ".py")

    @env.macro
    def script_admo(lang: str, nom: str) -> str:
        return f"""```{lang}
    --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
    ```"""

    @env.macro
    def py_admo(nom: str) -> str:
        return script_admo('python', "scripts/" + nom + ".py")

    @env.macro
    def script_admo_details(lang: str, nom: str) -> str:
        return f"""```{lang}
        --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
        ```"""

    @env.macro
    def py_admo_details(nom: str) -> str:
        return script_admo_details('python', "scripts/" + nom + ".py")

    @env.macro
    def pyl(expression: str) -> str:
        return f"""`#!python {expression}`"""
