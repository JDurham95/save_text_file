def example_append():

    #define the path for the service file
    service_file = "../Text Files/file-service.txt"

    #define the action, file name, and text to append
    action = "a"
    file_to_append = "Text Files/synth_params.txt"
    text_to_append = {"col": "#1539FF"}

    #write the content to the service file
    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_append + "\n" + str(text_to_append))


def main():
    example_append()
if __name__ == "__main__":
    main()
