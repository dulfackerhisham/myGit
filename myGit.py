import collections
import hashlib, os, zlib
import struct
from dataclasses import fields
from hmac import digest


def read_file(path):
    """Read contents of file at given path as bytes."""
    with open(path, 'rb') as f:
        return f.read()

def write_file(path, data):
    """Write data bytes to file at given path."""
    with open(path, 'wb') as f:
        f.write(data)

# INITIALIZING A REPO
def init(myGitRepo):
    """Create directory for repo and initialize .git directory."""
    if os.path.exists(myGitRepo):
        print(f"Error: Repository '{myGitRepo}' already exists.")
        return  # stop early, don’t overwrite

    os.mkdir(myGitRepo)
    os.mkdir(os.path.join(myGitRepo, ".git"))
    for name in ['objects', 'refs', 'refs/heads']: #creates folders with given names and inside ref a heads folder also
        os.mkdir(os.path.join(myGitRepo, ".git", name))
    write_file(os.path.join(myGitRepo, '.git', 'HEAD'), b'ref: refs/heads/master')
    print('initialized empty repository: {}'.format(myGitRepo))

init("hdRepo")

# HASHING OBJECTS
def hash_object(data, obj_type, write=True):
    """Compute hash of object data of given type and write to object store
       if "write" is True. Return SHA-1 object hash as hex string.
       """
    header = '{} {}'.format(obj_type, len(data)).encode()
    full_data = header + b'\x00' + data
    sha1 = hashlib.sha1(full_data).hexdigest()
    if write:
        path = os.path.join('.git', 'objects', sha1[:2], sha1[2:])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True) #an optional exist_ok parameter, which is False by default. If set to True, it will not raise an error if the directory already exists
            write_file(path, zlib.compress(full_data))
    return sha1

indexEntry = collections.namedtuple('IndexEntry', [
    'ctime_s', 'ctime_n', 'mtime_s', 'mtime_n', 'dev', 'ino', 'mode',
    'uid', 'gid', 'size', 'sha1', 'flags', 'path',
])

def read_index():
    """Read git index file and return list of IndexEntry objects."""
    try:
        data = read_file(os.path.join('.git', 'index'))
        print('data =>', data)
    except FileNotFoundError:
        return []

    digest = hashlib.sha1(data[:-20]).digest()
    print("digest =>", digest)
    assert digest == data[-20:], 'invalid index checksum'
    signature,version, num_entries = struct.unpack('!4sLL', data[:12])
    assert signature == b'DIRC', \
        'invalid index signature {}'.format(signature)
    assert version == 2, 'unknown index version {}'.format(version)
    entry_data = data[12:-20]
    entries = []
    i = 0
    while i + 62 < len(entry_data):
        fields_end = i + 62
        fields = struct.unpack('!LLLLLLLLLL20sH',
                               entry_data[i:fields_end])
        path_end = entry_data.index(b'\x00', fields_end)
        path = entry_data[fields_end:path_end]
        entry = IndexEntry(*(fields + (path.decode(),)))
        entries.append(entry)
        entry_len = ((62 + len(path) + 8) // 8) * 8
        i += entry_len
    assert  len(entries) == num_entries
    return entries