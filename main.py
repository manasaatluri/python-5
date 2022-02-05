import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A04WFnXR23PQmLKP4zFCsZHdy-pdBCaCzIj4sMwcvvI9kz3r3UUfrcL4uzfWKSr6hWjhGumyVUEsazEiFxqNZCjDGwl4Rv3YooB0ivEpOtSCG8iNdrP4ifRIVch0wpj8qwWf-6o'
    transferData = TransferData(access_token)

    file_from = input("File to be transfered ")
    file_to =  input(" Enter full path to upload the file to, including the file name")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Your File has been uploaded")


main()