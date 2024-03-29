.PHONY = pb2

SHELL := /bin/bash

pb2:
	pip install grpcio grpcio-tools
	python -m grpc_tools.protoc -I protobufs --python_out=srv_persistor/ --grpc_python_out=srv_persistor/ protobufs/sales_records.proto

	cp -R srv_persistor/sales_records_pb2.py srv_reader
	cp -R srv_persistor/sales_records_pb2_grpc.py srv_reader

	rm -r env