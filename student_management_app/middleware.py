import time


def log_middleware(get_response):
    def middleware(request):
        # Capture the start time
        start_time = time.time()

        response = get_response(request)

        # Calculate execution_time
        end_time = time.time()
        execution_time = end_time - start_time

        # Save data to a file
        log_data = (
            f"Path: {request.path}, Method: {request.method}, "
            + f"Execution Time: {execution_time} seconds\n"
        )

        with open("request_log.txt", "a") as log_file:
            log_file.write(log_data)

        return response

    return middleware
