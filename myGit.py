import os

def read_file(path):
    """Read contents of file at given path as bytes."""
    with open(path, 'rb') as f:
        return f.read()

def write_file(path, data):
    """Write data bytes to file at given path."""
    with open(path, 'wb') as f:
        f.write(data)

def init(myGitRepo):
    """Create directory for repo and initialize .git directory."""
    os.mkdir(myGitRepo)
    os.mkdir(os.path.join(myGitRepo, ".git"))
    for name in ['objects', 'refs', 'refs/heads']: #creates folders with given names and inside ref a heads folder also
        os.mkdir(os.path.join(myGitRepo, ".git", name))
    write_file(os.path.join(myGitRepo, '.git', 'HEAD'), b'ref: refs/heads/master')

init("hdRepo")