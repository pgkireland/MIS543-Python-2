import sys  # Import the sys module to access command line arguments
import requests  # Import the requests library for making HTTP requests

def main():
    # Check if exactly two command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python web_client.py <URL> <filename>")
        sys.exit(1)  # Exit the program with an error code if not

    # Assign the first command line argument to 'url' and the second to 'filename'
    url = sys.argv[1]  # The URL to fetch
    filename = sys.argv[2]  # The file name where content will be saved

    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        # Check for HTTP errors (like 404 or 500)
        response.raise_for_status()  # This will raise an error for bad responses

        # If the response is successful (status code 200), write the content to the file
        with open(filename, 'wb') as file:
            file.write(response.content)

        # Print a success message indicating where the content was saved
        print(f"Successfully saved content from {url} to {filename}")

    except requests.exceptions.HTTPError as e:
        # If a bad response is received, write the HTTP response line to the specified file
        with open(filename, 'w') as file:  # Open the file in write mode ('w')
            # Write the HTTP response line (status code and reason) to the file
            file.write(f"{e.response.status_code} {e.response.reason}\n")

        # Print an error message with the response status code
        print(f"Received HTTP error {e.response.status_code}: {e.response.reason}. Response written to {filename}.")

    except requests.exceptions.RequestException as e:
        # Handle any other exceptions that occur during the request
        print(f"Error fetching {url}: {e}")  # Print the error message

# This checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Call the main function to start the program
