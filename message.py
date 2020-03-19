

class Message():
    def __init__(self, message, type = 0):
        self.original = message
        if type == 0 :
            self.utf = message
            self.bin = message.encode()
            self.message = (f'{len(self.utf):<10}'+self.utf).encode()
        elif type == 1:
            self.bin = message
            self.utf = message.decode('utf-8', errors ='ignore')
            self.message = (f'{len(self.utf):<10}'+self.utf).encode()
        elif type ==2:
            self.utf = message.decode('utf-8')[10:]
            self.bin = self.utf.encode()
            self.message = message
    def get_size(self):
        return int(self.original.decode('utf-8')[:10])
