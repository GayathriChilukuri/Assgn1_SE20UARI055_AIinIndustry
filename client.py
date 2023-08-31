import requests

def send_message(message):
    url = 'http://SERVER_IP:5000/api/messages'
    data = {'message': message}
    response = requests.post(url, json=data)
    return response.json()

if __name__ == '__main__':
    while True:
        message = input("Enter a message to send to the server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        response = send_message(message)
        print("Server response:", response)
