import urlshort

def main():
    input_link = input("Insert the ID to lookup: ")
    if not input_link:
        print("No ID was entered")
        return
    db = urlshort.Database(4)

if __name__ == "__main__":
    main()