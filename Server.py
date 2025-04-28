from xmlrpc.server import SimpleXMLRPCServer

def compute_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Create the server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the function
server.register_function(compute_factorial, "compute_factorial")

# Start the server
server.serve_forever()