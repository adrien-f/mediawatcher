# MediaWatcher

Watch directories and move media files accordingly.

```
λ mediawatcher -h
usage: mediawatcher [-h] -c CONFIG

Watch directories and move media files accordingly.

optional arguments:
  -h, --help  show this help message and exit
  -c CONFIG   path to the config file in YAML
```

### Requirements

* Python 3.5
* Some folders to watch ;)

### Installation

You can install MediaWatcher using pip:

```
pip install mediawatcher
```

### Running

First, you'll need a config file, here's an example created in `~/.mediawatcher`:

```
watch:
  - /data/downloads
output_anime: /data/media/anime
output_tv: /data/media/tv
output_movies: /data/media/movies
```

And then, run mediawatcher:

```
mediawatcher -c ~/.mediawatcher
```

### License

MIT License

Copyright (c) [2016] [@adrien-f]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.