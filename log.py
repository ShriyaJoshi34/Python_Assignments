import logging


logging.basicConfig(filename="text.log",level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')



class Details:


    
    def __init__(self,first,last,message):
        self.first = input("FIRST NAME: ")
        self.last = input("LAST NAME: ")
        self.message = input("Write a message")
        
        logging.debug('Created Details: {} -{}'.format(self.fullname,self.message))
        logging.info('Created Details: {} -{}'.format(self.fullname,self.message))
        logging.warning('Created Details: {} -{}'.format(self.fullname,self.message))
        logging.error('Created Details: There is an error')
        
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
d_1 = Details('','','')


    

              

    

              
