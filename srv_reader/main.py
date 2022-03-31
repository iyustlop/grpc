from urllib import request
import sales_records_pb2
import sales_records_pb2_grpc
import grpc


def main():
    with grpc.insecure_channel('srv_persistor:50051') as channel:
        stub = sales_records_pb2_grpc.SalesRecordsStub(channel)
        request = sales_records_pb2.EmptyMesage()
        result = stub.PingSalesRecords(request)
        print(f"GRPC received: {result.ack}")


if __name__ == "__main__":
    main()
