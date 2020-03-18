

class Message():
    def __init__(self, message, type = 0):
        if type == 0 :
            self.utf = message
            self.bin = message.encode()
            self.message = (f'{len(self.utf):<10}'+self.utf).encode()
        elif type == 1:
            self.bin = message
            self.utf = message.decode('utf-8')
            self.message = (f'{len(self.utf):<10}'+self.utf).encode()
        elif type ==2:
            self.utf = message.decode('utf-8')[10:]
            self.bin = self.utf.encode()
            self.message = message
        self.size = len(self.utf)
