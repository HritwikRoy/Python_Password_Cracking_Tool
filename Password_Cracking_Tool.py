'''print("*** ***********                 *****                  ******************      ******************      ***                                             ***          *********          *** ***********     *** ********                                                                              ")
print("*** ***********                *** ***                *******************     *******************       ***                                           ***         *************        *** ***********     *** *********                                                                   ")
print("***         ***               ***   ***              *****                   *****                       ***                                         ***         ***         ***       ***         ***     ***         ***                                                           ")
print("***         ***              ***     ***              *****                   *****                       ***                                       ***         ***           ***      ***         ***     ***          ***                                                          ")
print("***         ***             ***       ***               *****                   *****                      ***                                     ***          ***           ***      ***         ***     ***           ***                                                         ")
print("***         ***            ***         ***                  ****                   ****                     ***               ******              ***           ***           ***      ***         ***     ***            ***                                                        ")
print("***         ***           ***           ***                    ***                    ****                   ***             *** ***             ***            ***           ***      ***         ***     ***            ***                                                       ")
print("*** ***********          *** *********** ***                      ***                    ***                  ***           ***   ***           ***             ***           ***      *** ***********     ***            ***                                                            ")
print("*** ***********         *** ************* ***                       ****                    ****               ***         ***     ***         ***              ***           ***      *** ***********     ***            ***                                                              ")
print("***                    ***                 ***                        *****                   *****             ***       ***       ***       ***               ***           ***      ***   ****          ***           ***                                                        ")
print("***                   ***                   ***                        *****                    *****            ***     ***         ***     ***                ***           ***      ***     ****        ***          ***                                                            ")
print("***                  ***                     ***                        *****                    *****            ***   ***           ***   ***                  ***          ***      ***      ****       ***         ***                                                             ")
print("***                 ***                       ***        ********************     ********************             *** ***             *** ***                    *************        ***        ****     *** *********                                                                       ")
print("***                ***                         ***       *******************      *******************               *****               *****                       **********         ***          ****   *** ********                                                                        ")

'''

pas=input("Enter Your Password :")
file_name=input("Enter Your File Name :")


f=open(file_name,"r")
L=f.readlines()

for i in L:
    print(i)
    if(i=="admin"+"\n"):
        print("your Password Is : ",i)
        break
else:
    print("password not found")
   

f.close()

