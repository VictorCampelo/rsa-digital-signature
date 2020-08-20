from digital_signature import Digital_signature
import os

if __name__ == "__main__":
    ds = Digital_signature()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        dig = int(input("1 - Generate Key \n2 - Documment Sign\n3 - Verify signature\n4 - Show Public Key\n5 - Show Private Key\n6 - Show Signature\n0 - Exit\n-- > "))
        print('\n')
        if dig == 1:
            ds.generate_key()
        elif dig == 2:
            doc_path = input("Insert the Document's name: ")
            ds.sign(doc_path)
        elif dig == 3:
            doc_path = input("Insert the Document's name to be verified: ")
            ds.verify_signature(doc_path)
        elif dig == 4:
            print(ds.show_public_key())
        elif dig == 5:
            print(ds.show_private_key())
        elif dig == 6:
            print(ds.show_signature().hex())
        else:
            break

        input("\nPress Enter to continue...")