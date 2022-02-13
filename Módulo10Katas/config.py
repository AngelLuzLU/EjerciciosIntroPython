def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!", err)
        elif err.errno == 13:
            print("Found config.txt but couldn't read it", err)
        elif err.errno == 20:
            print("The file exists, but it's a directory!")
        elif err.errno == 102:
            print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()