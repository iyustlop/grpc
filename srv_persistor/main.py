import grpc
import sales_records_pb2
import sales_records_pb2_grpc
from concurrent import futures

def main():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sales_records_pb2_grpc.add_SalesRecordsServicer_to_server(sales_records_pb2_grpc.SalesRecords(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("GRPC persistor server working")
    server.wait_for_termination()


if __name__ == "__main__":
    main()