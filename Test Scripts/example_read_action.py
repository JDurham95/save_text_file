import time

def example_read():

    #define the path for the service file
    service_file = "../Text Files/file-service.txt"

    #define the read action and file to read
    action = "r"
    file_to_read = "./Text Files/synth_params.txt"

    #write the action and file name to the service file
    with open(service_file, "w") as f:
        f.write(action + "\n" + file_to_read)

    #wait for the microservice to fill the action
    time.sleep(7)

    #read the content from the service file
    with open(service_file, "r") as f:
        content = f.readlines()

    #print the content and cleanse the service file
    print(content)
    open(service_file, "w").close()

def main():
    example_read()
if __name__ == "__main__":
    main()