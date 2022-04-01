import sales_records_pb2
import sales_records_pb2_grpc
import grpc
from repositories.file_repository import FileRepository
import os


def main():
    file_repository = FileRepository('/tmp/data/100_sr.csv')
    data_readed = file_repository.read_data()

    resource = os.environ["HOSTNAME"]

    for row in data_readed:
        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_records_pb2_grpc.SalesRecordsStub(channel)
            request = sales_records_pb2.SalesRecordsRequest(region=row[0],
                                                            item_type=row[1],
                                                            units_sold=row[2],
                                                            unit_price=row[3],
                                                            unit_cost=row[4],
                                                            source=resource)
            result = stub.SendSalesRecords(request)
            print(f"GRPC received: {result.data}")


if __name__ == "__main__":
    main()
