import urlshort

def main():
    input_id = input("Insert the ID to lookup: ")
    if not input_id:
        print("No ID was entered")
        return
    db = urlshort.Database(4)
    link = db.lookup(input_id)
    if link:
        print(f"Link: {link}")
    db.close()

if __name__ == "__main__":
    main()