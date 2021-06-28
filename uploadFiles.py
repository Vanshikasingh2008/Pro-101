import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def uploadFile(self, fileFrom, fileTo):
        dbox = dropbox.Dropbox(self.accessToken)
        file = open(fileFrom, "w")
        dbox.files_upload(file.write(), fileTo)

def main():
    access_token = "I0DQOWYCwBkAAAAAAAAAAbZXmPqaIIuLJZESLX_Gy0lvN3H42lkbHOjuLBaEN2lV"
    data = TransferData(access_token)
    file_from = input("Enter the file name:- ")
    file_to = input("Enter the entire path of the file :- ")
    data.uploadFile(file_from, file_to)
    print("File is transferred !!!")

main()
