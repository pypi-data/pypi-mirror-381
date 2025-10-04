[![Python package](https://github.com/Jylpah/queutils/actions/workflows/python-package.yml/badge.svg)](https://github.com/Jylpah/queutils/actions/workflows/python-package.yml)  [![codecov](https://codecov.io/gh/Jylpah/queutils/graph/badge.svg?token=rMKdbfHOFs)](https://codecov.io/gh/Jylpah/queutils)

# Queutils

Queutils *[Queue Utils]* is a package of handy Python queue classes:

- **[AsyncQueue](docs/asyncqueue.md)** - An `async` wrapper for non-async `queue.Queue`
- **[IterableQueue](docs/iterablequeue.md)** - An `AsyncIterable` queue that terminates when finished
- **EventCounterQueue** - An `IterableQueue` for counting events in `async` threads
- **[FileQueue](docs/filequeue.md)** - Builds an `IterableQueue[pathlib.Path]` of filenames from files/dirs given as input


# AsyncQueue

[`AsyncQueue`](docs/asyncqueue.md) is a async wrapper for non-async `queue.Queue`. It can be used to create 
an `asyncio.Queue` compatible interface to a (non-async) managed `multiprocessing.Queue` and thus enable `async` code in parent/child processes to communicate over  `multiprocessing.Queue` as it were an `asyncio.Queue`. Uses `sleep()` for `get()`/`put()` if the queue is empty/full.

## Features 

- `asyncio.Queue` compatible
- `queue.Queue` support
- `multiprocessing.Queue` support


# IterableQueue

[`IterableQueue`](docs/iterablequeue.md) is an `asyncio.Queue` subclass that is `AsyncIterable[T]` i.e. it can be 
iterated in `async for` loop. `IterableQueue` terminates automatically when the queue has been filled and emptied. 

The `IterableQueue` requires "producers" (functions adding items to the queue) to register themselves with `add_producer()` call. It keeps count of registered producers. When a producer "finishes" adding items to the queue, 
it needs to unregister itself with `finish_producer()` call. Once all the registered 
producers are "finished", the queue enters into "filled" state and no new items can be added. Once a "filled" queue has been emptied, the queue becomes "done" and 
all new `get()` calls to the queue will `raise QueueDone` exception. 
    
## Features

- `asyncio.Queue` interface, `_nowait()` methods are experimental
- `AsyncIterable` support: `async for item in queue:`
- Automatic termination of the consumers with `QueueDone` exception when the queue has been emptied 
- Producers must be registered with `add_producer()` and they must notify the queue
  with `finish_producer()` once they have finished adding items 
- Countable interface to count number of items task_done() through `count` property

# EventCounterQueue

`EventCounterQueue` can be used to count named events (default event is `count`) between `async` threads. `async` worker threads call `queue.send(event="event_name", N=amount)`. The receving end can either `receive()` a single event or `listen()` all  events and return `collections.defaultdict[str, int]` as a result.

## Features

- Supports multiple producers and a single listener
- Default event is `count`


# FileQueue

[`FileQueue`](docs/filequeue.md) builds a queue (`IterableQueue[pathlib.Path]`) of the matching 
files found based on search parameters given. It can search both list of files or directories or 
mixed. Async method `FileQueue.mk_queue()` searches subdirectories of given directories.  

## Features

- Input can be given both as `str` and `pathlib.Path`
- `exclude: bool` exclusive or  inclusive filtering. Default is `False`.
- `case_sensitive: bool` case sensitive filtering (use of `fnmatch` or `fnmatchcase`). Default is `True`.
- `follow_symlinks: bool` whether to follow symlinks. Default is `False`.

