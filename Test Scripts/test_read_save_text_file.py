import time


def test_read():
    """Test method for the read action of the save_text_file microservice"""
    service_file = "../Text Files/file-service.txt"

    action = "r"
    file_to_read = "./Text Files/test_read.txt"

    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_read)

    time.sleep(5)

    with open(service_file, "r") as f:
        content = f.readlines()

    print(content)

def main():
    test_read()
if __name__ == "__main__":
    main()