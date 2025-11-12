import time

def test_append():
    """ Test function for the append action of the save_text_file microservice """
    service_file = "../Text Files/file-service.txt"

    action = "a"
    file_to_append = "Text Files/test_append.txt"
    text_to_append = "enter text to append here "

    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_append + "\n" + text_to_append)


def main():
    test_append()
if __name__ == "__main__":
    main()
