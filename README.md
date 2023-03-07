# simple-grpc

## Getting started

### Step 1

Pull the repo.

### Step 2

Set up the `venv` in `/server` and activate the `venv` with the following commands

```
$ cd server
$ python3 -m venv ./venv
$ . ./activate
```

After that, start the gRPC server

```
$ python server.py
```

### Step 3

Build and up the `envoy` to connect with the gRPC server.

> Please do it in another terminal window

```
$ cd envoy
$ docker build -t .
$ docker compose up
```

### Step 4

Run the GUI client locally.

```
$ cd client
$ quasar dev
```
