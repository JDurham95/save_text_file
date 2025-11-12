

def test_save():
    """Test function for the write action of the save_text_file microservice"""
    service_file = "../Text Files/file-service.txt"

    action = "w"
    saved_file_name = "test_save.txt"
    saved_file_text = "Input text to save in test_save.txt here"

    with open(service_file, "w") as f:
        f.write(action + "\n" + saved_file_name + "\n" + saved_file_text)

def main():
    test_save()
if __name__ == "__main__":
    main()