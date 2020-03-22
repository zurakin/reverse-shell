

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
            length = f'{len(self.bin):<10}'.encode()
            self.message = (length + self.bin)
        elif type ==2:
            self.utf = message.decode('utf-8', errors ='ignore')[10:]
            self.bin = message[10:]
            self.message = message
    def get_size(self):
        try:
            return int(self.original[:10])
        except:
            return len(self.original)
