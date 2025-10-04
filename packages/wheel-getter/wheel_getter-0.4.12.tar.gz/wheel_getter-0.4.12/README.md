# wheel-getter

## What's the problem?

I want to install (locally authored) Python packages on servers that (for
security and other reasons) can't retrieve packages from PyPI or that (for
security reasons) don't have compilers and other development tools
installed. And I want to be sure that the same packages are installed as in
my development or staging environment, identified by a hash checksum.

My workflows are based on uv, which is fast and has other advantages in
comparison to pip, pip-tools and other “legacy” tools. Unfortunately uv
doesn't (yet?) offer an export of wheels (like `pip wheel`) that were
downloaded or locally built. AFAICT uv doesn't even cache downloaded wheel
but just their contents (which makes copying / hardlinking them into venv's
faster).

## How can wheel-getter help?

This tool reads uv's lockfile and downloads the same wheels that uv has used
for the current project. The lockfile contains checksums for these wheels;
they are checked against the downloaded files.

For locally built wheels the lockfile has “sdist” information with URLs and
checksums for the source archives. The wheel-getter tool retrieves these
archives, invokes `uv build` and grabs the resulting wheels.

For these freshly made wheels some metadata is added to the wheel directory,
containing file size and checksum so that the wheels can be verified.

## Can wheel-getter guarantee workflow security?

No. Use it at your own risk.

## How can I install this tool?

The easiest way is `uv tool install wheel-getter`; there are plenty of
alternatives, of course.

## How should I use wheel-getter?

It is recommended to cd into the base directory of your project where your
`pyproject.toml` file lives, after having locked and synced (and tested) the
project. Then invoke wheel-getter, specifying the Python version unless it's
the one that executes wheel-getter itself:

```
wheel-getter --python=3.11
```

If all is well, all required wheels should be collected in the `wheels`
subdirectory (or the output directory specified by `--wheelhouse`).

Please note that no wheels are built for packages installed as editable; you
should build them as usual and copy them to the “wheelhouse” yourself.

Since this tool has only been tested and used under Linux, there can (and
will) be problems with other OSes.

## Example

Let's assume you have a development installation of a Python project with
a `pyproject.toml` file, managed with uv.

### Step 1: Preparation

Build a wheel from your project: `uv build` (after having incremented the
version number, e.g. with `uv version --bump minor` or the like).

### Step 2: Collect wheels

Invoke wheel-getter; check the contents of the `wheels` directory.

### Step 3: Create temporary staging installation

Create a directory for a temporary staging installation. It should be
outside your development tree (so that neither uv nor git will regard it as
belonging to the project) but on the same filesystem (so that uv can create
hardlinks ad lib). Copy or, better, symlink the `wheels` directory and
initialize a bare Python project like this:

```
cd staging_base
ln -s ~/projects/my_proj/wheels .
uv init --bare stage313
cd stage313
uv python pin 3.13
uv add --no-index --find-links ../wheels my-proj
```

You should now have a uv lockfile referencing your project and all packages
it depends on as installed from `../wheels`, and if all was well, the
project dependencies were satisfied from this “wheelhouse”.

The pinned Python version should be the same that wheel-getter was running
for in the previous step. Otherwise it would not match version-dependent
wheels.

### Step 4: Deployment on the target host

We will assume that the target host runs the same (or a sufficiently
compatible) OS, has a working uv installation and allows key-based SSH
access from your local user. The following steps could as well be performed
by tools like ansible, pyinfra or whatever you prefer.

```
ssh target "mkdir -p /home/myuser/myproj/wheels /home/myuser/myproj/run"
rsync -avxc --exclude .venv ./ target:/home/myuser/myproj/run/
rsync -avxc ../wheels/ target:/home/myuser/myproj/wheels/
ssh target "cd /home/myuser/myproj/run && uv sync --no-index -f ../wheels"
```

If everything was fine, ssh into the target host and verify that your new
installation works as intended, for instance executing a project script or a
Django management command:

```
ssh target "cd /home/myuser/myproj/run && uv run my-proj --help"
```

### Steps 5 and onwards: Repeat for updates

For updates with new versions of your project and/or its dependencies, you
can repeat this process. In order to save time and bandwidth you can recycle
the wheels directories on the local and on the target host; wheel-getter
won't download the same wheels again if they are already present and have
the correct checksum. When rsyncing the wheels to the target host you might
want to add the `--delete` option unless you plan to create another
installation with previously used wheels. Running installations won't need
the wheels in the “wheelhouse” any more.

## If you find a bug or want to improve this tool …

… you are welcome to write a bug report or, preferably, supply a PR. Please
be aware, though, that I may be slow (but willing) to respond; my primary
concern is that this tool works for me, and I probably haven't run into lots
of edge and corner cases.
