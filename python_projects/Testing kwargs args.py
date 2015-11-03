#-------------------------------------------------------------------------------
#
# Author:      Roland Junior Toussaint
#
# Created:     29/04/2014
# Copyright:   (c) toussaintr 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def damn(**kwargs): # Allows dictionary use and adding
    print 'I love ' + str(kwargs) + '!'

damn(butt = 'hole', tickle = 'me')

def shit(*args): # Allows unlimted parameters in tuple form
    print 'Damn that is a cold ' + args + ' bitch!'

shit('butt', 'hole')
