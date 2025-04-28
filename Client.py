import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    try:
        num = int(input("Enter an integer (-1 to exit): "))
        if num == -1:
            break
        # Call the remote method
        result = proxy.compute_factorial(num)
        print(f"Factorial of {num} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")
    except xmlrpc.client.Fault as fault:
        print(f"XML-RPC Fault: {fault.faultCode} - {fault.faultString}")
    except Exception as e:
        print("An unexpected error occurred:", e)