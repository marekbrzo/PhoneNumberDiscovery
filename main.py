class PhoneNumber:
    """ Phone class represents and manipulates x,y coords. """

    def __init__(self,number,value):
        """ Create a new phone number """
        self.number = number
        self.value = value
    
    def remainder(self):
        """ Remainder check"""
        return(int(self.number) % self.value)

    def replaceChar(self):
        """ Replacing # with variable """
        return (self.number.replace("#","0"),self.number.replace("#","9"))

    def checkLength(self):
        """ Quick check to determine if the unknown number is correct in lenght. Must have
        a string of 10 characters"""
        return (len(self.number) )




def main(min,max,val):
    """ Main function, with a quick check at the beginning """
    for i in range(int(min),int(max)):
        if PhoneNumber(unknownNumber,divisibleBy).checkLength() != 10:
            raise Exception("Sorry,  please input a proper 10 digit string with # as the missing values")
        
        # Returns a phone number that matches the met conditions, must have a remainder of value
        if PhoneNumber(i,val).remainder() == 0:
            print('Your Phone Number is: (with a remainder %d) \n%d' % (val,i))
            return

# Variables 
divisibleBy = 13                # Remainder by
unknownNumber = "20#23##016"     # 10-digit with characters of the unknwon number


print('Your unknown number is ',(unknownNumber))
minNumber, maxNumber = PhoneNumber(unknownNumber,divisibleBy).replaceChar()
main(minNumber,maxNumber,divisibleBy)

