#!/bin/bash

PROTO_DIR=./tron_sdk_py/proto/
rm -rf ${PROTO_DIR}/*

# git clone https://github.com/googleapis/googleapis
# pip install pycryptodome ecdsa base58 grpcio grpcio-tools googleapis-common-protos
python3 -m grpc_tools.protoc -Iproto \
    -I /usr/local/include/google/protobuf/ \
    -I./googleapis \
    --python_out=./ --grpc_python_out=./ \
    proto/${PROTO_DIR}/api/*.proto \
    proto/${PROTO_DIR}/core/*.proto \
    proto/${PROTO_DIR}/core/contract/*.proto
