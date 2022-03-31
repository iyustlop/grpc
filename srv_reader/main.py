import sales_records_pb2
import sales_records_pb2_grpc
import grpc
from repositories.file_repository import FileRepository

def main():
    file_repository = FileRepository('/tmp/data/100_sr.csv')
    data_readed = file_repository.read_data()

    for row in data_readed:
        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_records_pb2_grpc.SalesRecordsStub(channel)
            request = sales_records_pb2.EmptyMesage()
            result = stub.PingSalesRecords(request)
            print(f"GRPC received: {result.ack}")


if __name__ == "__main__":
    main()