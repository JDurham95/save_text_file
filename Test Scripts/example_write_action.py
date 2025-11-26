
def write_example():

    #define the service file directory
    service_file = "../Text Files/file-service.txt"

    #define the action, file name, and text to save
    action = "w"
    saved_file_name = "Text Files/synth_params.txt"
    saved_file_text = {"osc" : "sine", "amp": "100", "freq" : "432"}

    #write the parameters to the service file
    with open(service_file, "w") as f:
        f.write(action + "\n" + saved_file_name + "\n" + str(saved_file_text))

def main():
    write_example()
if __name__ == "__main__":
    main()