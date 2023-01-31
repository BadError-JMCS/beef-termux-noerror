import os
purple = "\033[0;35m"                                                                                white = "\033[0;37m"
bred = "\033[1;31m"                                                                                  print(f"\n\n{bred}You Have To Change Beef User Name And Password !")
sd = input(f"\n{purple}Press Any Key To Continue :{white}")
os.system("cd beef && nano config.yaml")
print ("enter ' ./beef ' To Launch beef")