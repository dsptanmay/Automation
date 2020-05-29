def run():
    import pkg_resources
    import subprocess as sp
    import sys
    python = sys.executable
    required = {"PyGithub", "selenium"}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        sp.check_call([python, '-m', 'pip', 'install',
                       '--upgrade', *missing], stdout=sp.DEVNULL)
