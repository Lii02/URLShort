from common import Database

def main():
    input_link = input("Insert the link to shorten: ")
    if not input_link:
        print("No link was entered")
        return
    db = Database(8)
    db.add(input_link)
    db.close()

if __name__ == "__main__":
    main()