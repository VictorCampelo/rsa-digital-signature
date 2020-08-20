import rsa

class Digital_signature:
    def __read_file(self, file):
        f = open(file, 'rb')
        data = f.read()
        f.close()
        return data

    def show_public_key(self):
        return self.__read_file('public_key.txt')

    def show_private_key(self):
        return self.__read_file('private_key.txt')

    def show_signature(self):
        return self.__read_file('signature.txt')

    def generate_key(self):
        (public_key, private_key) =  rsa.newkeys(2048)
        print("Creating keys...")
        try:
            with open("public_key.txt", "wb") as outfile:
                outfile.write(public_key.save_pkcs1('PEM'))
        except IOError:
            print('erro')

        try:
            with open("private_key.txt", "wb") as outfile2:
                outfile2.write(private_key.save_pkcs1('PEM'))
            print("Keys created!!")
        except IOError:
            print('erro')
    
    def sign(self, doc):
        pvt = rsa.PrivateKey.load_pkcs1(self.__read_file('private_key.txt'))

        doc = self.__read_file(doc)

        sing_hash = rsa.compute_hash(doc, 'SHA-512')

        signature = rsa.sign(doc, pvt, 'SHA-512')

        try:
            with open("signature.txt", "wb") as outfile2:
                outfile2.write(signature)
        except IOError:
            print('erro')
    
    def verify_signature(self, doc):
        pbc = rsa.PublicKey.load_pkcs1(self.__read_file('public_key.txt'))

        doc = self.__read_file(doc)

        signature = self.__read_file('signature.txt')

        try:
            rsa.verify(doc, signature, pbc)
            print('\n!!! Signature is valid. Document has not been modified. !!!\n')
        except:
            print('\n!!! Document has been modified or do not have digital signature. !!!\n')