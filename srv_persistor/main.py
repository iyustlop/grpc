import grpc
import sales_records_pb2
import sales_records_pb2_grpc
from concurrent import futures


class SalesRecords(sales_records_pb2_grpc.SalesRecordsServicer):
    def PingSalesRecords(self, request, context):
        response = sales_records_pb2.PingSalesRecordsResponse(ack='1')
        return response

    def SendSalesRecords(self, request, context):
        print(request.region)
        print(request.source)

        response = sales_records_pb2.SalesRecordsResponse(data=request.unit_cost)
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sales_records_pb2_grpc.add_SalesRecordsServicer_to_server(
        SalesRecords(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("GRPC persistor server")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
