#!/bin/bash

python3 -m grpc_tools.protoc -Iproto \
    -I /usr/local/include/google/protobuf/ \
    --python_out=./ --grpc_python_out=./ \
    proto/tron_sdk_py/proto/api/api.proto proto/tron_sdk_py/proto/core/*
